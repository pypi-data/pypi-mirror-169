import json
from pathlib import Path

import data_minion.handle_settings as hs

def get_all_students_files():
    settings = hs.get_settings()
    output_dir = Path(settings['output_folder']).glob('**/*')
    files = [x.absolute().as_posix() for x in output_dir if x.is_file()]
    files = [x for x in files if x.endswith('GROUPED.json')]
    return sorted(files, reverse=True)

def get_all_output_files():
    settings = hs.get_settings()
    output_dir = Path(settings['output_folder']).glob('**/*')
    files = [x.absolute().as_posix() for x in output_dir if x.is_file()]
    return sorted(files, reverse=True)

def get_files_ending_with(ending: str):
    settings = hs.get_settings()
    output_dir = Path(settings['output_folder']).glob('**/*')
    files = [x.absolute().as_posix() for x in output_dir if x.is_file()]
    files = [x for x in files if x.endswith(ending)]
    return files

def get_absolute_from_file(fn):
    files = get_all_output_files()
    for f in files:
        if f.split('/')[-1] == fn:
            return f

def get_all_student_info_from_file(fn, class_list_name: str):
    with open(get_absolute_from_file(fn), 'r') as f:
        items = json.load(f)
    for class_list in items:
        if class_list['class_list'] == class_list_name:
            return class_list['students']

def get_newest_grouped_file_open():
    try:
        newest_grouped_file = get_all_students_files()[0]
        with open(newest_grouped_file, 'r') as f:
            return json.load(f)
    except:
        return ['']

def get_kudos_and_uhoh():
    kudos = get_files_ending_with('kudos.json')
    uhoh = get_files_ending_with('uhoh.json')
    kudos_filenames = []
    uhoh_filenames = []
    for k in kudos:
        kudos_filenames.append(k.split('/')[-1])
    for u in uhoh:
        uhoh_filenames.append(u.split('/')[-1])
    if kudos_filenames == []:
        kudos_filenames = ['']
    if uhoh_filenames == []:
        uhoh_filenames = ['']
    return kudos_filenames, uhoh_filenames

def get_kudos_uhoh_students(fn):
    file_path = get_absolute_from_file(fn)
    with open(file_path, 'r') as f:
        return json.load(f)

def get_one_student(name: str, fn):
    fn = get_absolute_from_file(fn)
    with open(fn, 'r') as f:
        all_class_lists = json.load(f)
    for class_list in all_class_lists:
        for student in class_list['students']:
            if student['name'] == name:
                return student

def get_one_student_from_split_file(name: str, fn):
    fn = get_absolute_from_file(fn)
    with open(fn, 'r') as f:
        students = json.load(f)
    for student in students:
        if student['name'] == name:
            return student