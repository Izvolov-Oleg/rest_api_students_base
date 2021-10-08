from app_flask import db

students_courses = db.Table('students_courses',
                            db.Column('student_id', db.Integer, db.ForeignKey('student.id')),
                            db.Column('course_id', db.Integer, db.ForeignKey('course.id')))


class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)

    students = db.relationship('Student', backref=db.backref('group', lazy=True))

    def __repr__(self):
        return f"<group {self.name}>"

    def to_dict(self):
        return {'id': self.id, 'name': self.name,
                'students': [f'{student.first_name} {student.last_name}'
                             for student in self.students]}


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'))
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))

    courses = db.relationship('Course', secondary=students_courses,
                              backref=db.backref('students', lazy='dynamic')
                              )

    def __repr__(self):
        return f"<student {self.first_name} {self.last_name}>"

    def to_dict(self):
        return {'id': self.id, 'group id': self.group_id,
                'first name': self.first_name, 'last name': self.last_name,
                'courses': [course.name for course in self.courses]}


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    description = db.Column(db.String(500))

    def __repr__(self):
        return f"<course {self.name}>"

    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'description': self.description,
                'students': [f'ID={student.id}, {student.first_name} {student.last_name}'
                             for student in self.students]}


if __name__ == "__main__":
    db.create_all()
