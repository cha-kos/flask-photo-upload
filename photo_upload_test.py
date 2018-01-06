import os
import app
import unittest
import tempfile
import StringIO
from PIL import Image
from pdb import set_trace as bp

class UploadTestCase(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.app.test_client()


    def tearDown(self):
        app.testing = False

    def test_photo_upload(self):

        with open('test_files/test_image.jpg') as test:
            test_image = StringIO.StringIO(test.read())
            test.close()

        upload = self.app.post('/upload', data = {'file': (test_image, 'test.jpg')}, follow_redirects=True)
        converted_test_image = test_image.encode('base64').replace('\n', '')
        assert converted_test_image in upload.data

if __name__ == '__main__':
    unittest.main()
