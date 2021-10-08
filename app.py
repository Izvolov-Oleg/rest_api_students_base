import random
from models import Group, Student, Course, db


def generate_test_data():
    """
    This function create test data for db
    """
    # create 10 groups (for example - "AA-11"), use random
    groups = []
    for i in range(10):
        group_name = "".join([random.choice('ABCDEFGH'), random.choice(
            'ABCDEFGH'), '-', str(random.randint(0, 9)), str(random.randint(0, 9))])
        group = Group(name=group_name)
        db.session.add(group)
        db.session.flush()
        groups.append(group)
    # create 10 courses
    course_names = [
        'Biology',
        'Math',
        'English',
        'Physics',
        'History',
        'Astronomy',
        'Chemistry',
        'Physical education',
        'Computer science',
        'Economics']
    courses = []
    for name in course_names:
        course = Course(
            name=name,
            description=f'A little description of {name}')
        db.session.add(course)
        db.session.flush()
        courses.append(course)

    # create students (200 students)
    first_names = ['Kirk', 'Leon', 'Brittany', 'Dorothy', 'David', 'William',
                   'Brittany', 'Vicki', 'Don', 'Jeremy', 'Jason', 'Kenneth',
                   'Diane', 'Susan', 'Carla', 'Monica', 'Raymond', 'Eugene',
                   'Craig', 'Susan']

    last_names = [
        'Brown',
        'Nunez',
        'Curtis',
        'Jones',
        'Smith',
        'Gonzalez',
        'Johnson',
        'Anderson',
        'Robinson',
        'Brock',
        'Howard',
        'Stanley',
        'Hughes',
        'Brown',
        'Young',
        'Nichols',
        'Collins',
        'Henderson',
        'Lori',
        'Sanders']

    students = []
    while len(students) < 200:
        student = "".join([random.choice(first_names),
                           ' ', random.choice(last_names)])
        if student not in students:
            students.append(student)

    # assign students to group (randomly)
    for group in groups:
        if len(students) < 10:
            break
        amount = random.randint(10, 30)
        if len(students) < amount:
            break
        for i in range(amount):
            student = students.pop()
            f_name, l_name = student.split()
            s = Student(
                first_name=f_name,
                last_name=l_name,
                group_id=group.id)
            crs = random.sample(courses, random.randint(1, 3))
            s.courses.extend(crs)
            db.session.add(s)
            db.session.flush()
    else:
        for student in students:
            f_name, l_name = student.split()
            s = Student(first_name=f_name, last_name=l_name)
            db.session.add(s)
            db.session.flush()

    db.session.commit()


if __name__ == "__main__":
    generate_test_data()
