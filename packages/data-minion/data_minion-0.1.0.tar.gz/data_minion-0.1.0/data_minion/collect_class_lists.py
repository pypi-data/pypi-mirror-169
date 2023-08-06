import json
import time
from typing import List

from helium import go_to, find_all, S

def reformat_class_list(students):
    new_list = []
    for s in students:
        names = s.split(', ')
        first_last = f'{names[1]} {names[0]}'
        new_list.append(first_last)
    return new_list

def get_class_lists(class_lists: List[dict], output_fn):
    output_fn = f'{output_fn}_CLASS_LISTS.json'
    print('\nGetting names from class list URLs for sorting...')
    students_by_class_list = []
    for c in class_lists:
        print(f'Going to {c["name"]}')
        go_to(c['url'])
        print('\nLetting the page load for five seconds...')
        time.sleep(5.0)
        students = find_all(S('.d_ich'))
        print(f'\nFound {len(students)} students in this class list.')
        students_list = [student.web_element.text for student in students]
        students_list = reformat_class_list(students_list)
        students_by_class_list.append({'name': c['name'], 'students': students_list})
    with open(output_fn, 'w') as f:
        json.dump(students_by_class_list, f, indent=4)
    print(f'''
Student names by class list affiliation have been saved to {output_fn}''')
    return output_fn

def group_students_by_class(all_students_fn, students_by_class_fn, output_fn):
    output_fn = f'{output_fn}_GROUPED.json'
    with open(all_students_fn, 'r') as f:
        all_students_data = json.load(f) #type: list
    with open(students_by_class_fn, 'r') as f:
        class_lists = json.load(f)

    grouped_students = []
    for class_list in class_lists:
        students_found_in_class_list = []
        for student in all_students_data:
            if student['name'] in class_list['students']:
                students_found_in_class_list.append(student)
                all_students_data.remove(student)
        grouped_students.append({'class_list': class_list['name'], 'students': students_found_in_class_list})
    grouped_students.append({'class_list': 'ungrouped', 'students': all_students_data})
    
    with open(output_fn, 'w') as f:
        json.dump(grouped_students, f, indent=4)
    print(f'\nGrouped students file saved to\n{output_fn}')

