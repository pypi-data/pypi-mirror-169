import json
import re
from typing import List

import data_minion.handle_settings as hs

def split_students(all_students: List[dict], class_list: str):
    settings = hs.get_settings()

    kudos_threshold = settings['kudos']
    uhoh_threshold = settings['uhoh']

    uhoh = []
    kudos = []

    for group in all_students:
        if group['class_list'] == class_list:
            students = group['students']
            break
    else:
        return False
    for student in students:
        grades = []
        if student['courses'] is None:
            continue
        for course in student['courses']:
            if course['course'].startswith('ORN010'):
                continue
            grade = course['grade']
            if grade.startswith('-'):
                continue
            grade = re.sub(r'%| |[A-Za-z]|-|\+', '', grade)
            try:
                grade = float(grade)
            except:
                continue
            grades.append(grade)
        if all(i >= kudos_threshold for i in grades):
            kudos.append(student)
        elif any(i <= uhoh_threshold for i in grades):
            uhoh.append(student)


    with open(f"{settings['output_folder']}/{class_list}_kudos.json", 'w') as f:
        json.dump(kudos, f, indent=4)

    with open(f"{settings['output_folder']}/{class_list}_uhoh.json", 'w') as f:
        json.dump(uhoh, f, indent=4)

    return True

def return_split_students(all_students: List[dict]):
    settings = hs.get_settings()

    kudos_threshold = settings['kudos']
    uhoh_threshold = settings['uhoh']

    uhoh = []
    kudos = []

    for student in all_students:
        grades = []
        if student['courses'] is None:
            continue
        for course in student['courses']:
            if course['course'].startswith('ORN010'):
                continue
            grade = course['grade']
            if grade.startswith('-'):
                continue
            grade = re.sub(r'%| |[A-Za-z]|-|\+', '', grade)
            try:
                grade = float(grade)
            except:
                continue
            grades.append(grade)
        if all(i >= kudos_threshold for i in grades):
            kudos.append(student)
        elif any(i <= uhoh_threshold for i in grades):
            uhoh.append(student)
    return kudos, uhoh
