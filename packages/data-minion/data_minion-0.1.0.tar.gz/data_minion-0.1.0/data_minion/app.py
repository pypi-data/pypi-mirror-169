import json
from pathlib import Path
import re
import sys
from subprocess import Popen, CREATE_NEW_CONSOLE

import PySimpleGUIQt as sg

import data_minion.files_and_folders as ff
import data_minion.handle_settings as hs
from data_minion.json_to_xlsx import export_to_xlsx as j2x
from data_minion.set_settings import set_settings
import data_minion.split_students as ss

# pylint: disable=no-member

def selected_student_name(values: dict, window: sg.Window):
    if values['selected_student_name'] == []:
        return
    name = values['selected_student_name'][0]
    name = re.sub(r'\n.+', '', name)
    student = ff.get_one_student(name, values['selected_all_students_file'])
    text = ['Grade\t  Overdue\tLast Visited']
    text.append('----------------------------------------')
    for course in student['courses']:
        text.append(f'\n{course["course"]}\n{course["grade"]}\t  {course["overdue"]}\t{course["visited"]}')
        text.append('____________________________________')
    text = '\n'.join(text)
    window['courses_info'].update(text)

def selected_kudos_uhoh_student_name(values: dict, event: str, window: sg.Window):
    group = event.replace('selected_', '')
    group = group.replace('_student_name', '')
    if values[f'selected_{group}_student_name'] == []:
        return
    name = values[f'selected_{group}_student_name'][0]
    name = re.sub(r'\n.+', '', name)
    student = ff.get_one_student_from_split_file(name, values[f'selected_{group}_file'])
    text = ['Grade\t  Overdue\tLast Visited']
    text.append('----------------------------------------')
    for course in student['courses']:
        text.append(f'\n{course["course"]}\n{course["grade"]}\t  {course["overdue"]}\t{course["visited"]}')
        text.append('____________________________________')
    text = '\n'.join(text)
    window[f'{group}_courses_info'].update(text)

def export(values):
    result = j2x(
        values['selected_all_students_file'], 
        values['selected_class_list']
        )
    if result == 'cancelled':
        return
    elif result == 'PermissionError':
        sg.popup_quick_message('Cannot overwrite file because it is opened in another program')
    else:
        sg.popup_ok(f'Data exported to Excel and saved to\n{result}')

def split_students(values, window):
    from_file = values['selected_all_students_file']
    from_file = ff.get_absolute_from_file(from_file)
    with open(from_file, 'r') as f:
        class_lists = json.load(f)
    result = ss.split_students(class_lists, values['selected_class_list'])
    if result:
        kudos_uhoh = ff.get_kudos_and_uhoh()
        kudos_students = [f"{x['name']}\n\t\t{x['average_grade']}" for x in ff.get_kudos_uhoh_students(kudos_uhoh[0][0])]
        uhoh_students = [f"{x['name']}\n\t\t{x['average_grade']}" for x in ff.get_kudos_uhoh_students(kudos_uhoh[1][0])]
        window['selected_kudos_file'].update(values=kudos_uhoh[0])
        window['selected_uhoh_file'].update(values=kudos_uhoh[1])
        window['selected_kudos_student_name'].update(kudos_students)
        window['selected_uhoh_student_name'].update(uhoh_students)
        sg.popup_quick_message('Students have been grouped')
    else:
        sg.popup_quick_message('Failed to group students')

def selected_class_list(values, window):
    students = ff.get_all_student_info_from_file(
        values['selected_all_students_file'], 
        values['selected_class_list']
        )
    if not students:
         window['selected_student_name'].update(['no students found'])
         return
    names = [f"{x['name']}\n\t\t{x['average_grade']}" for x in students if x['courses']]
    window['selected_student_name'].update(names)

def selected_kudos_uhoh_file(values: dict, event, window: sg.Window):
    subgroup = event.replace('selected_', '')
    subgroup = subgroup.replace('_file', '')
    students = ff.get_kudos_uhoh_students(values[f'selected_{subgroup}_file'])
    names = [f"{x['name']}\n\t\t{x['average_grade']}" for x in students if x['courses']]
    window[f'selected_{subgroup}_student_name'].update(names)

def update_settings(values):
    settings = hs.get_settings()
    settings['login_url'] = values['login_url']
    settings['class_home_url'] = values['class_home_url']
    settings['get_new_class_lists'] = values['get_new_class_lists']
    hs.save_settings(settings)

def launch_data_collection(values, main_dir):
    settings = hs.get_settings()
    update_settings(values)
    s = ['login_url', 'class_home_url', 'kudos', 'uhoh', 'output_folder', 'class_lists']
    for x in s:
        if settings[x] in ['', None, []]:
            sg.popup_quick_message('Some required settings are missing')
            return
    Popen(f'{sys.executable.replace("pythonw", "python")} {main_dir}/collect_data.py', creationflags=CREATE_NEW_CONSOLE)

def class_lists_listbox(settings):
    names_urls = []
    for class_list in settings['class_lists']:
        names_urls.append(f'{class_list["name"]} | {class_list["url"]}')
    return names_urls

def get_all_students_files_for_combo():
    files = ff.get_all_students_files()
    files = [f.split('/')[-1] for f in files]
    files = sorted(files, reverse=True)
    if files != []:
        return files
    else:
        return ['']

def add_class_list(values, window):
    if values['new_class_list_name'] == '' or values['new_class_list_url'] == '':
        return
    new_class_list = {'name': values['new_class_list_name'], 'url': values['new_class_list_url']}
    settings = hs.get_settings()
    settings['class_lists'].append(new_class_list)
    hs.save_settings(settings)
    window['listbox_class_lists'].update(class_lists_listbox(settings))

