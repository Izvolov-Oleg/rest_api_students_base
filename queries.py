from models import Group, Course, Student, db


def find_groups(n: int):
    """
    Find all groups with less or equals student count (n)
    """
    from sqlalchemy.sql.expression import func

    groups = Group.query.join(Student, Group.id == Student.group_id). \
        group_by(Group.id). \
        having(func.count(Student.group_id) < n).all()
    for group in groups:
        print(group.name)


def find_students(name_course: str):
    """
    Find all students related to the course with a given name.
    """
    course = Course.query.filter_by(name=name_course).first()
    for student in course.students:
        print(student.first_name, student.last_name)


def add_student(f_name, l_name, group_id=None):
    """
    Add new student
    """
    if group_id:
        new_student = Student(
            first_name=f_name,
            last_name=l_name,
            group_id=group_id)
    else:
        new_student = Student(first_name=f_name, last_name=l_name)
    db.session.add(new_student)
    db.session.commit()


def del_student(student_id):
    """
    Delete student by STUDENT_ID
    """
    student = Student.query.get(student_id)
    db.session.delete(student)
    db.session.commit()


def add_student_to_course(student_id, course_name):
    """
    Add a student to the course (from a list by id)
    """
    student = Student.query.filter_by(student_id=student_id).first()
    course = Course.query.filter_by(name=course_name).first()
    student.courses.append(course)
    db.session.add(student)
    db.session.commit()


def remove_student_from_course(student_id, course_name):
    """
    Remove the student from one of his or her courses
    """
    student = Student.query.filter_by(student_id=student_id).first()
    course = Course.query.filter_by(name=course_name).first()
    student.courses.remove(course)
    db.session.commit()
