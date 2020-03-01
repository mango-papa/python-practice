import unittest


class TestSomeModule(unittest.TestCase):
    def test_f1(self):
        print('test start')
        pass


test = TestSomeModule()
test.test_f1()