def delete_class_list(values, window):
    if values['listbox_class_lists'] == []:
        return
    settings = hs.get_settings()
    for class_list_to_remove in values['listbox_class_lists']:
        name_to_remove = class_list_to_remove.split(' | ')[0]
        for i, class_list in enumerate(settings['class_lists'], 0):
            if name_to_remove == class_list['name']:
                settings['class_lists'].pop(i)
    hs.save_settings(settings)
    window['listbox_class_lists'].update(class_lists_listbox(settings))

def get_layout(settings: dict, all_student_filenames, newest_grouped_file, kudos_uhoh):
    menu_bar = [
            ['File', ['Settings']],
        ]
    data_collection_settings_frame = [
        [sg.T('Log In URL:', size=(15, 1)), sg.I(settings.get('login_url'), key='login_url')],
        [sg.T('Class Home URL:', size=(15, 1)), sg.I(settings.get('class_home_url'), key='class_home_url')],
        [sg.T('Class List URLs:', size=(15, 1)), sg.Listbox(class_lists_listbox(settings), key='listbox_class_lists', select_mode=sg.SELECT_MODE_EXTENDED)],
        [sg.B('Add Class List URL', key='add_class'), sg.I('name', key='new_class_list_name'), sg.I('URL', key='new_class_list_url'), sg.B('Delete Selected Class List(s)', key='delete_class')],
        [sg.Checkbox('Get New Class Lists', default=settings['get_new_class_lists'], key='get_new_class_lists')]
    ]
    data_collection_tab = [
        [sg.Frame('Data Collection Settings', data_collection_settings_frame)],
        [sg.Button('Launch Data Collection Script', key='scrape')]
    ]

    try:
        selected_class_list_items = [x['class_list'] for x in newest_grouped_file]
        all_student_names = [f"{x['name']}\n\t\t{x['average_grade']}" for x in newest_grouped_file[0]['students']]
    except:
        selected_class_list_items = ['']
        all_student_names = ['']

    all_students_tab = [
        [sg.Combo(all_student_filenames, enable_events=True, key='selected_all_students_file', readonly=True), 
                    sg.Combo(selected_class_list_items, key='selected_class_list', readonly=True, enable_events=True)],
        [sg.Listbox(all_student_names, enable_events=True, key='selected_student_name', select_mode=sg.SELECT_MODE_SINGLE),
                    sg.Multiline(key='courses_info', enable_events=True)],
        [sg.Button('Group Students into "Kudos" and "Uhoh" Groups', key='split_students'), 
                    sg.Button('Export to Excel', key='export')],
    ]

    try:
        kudos_students = [f"{x['name']}\n\t\t{x['average_grade']}" for x in ff.get_kudos_uhoh_students(kudos_uhoh[0][0])]
    except:
        kudos_students = ['']

    kudos_tab = [
        [sg.Combo(kudos_uhoh[0], enable_events=True, key='selected_kudos_file', readonly=True), sg.T('')],
        [sg.Listbox(kudos_students, enable_events=True, key='selected_kudos_student_name'),
                    sg.Multiline(key='kudos_courses_info', enable_events=True)],
    ]

    try:
        uhoh_students = [f"{x['name']}\n\t\t{x['average_grade']}" for x in ff.get_kudos_uhoh_students(kudos_uhoh[1][0])]
    except:
        uhoh_students = ['']

    uhoh_tab = [
        [sg.Combo(kudos_uhoh[1], enable_events=True, key='selected_uhoh_file', readonly=True), sg.T('')],
        [sg.Listbox(uhoh_students, enable_events=True, key='selected_uhoh_student_name'),
                    sg.Multiline(key='uhoh_courses_info', enable_events=True)],
    ]

    return [
        [sg.Menu(menu_bar)],
        [sg.TabGroup(
             [[
                sg.Tab('Data Collection', data_collection_tab), 
                sg.Tab('All Students', all_students_tab),
                sg.Tab('Kudos', kudos_tab),
                sg.Tab('Uhoh', uhoh_tab),
             ]])
            ]
    ]

def main():
    settings = hs.get_settings()
    sg.theme(settings['theme'])
    sg.set_options(border_width=1)
    all_student_filenames = get_all_students_files_for_combo()
    newest_grouped_file = ff.get_newest_grouped_file_open()
    kudos_uhoh = ff.get_kudos_and_uhoh()
    layout = get_layout(settings, all_student_filenames, newest_grouped_file, kudos_uhoh)
    version = 'v0.9.1'
    main_dir = Path(__file__).parent.as_posix()
    icon = f'{main_dir}/resources/data_minion.ico'
    window = sg.Window(f'data_minion {version}', layout, icon=icon, size=(1200, 600))
    while True:
        event, values = window.read()
        if event in ('exit', None, sg.WINDOW_CLOSED):
            break
        elif event == 'add_class':
            add_class_list(values, window)
        elif event == 'delete_class':
            delete_class_list(values, window)
        elif event == 'scrape':
            launch_data_collection(values, main_dir)
        elif event == 'split_students':
            split_students(values, window)
        elif event == 'selected_class_list':
            selected_class_list(values, window)
        elif event == 'selected_all_students_file':
            selected_class_list(values, window)
        elif event == 'selected_uhoh_file' or event == 'selected_kudos_file':
            selected_kudos_uhoh_file(values, event, window)
        elif event == 'export':
            export(values)
        elif event == 'Settings':
            set_settings(main_dir, icon)
        elif event == 'selected_student_name':
            selected_student_name(values, window)
        elif event == 'selected_uhoh_student_name' or event == 'selected_kudos_student_name':
            selected_kudos_uhoh_student_name(values, event, window)
        # print(event)
    window.close()
