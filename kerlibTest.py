# run 'python -m unittest kerlibTest.py'
# 'python -m unittest -v kerlibTest.py' to produce more verbose output

import logging
import os
import unittest
from random import randint

import pep8
from PIL import Image

import kerlib


class KerlibTests(unittest.TestCase):

    def setUp(self):
        # define instructions that will be executed before each test method
        # we can do stuff like 'self.customvariable = <custom value>'
        self.image_path = "test_files/pablo.png"
        self.new_image_path = "test_files/pablo-out.png"


    #def tearDown(self):
        # define instructions that will be executed after each test method


    def test_add_text_to_image(self):
        random_number = randint(0,10000)
        text = "kerlib.add_text_to_image()\nThis is Random Text to test\nrandom number: " + str(random_number)
        logging.info("random number of '{0}' for picture".format(random_number))
        kerlib.add_text_to_image(self.image_path,
                                 text,
                                 new_image_path=self.new_image_path,
                                 image_font_size=35,
                                 font_color="white")
        with Image.open(self.new_image_path) as image:
            image.show()

        print('name of file ' + self.new_image_path)
        print('random number of image: ' + str(random_number))
        assert os.path.isfile(self.new_image_path)

    def test_create_image_with_text(self):
        kerlib.create_image_with_text()
        assert os.path.isfile("hello.png")
        os.remove("hello.png")
        assert not os.path.isfile("hello.png")


    def test_pep8(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide()
        result = pep8style.check_files(['kerlib/gmail.py', 'kerlib/image.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_send_email_single_to_cc_bcc(self):
         assert helper_send_email(["a.com"], ["b.com"], ["c.com"])

 
    def test_send_email_multiple_to_cc_bcc(self):
        assert helper_send_email(["a.com", "b.com", "c.com"], ["d.com", "e.com"],["f.com", "g.com"])


    def test_send_email_single_to(self):
        assert helper_send_email(["a.com"])


    def test_send_email_Empty_List_Throws_ValueError(self):
        # calling the method 'helper_send_email' and passing argument of empty list []
        with self.assertRaises(ValueError):
            helper_send_email([])
        #self.assertRaises(ValueError, helper_send_email, [])



    def test_send_email_Empty_List_Throws_TypeError(self):
        # calling the method 'test_send_email' and passing argument of "a.com"
        # should get a TypeError because it is expecting a list, not a string
        with self.assertRaises(TypeError):
            helper_send_email("a.com")
        #self.assertRaises(TypeError, helper_send_email, "a.com")


    def test_send_email_real(self):
        #kerlib.send_email("shane.kercheval@gmail.com", "nhgehhcyylagqktr", "test subject", "test email", ["shane_kercheval@hotmail.com"],["shane@intellitect.com"],["shane.kercheval@gmail.com"])
        #kerlib.send_email("shane.kercheval@gmail.com", "nhgehhcyylagqktr", "test subject", "this is a test email", ["shane.kercheval@gmail.com"])
        assert True
  

def helper_send_email(toList=list(), ccList=list(), bccList=list()):
    testResult = kerlib.send_email("username",
                                   "password",
                                   "subject",
                                   "emailText",
                                   toList,
                                   ccList,
                                   bccList,
                                   True)
    sendTo = list()
    sendTo.extend(toList)
    sendTo.extend(ccList)
    sendTo.extend(bccList)
    expectedResult = """from: username
subject: subject
to: {0}{1}{2}
mime-version: 1.0
content-type: text/html
emailText
{3}""".format(", ".join(toList), "\ncc: " if len(ccList) > 0 else "",", ".join(ccList), ", ".join(sendTo))

    return testResult == expectedResult

if __name__ == '__main__':
    unittest.main()
