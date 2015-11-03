import unittest

from fib import app

class TestRoot(unittest.TestCase):
    def setUp(self):
        self.test_fib = app.test_client()
    
    def test_root_status(self):
        resp = self.test_fib.get('/')
        self.assertEquals(resp.status, "200 OK")
    def test_root_data(self):
        resp = self.test_fib.get('/')
        self.assertEquals(resp.data, "Give us a number")
    def test_fib_good_status(self):
        resp = self.test_fib.get('/5')
        self.assertEquals(resp.status, "200 OK")
    def test_fib_good_data(self):
        resp = self.test_fib.get('/5')
        self.assertEquals(resp.data, "0 1 1 2 3")
    def test_fib_specal_cases(self):
        resp = self.test_fib.get('/0')
        self.assertEquals(resp.data, "fail")
        resp = self.test_fib.get('/1')
        self.assertEquals(resp.data, "0")
        resp = self.test_fib.get('/2')
        self.assertEquals(resp.data, "0 1")
    def test_fib_bad_status(self):
        resp = self.test_fib.get('/-5')
        self.assertEquals(resp.status, "404 NOT FOUND")



