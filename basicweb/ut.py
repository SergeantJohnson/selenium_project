import unittest
import HtmlTestRunner

from Demoeg import Sample

class Mytest(unittest.TestCase):

    def setUp(self):
        print("setup")

    def tearDown(self):
        print("teardown")

    def test_add1(self):
        self.assertTrue(8 == Sample.add1(self, 3, 5))

    def test_sub1(self):
        self.assertTrue(2 == Sample.sub1(self, 5, 3))


if __name__ == "__main__":
    print("here")
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=r'C:\Users\charu\workspace_python\selenium_project\reports'))