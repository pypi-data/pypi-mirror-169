import re
import statistics as st
from typing import List


def add_average_grade(students: List[dict]):
    for student in students:
        if student['courses'] is None:
            continue
        grades = []
        for course in student['courses']:
            grade = course['grade']
            if grade.startswith('-'):
                continue
            grade = re.sub(r'%| |[A-Za-z]|-|\+', '', grade)
            try:
                grade = float(grade)
                grades.append(grade)
            except:
                continue
        if grades != []:
            student['average_grade'] = round(st.fmean(grades), 2)
    return students
