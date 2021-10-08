from app_flask import app, db
from flask_restful import Resource, Api, abort, reqparse
from models import Student, Course, Group
from flask import request, Response
from dicttoxml import dicttoxml

api = Api(app)


def abort_if_id_doesnt_exist(obj_id, obj):
    result = obj.query.get(obj_id)
    if result is None:
        abort(404, message="Id is not correct, please try again")


class StudentsAll(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('first_name', type=str)
        self.parser.add_argument('last_name', type=str)
        self.parser.add_argument('group_id', type=int, default=None)
        super(StudentsAll, self).__init__()

    def get(self):
        students = Student.query
        format_api = request.args.get('format')
        order = request.args.get('order')
        if order == 'desc':
            students = students.order_by(Student.id.desc())
        students_list = [student.to_dict() for student in students.all()]
        if format_api == 'xml':
            result = dicttoxml(students_list)
            return Response(result, content_type='text/xml')
        else:
            return students_list

    def post(self):
        args = self.parser.parse_args()
        if not args['first_name'] or not args['last_name']:
            abort(404, message="Id is not correct, please try again")
        if args['group_id']:
            new_student = Student(first_name=args['first_name'],
                                  last_name=args['last_name'],
                                  group_id=args['group_id'])
        else:
            new_student = Student(first_name=args['first_name'],
                                  last_name=args['last_name'],)
        db.session.add(new_student)
        db.session.commit()
        return new_student.to_dict(), 201


class Students(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('group_id', type=int, default=None)
        super(Students, self).__init__()

    def get(self, student_id):
        abort_if_id_doesnt_exist(student_id, Student)
        student = Student.query.get(student_id)
        format_api = request.args.get('format')
        if format_api == 'xml':
            xml_result = dicttoxml(student.to_dict())
            return Response(xml_result, content_type='text/xml')
        return student.to_dict()

    def put(self, student_id):
        abort_if_id_doesnt_exist(student_id, Student)
        args = self.parser.parse_args()
        if args['group_id']:
            update_student = Student.query.get(student_id)
            abort_if_id_doesnt_exist(args['group_id'], Group)
            update_student.group_id = args['group_id']
            db.session.commit()
            return update_student.to_dict(), 201
        abort(404, message="Group_id is not correct, please try again")

    def delete(self, student_id):
        abort_if_id_doesnt_exist(student_id, Student)
        student = Student.query.get(student_id)
        db.session.delete(student)
        db.session.commit()
        return '', 204


class GroupsAll(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name', type=str)
        super(GroupsAll, self).__init__()

    def get(self):
        groups = Group.query
        format_api = request.args.get('format')
        order = request.args.get('order')
        if order == 'desc':
            groups = groups.order_by(Group.id.desc())
        groups_list = [group.to_dict() for group in groups.all()]
        if format_api == 'xml':
            result = dicttoxml(groups_list)
            return Response(result, content_type='text/xml')
        else:
            return groups_list

    def post(self):
        args = self.parser.parse_args()
        if args['name']:
            new_group = Group(name=args['name'])
            db.session.add(new_group)
            db.session.commit()
            return new_group.to_dict(), 201
        abort(404, message="Group name is not correct, please try again")

class Groups(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name', type=str)
        super(Groups, self).__init__()

    def get(self, group_id):
        abort_if_id_doesnt_exist(group_id, Group)
        format_api = request.args.get('format')
        group = Group.query.get(group_id)
        if format_api == 'xml':
            xml_result = dicttoxml(group.to_dict())
            return Response(xml_result, content_type='text/xml')
        return group.to_dict()

    def put(self, group_id):
        abort_if_id_doesnt_exist(group_id, Group)
        args = self.parser.parse_args()
        if args['name']:
            update_group = Group.query.get(group_id)
            update_group.name = args['name']
            db.session.commit()
            return update_group.to_dict()
        abort(404, message="Group name is not correct, please try again")

    def delete(self, group_id):
        abort_if_id_doesnt_exist(group_id, Group)
        group = Group.query.get(group_id)
        db.session.delete(group)
        db.session.commit()
        return '', 204


class CoursesAll(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name', type=str)
        self.parser.add_argument('description', type=str)
        super(CoursesAll, self).__init__()

    def get(self):
        courses = Course.query
        format_api = request.args.get('format')
        order = request.args.get('order')
        if order == 'desc':
            courses = courses.order_by(Course.id.desc())
        courses_list = [course.to_dict() for course in courses.all()]
        if format_api == 'xml':
            result = dicttoxml(courses_list)
            return Response(result, content_type='text/xml')
        else:
            return courses_list

    def post(self):
        args = self.parser.parse_args()
        if args['name']:
            new_course = Course(name=args['name'], description=args['description'])
            db.session.add(new_course)
            db.session.commit()
            return new_course.to_dict(), 201
        abort(404, message="Course name is not correct, please try again")

class Courses(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('description', type=str)
        super(Courses, self).__init__()

    def get(self, course_id):
        abort_if_id_doesnt_exist(course_id, Course)
        format_api = request.args.get('format')
        course = Course.query.get(course_id)
        if format_api == 'xml':
            xml_result = dicttoxml(course.to_dict())
            return Response(xml_result, content_type='text/xml')
        return course.to_dict()

    def put(self, course_id):
        abort_if_id_doesnt_exist(course_id, Course)
        args = self.parser.parse_args()
        if args['description']:
            update_course = Group.query.get(course_id)
            update_course.name = args['description']
            db.session.commit()
            return update_course.to_dict()
        abort(404, message="Course description is not correct, please try again")

    def delete(self, course_id):
        abort_if_id_doesnt_exist(course_id, Course)
        course = Course.query.get(course_id)
        db.session.delete(course)
        db.session.commit()
        return '', 204


api.add_resource(StudentsAll, '/api/v1/students', endpoint='students')
api.add_resource(Students, '/api/v1/students/<int:student_id>', endpoint='user')
api.add_resource(GroupsAll, '/api/v1/groups', endpoint='groups')
api.add_resource(Groups, '/api/v1/groups/<int:group_id>', endpoint='group')
api.add_resource(CoursesAll, '/api/v1/courses', endpoint='courses')
api.add_resource(Courses, '/api/v1/courses/<int:course_id>', endpoint='course')

if __name__ == '__main__':
    app.run(debug=True)
