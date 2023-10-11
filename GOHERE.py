import os
import warnings
from flask import Flask
from app.config import Configuration
from app.factory import create_app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Course, Enrollment, Student, Teacher, Subject,db


warnings.simplefilter('ignore', category=Warning, append=True)

app = create_app()
app.config.from_object(Configuration)
db.init_app(app)
database_path = os.environ.get('SQLALCHEMY_DATABASE_URI')
engine = create_engine(f'sqlite:///{database_path}')
Session = sessionmaker(bind=engine)
session = Session()

#run the following terminal commands:
# ||  python -m venv venv_name ||  source venv_name/bin/activate  ||  pip install -r requirements.txt
#  ASSIGNMENT:
# go to models.py.   establish your connections, then come back here and run this page with:
#  python GOHERE.py
#read the printouts and you can see if everyone is connected.  will tell u exactly whats connected and not.

# 1. Get all subjects and their teachers
def subjectsWithTeacher():
    subjects_with_teachers = session.query(Subject.name, Teacher.name).join(Teacher).all()
    if subjects_with_teachers:
        return subjects_with_teachers
    else:
        return "#1 failed. This tests the one-to-many relationship between teacher and subjects."

# 2. Get all teachers and their subjects
def teachersWithSubjects():
    teachers_with_subjects = session.query(Teacher.name, Subject.name).join(Subject).all()
    if teachers_with_subjects:
        return teachers_with_subjects
    else:
        return "#2 failed. This tests the one-to-many relationship between teacher and subjects."

# 3. Get all courses and their enrolled students
def coursesWithStudents():
    courses_with_students = session.query(Course.title, Student.name).join(Enrollment).join(Student).all()
    if courses_with_students:
        return courses_with_students
    else:
        return "#3 failed. This tests the many-to-many relationship between courses and students."

# 4. Get all students and the courses they are enrolled in
def studentsWithCourses():
    students_with_courses = session.query(Student.name, Course.title).join(Enrollment).join(Course).all()
    if students_with_courses:
        return students_with_courses
    else:
        return "#4 failed. This tests the many-to-many relationship between students and courses."

# 5. Get all teachers and the subjects they teach
def teachersWithSubjects():
    teachers_with_subjects = session.query(Teacher.name, Subject.name).join(Subject).all()
    if teachers_with_subjects:
        return teachers_with_subjects
    else:
        return "#5 failed. This tests the one-to-many relationship between teacher and subjects."

# 6. Get all subjects and their teachers
def subjectsWithTeachers():
    subjects_with_teachers = session.query(Subject.name, Teacher.name).join(Teacher).all()
    if subjects_with_teachers:
        return subjects_with_teachers
    else:
        return "#6 failed. This tests the one-to-many relationship between teacher and subjects."

# 7. Get all students and the courses they are enrolled in using a specific student ID (e.g., student_id=2)
def studentCourses():
    student_courses = session.query(Student.name, Course.title).join(Enrollment).join(Course).filter(Student.id == 2).all()
    if student_courses:
        return student_courses
    else:
        return "#7 failed. This tests the many-to-many relationship between students and courses for a specific student ID."

# 8. Get all students enrolled in a specific course (e.g., course_id=3)
def courseStudents():
    course_students = session.query(Student.name).join(Enrollment).join(Course).filter(Course.id == 3).all()
    if course_students:
        return course_students
    else:
        return "#8 failed. This tests the many-to-many relationship between students and courses for a specific course ID."

# 9. Get all teachers for a specific subject (e.g., subject_id=2)
def subjectTeachers():
    subject_teachers = session.query(Teacher.name).join(Subject).filter(Subject.id == 2).all()
    if subject_teachers:
        return subject_teachers
    else:
        return "#9 failed. This tests the one-to-many relationship between teacher and subjects for a specific subject ID."

# 10. Get all subjects for a specific teacher (e.g., teacher_id=3)
def teacherSubjects():
    teacher_subjects = session.query(Subject.name).join(Teacher).filter(Teacher.id == 3).all()
    if teacher_subjects:
        return teacher_subjects
    else:
        return "#10 failed. This tests the one-to-many relationship between teacher and subjects for a specific teacher ID."

# Print the results of each query

print('Subjects with teachers:', subjectsWithTeacher())
print('Teachers with subjects:', teachersWithSubjects())
print('Courses with students:', coursesWithStudents())
print('Students with courses:', studentsWithCourses())
print('Teachers with subjects:', teachersWithSubjects())
print('Subjects with teachers:', subjectsWithTeachers())
print('Student courses (Student ID 2):', studentCourses())
print('Course students (Course ID 3):', courseStudents())
print('Subject teachers (Subject ID 2):', subjectTeachers())
print('Teacher subjects (Teacher ID 3):', teacherSubjects())
