import unittest #  import the Unittest module
from models import newssource # import the newssource module
Newssource = newssource.Newssource # get the Newssource class which we will create.

class NewssourceTest(unittest.TestCase): #  create a test class

    def setUp(self): #define a setUp() method.This will instantiate our Newsource class to make the self.new_newssource object.
        self.new_newssource = Newssource(1234,'Python News','A thrilling new Python news website','https://image.tmdb.org/t/p/w500/khsjha27hbs',8.5,129993)

    def test_instance(self): #define a test case test_instance 
        self.assertTrue(isinstance(self.new_newssource,Newssource)) #function test_instance uses the isinstance() function that checks if the object self.new_newssource is an instance of the Newssource class.


if __name__ == '__main__':
    unittest.main()