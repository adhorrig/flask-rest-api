from app import app
import unittest
import json
import requests

class TestAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass

    #Test the status code from getting all cars.
    def test_status_code(self):
        result = self.app.get('/cars')
        self.assertEqual(result.status_code, 200)

    #Test that the correct car is returned when passing an ID
    def test_response(self):
        result = self.app.get('cars/1')
        data = json.loads(result.get_data(as_text=True))
        self.assertEqual(data['id'], 1)
        self.assertEqual(data['make'], 'Nissan')
        self.assertEqual(data['model'], 'Mac 4')
        self.assertEqual(data['price'], 600)
        self.assertEqual(data['year'], 2016)

    #Test the ability to create a car
    def test_create(self):
        response = self.app.post('/car', 
                                data=json.dumps(dict(make='Ford', model='Focus', year = 2011, chasis_id='XYZ123', price = 1000.00)),
                                content_type='application/json')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
