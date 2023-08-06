import datetime
import json
from pathlib import Path
import re
import time

from bs4 import BeautifulSoup
from helium import * # pylint: disable=unused-wildcard-import

from data_minion.collect_class_lists import get_class_lists, group_students_by_class
from data_minion.add_average_grade import add_average_grade


def get_output_fn(output_dir):
    timestamp = datetime.datetime.now().strftime('%G-%m-%d_%H.%M')
    output_dir = Path(output_dir).as_posix()
    return f'{output_dir}/{timestamp}'

def get_settings():
    main_dir = Path(__file__).parent.as_posix()
    with open(f'{main_dir}/resources/settings.json', 'r') as f:
        settings = json.load(f)
    return (settings['login_url'], settings['class_home_url'], 
            settings['class_lists'], settings['output_folder'],
            settings['get_new_class_lists'], settings['newest_class_list_fn'])

def edit_settings(key, value):
    main_dir = Path(__file__).parent.as_posix()
    with open(f'{main_dir}/resources/settings.json', 'r') as f:
        settings = json.load(f)
    settings[key] = value
    with open(f'{main_dir}/resources/settings.json', 'w') as f:
        json.dump(settings, f, indent=4)

def reload(driver):
    try:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        click('Load More')
        return True
    except:
        return False

def load_all_students(driver):
    end = False
    while not end:
        clicked = False
        retry = 0
        while not clicked:
            if retry >= 3:
                end = True
                break
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            clicked = reload(driver)
            time.sleep(1.0)
            retry += 1

def scroll_shim(driver, element):
    x = element.location['x']
    y = element.location['y']
    scroll_by_coord = f'window.scrollTo({x},{y});'
    driver.execute_script(scroll_by_coord)

def parse_student_summary(html) -> dict:
    soup = BeautifulSoup(html, features='lxml')
    text = soup.text
    if 'No Courses Found' in text:
        courses_present = False
    else:
        courses_present = True
    text = text.split('Student Summary')[0]
    text = text.replace('Last Login: ', '')
    text = re.split(r'\n+', text.strip())
    if text[0] == 'Discussion forums for you!' or len(text) <= 1:
        return None
    if courses_present:
        student = {'name': text[0], 'id': text[1], 'last_login': text[2], 'courses': []}
    else:
        student = {'name': text[0], 'id': text[1], 'last_login': text[2], 'courses': None}
    rows = soup.find_all('tr')
    for row in rows:
        cleaned = re.split(r'\n+', row.text.strip())
        if cleaned[0] != 'Course':
            student['courses'].append({'course': cleaned[0], 
                                       'grade': cleaned[1], 
                                       'overdue': cleaned[2], 
                                       'visited': cleaned[3]})
    return student

def open_student_summaries(open_summary_buttons, driver):
    for summary in open_summary_buttons:
        clicked = False
        tries = 0
        while not clicked and tries <= 2:
            scroll_shim(driver, summary.web_element)
            try:
                if summary.web_element.get_attribute('icon') == 'tier1:arrow-expand-small':
                    click(summary)
                clicked = True
            except LookupError:
                tries += 1
            time.sleep(0.5)

def try_to_open_summaries(open_summary_buttons, driver):
    print('''
Checking that every "Student Summary" is opened...''')
    try:
        open_student_summaries(open_summary_buttons, driver)
    except:
        answer = input('''
Something went wrong while opening each summary. 
If the page looks like it is still loaded correctly,
then trying again may work. Otherwise, we can continue
and only collect data from the currently opened
summaries.
"Try again" or "continue"?: ''')
        if answer.lower() == 'try again':
            try:
                open_student_summaries(open_summary_buttons, driver)
            except:
                print('''
Something seems to have prevented this tool from opening
all student summaries. Now continuing with what was able
to be opened.''')


def parse_html():
    student_elems = find_all(S('.d2l-datalist-item'))
    all_students = []
    for student in student_elems:
        student_html = student.web_element.get_attribute('innerHTML')
        parsed_student_info = parse_student_summary(student_html)
        if parsed_student_info:
            all_students.append(parsed_student_info)
    return all_students

def main():
    log_in, class_home, class_lists, output_dir, get_new_class_lists, newest_class_list_fn = get_settings()
    print('Launching Firefox...')
    driver = start_firefox(log_in)
    
    input('''

When the page has loaded, enter your credentials
and click "Log In." For security, this automation
tool does not read or store your username or password.
Once your home page loads, press ENTER here to continue: ''')
    print('''
Okay, data_minion will take it from here (unless there is a problem).
Try to leave Firefox open and alone while the script works.''')
    print('\nGoing to class home and waiting for the page to load...')
    go_to(class_home)
    time.sleep(2.0)

    print('\nLoading all students...')
    # load_all_students(driver) #! Don't leave this commented

    print('\nFinding all of the "Open Student Summary" buttons...')
    open_summary_buttons = find_all(S("//d2l-button-icon", to_left_of='Student Summary'))
    print(f'Found about {len(open_summary_buttons)} summaries.')

    try_to_open_summaries(open_summary_buttons, driver)

    print('\nParsing HTML and converting to a JSON file...')
    all_students = parse_html()
    all_students = add_average_grade(all_students)

    output_fn = get_output_fn(output_dir)

    with open(f'{output_fn}_ALL.json', 'w') as f:
        json.dump(all_students, f, indent=4)

    print(f'\nSuccess!\nThe output file has been saved to\n{output_fn}')

    print('\nNow getting class lists for sorting...')
    if get_new_class_lists:
        newest_class_list_fn = get_class_lists(class_lists, output_fn)
        edit_settings('newest_class_list_fn', newest_class_list_fn)

    group_students_by_class(f'{output_fn}_ALL.json', newest_class_list_fn, output_fn)

    input('Press enter to exit: ')

if __name__ == '__main__':
    main()