import unittest
from api import app
from app_flask import db


class TestApi(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()
        db.create_all()

    @classmethod
    def tearDownClass(cls):
        db.drop_all()

    def test_01_groups_post_status(self):
        """Test that the api server is running and reachable
         when we pass in POST correct params"""
        params = {'name': 'AA-11'}
        response = self.app.post('/api/v1/groups', data=params)
        self.assertEqual(response.status_code, 201)

    def test_02_groups_post_status(self):
        """Test that the api server isn't running and reachable
         when we pass nothing in POST"""
        response = self.app.post('/api/v1/groups')
        self.assertEqual(response.status_code, 404)

    def test_03_students_post_status(self):
        """Test that the api server is running and reachable
         when we pass in POST correct params"""
        params = {'first_name': 'Harry', 'last_name': 'Potter', 'group_id': 1}
        response = self.app.post('/api/v1/students', data=params)
        self.assertEqual(response.status_code, 201)

    def test_04_students_post_status(self):
        """Test that the api server isn't running and reachable
         when we pass nothing in POST"""
        response = self.app.post('/api/v1/students')
        self.assertEqual(response.status_code, 404)

    def test_05_students_post_status(self):
        """Test that the api server isn't running and reachable
         when we pass wrong params in POST"""
        params = {'first_name': 'Drako', 'group_id': 1}
        response = self.app.post('/api/v1/students', data=params)
        self.assertEqual(response.status_code, 404)

    def test_06_courses_post_status(self):
        """Test that the api server is running and reachable
         when we pass in POST correct params"""
        params = {'name': 'History of Magic',
                  'description': 'A History of Magic by Bathilda Bagshot'}
        response = self.app.post('/api/v1/courses', data=params)
        self.assertEqual(response.status_code, 201)

    def test_07_courses_post_status(self):
        """Test that the api server isn't running and reachable
         when we pass nothing in POST"""
        response = self.app.post('/api/v1/courses')
        self.assertEqual(response.status_code, 404)

    def test_08_students_get_status(self):
        """Test that the api server is running and reachable"""
        response = self.app.get('/api/v1/students')
        self.assertEqual(response.status_code, 200)

    def test_09_student_get_status(self):
        """Test that the api server is running and reachable"""
        response = self.app.get('/api/v1/students/1')
        self.assertEqual(response.status_code, 200)

    def test_10_students_get_with_params_status(self):
        """Test that the api server is running and reachable
         when we pass param(format and order)"""
        response = self.app.get('/api/v1/students?format=xml&order=desc')
        self.assertEqual(response.status_code, 200)

    def test_11_student_get_with_wrong_id_status(self):
        """Test that the api server isn't running and reachable when we pass wrong id"""
        response = self.app.get('/api/v1/students/10000000')
        self.assertEqual(response.status_code, 404)

    def test_12_students_content_xml(self):
        """The content type test when format=xml"""
        response = self.app.get('/api/v1/students?format=xml')
        self.assertEqual(response.content_type, "text/xml")

    def test_13_students_content_json(self):
        """The content type test when format=json"""
        response = self.app.get('/api/v1/students?format=json')
        self.assertEqual(response.content_type, "application/json")

    def test_14_student_content_json(self):
        """The content type test when format=json"""
        response = self.app.get('/api/v1/students/1?format=json')
        self.assertEqual(response.content_type, "application/json")

    def test_15_groups_get_status(self):
        """Test that the api server is running and reachable"""
        response = self.app.get('/api/v1/groups')
        self.assertEqual(response.status_code, 200)

    def test_16_group_get_status(self):
        """Test that the api server is running and reachable"""
        response = self.app.get('/api/v1/groups/1')
        self.assertEqual(response.status_code, 200)

    def test_17_groups_get_with_params_status(self):
        """Test that the api server is running and reachable
         when we pass param(format and order)"""
        response = self.app.get('/api/v1/groups?format=xml&order=desc')
        self.assertEqual(response.status_code, 200)

    def test_18_group_get_with_wrong_id_status(self):
        """Test that the api server isn't running and reachable when we pass wrong id"""
        response = self.app.get('/api/v1/groups/10000000')
        self.assertEqual(response.status_code, 404)

    def test_19_groups_content_xml(self):
        """The content type test when format=xml"""
        response = self.app.get('/api/v1/groups?format=xml')
        self.assertEqual(response.content_type, "text/xml")

    def test_20_groups_content_json(self):
        """The content type test when format=xml"""
        response = self.app.get('/api/v1/groups?format=json')
        self.assertEqual(response.content_type, "application/json")

    def test_21_group_content_json(self):
        """The content type test when format=json"""
        response = self.app.get('/api/v1/groups/1?format=json')
        self.assertEqual(response.content_type, "application/json")

    def test_22_courses_get_status(self):
        """Test that the api server is running and reachable"""
        response = self.app.get('/api/v1/courses')
        self.assertEqual(response.status_code, 200)

    def test_23_course_get_status(self):
        """Test that the api server is running and reachable"""
        response = self.app.get('/api/v1/courses/1')
        self.assertEqual(response.status_code, 200)

    def test_24_courses_get_with_params_status(self):
        """Test that the api server is running and reachable
         when we pass param(format and order)"""
        response = self.app.get('/api/v1/courses?format=xml&order=desc')
        self.assertEqual(response.status_code, 200)

    def test_25_course_get_with_wrong_id_status(self):
        """Test that the api server isn't running and reachable when we pass wrong id"""
        response = self.app.get('/api/v1/groups/10000000')
        self.assertEqual(response.status_code, 404)

    def test_26_courses_content_xml(self):
        """The content type test when format=xml"""
        response = self.app.get('/api/v1/courses?format=xml')
        self.assertEqual(response.content_type, "text/xml")

    def test_27_courses_content_json(self):
        """The content type test when format=xml"""
        response = self.app.get('/api/v1/courses?format=json')
        self.assertEqual(response.content_type, "application/json")

    def test_28_course_content_json(self):
        """The content type test when format=json"""
        response = self.app.get('/api/v1/courses/1?format=json')
        self.assertEqual(response.content_type, "application/json")

    def test_29_students_update_group_status(self):
        """Test that the api server isn't running and reachable
         when we pass nothing in PUT"""
        response = self.app.put('/api/v1/students/1')
        self.assertEqual(response.status_code, 404)

    def test_30_students_update_group_status(self):
        """Test that the api server is running and reachable
         when we pass in PUT correct params"""
        params = {'group_id': 1}
        response = self.app.put('/api/v1/students/1', data=params)
        self.assertEqual(response.status_code, 201)

    def test_31_group_update_name_status(self):
        """Test that the api server isn't running and reachable
         when we pass nothing in PUT"""
        response = self.app.put('/api/v1/groups/1')
        self.assertEqual(response.status_code, 404)

    def test_32_group_update_name_status(self):
        """Test that the api server is running and reachable
         when we pass in PUT correct params"""
        params = {'name': "BB-22"}
        response = self.app.put('/api/v1/groups/1', data=params)
        self.assertEqual(response.status_code, 200)

    def test_33_course_update_status(self):
        """Test that the api server isn't running and reachable
         when we pass nothing in PUT"""
        response = self.app.put('/api/v1/courses/1')
        self.assertEqual(response.status_code, 404)

    def test_34_course_update_name_status(self):
        """Test that the api server is running and reachable
         when we pass in PUT correct params"""
        params = {'description': "some description"}
        response = self.app.put('/api/v1/courses/1', data=params)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
