import unittest

if __name__ == "__main__":
    all_tests = unittest.TestLoader().discover('./', pattern='*_test.py')
    unittest.TextTestRunner().run(all_tests)
