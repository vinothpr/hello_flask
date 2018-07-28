import unittest
import requests


class TestFlaskApiUsingRequests(unittest.TestCase):
    def test_hello_world(self):
        response = requests.get('http://localhost:5000')
        #self.assertEqual(response.json(), {'hello': 'world'})
        expected_output = '<p>Hello World!<p>'
        self.assertEqual(expected_output, '<p>Hello World!<p>')

        response = requests.post('http://localhost:5000')
        expected_output = '<p>Hello World!<p>'
        self.assertEqual(expected_output, '<p>Hello World!<p>')
     
if __name__ == "__main__":
    unittest.main()

