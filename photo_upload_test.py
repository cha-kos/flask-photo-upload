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
            test_image_stream = test.read()
            test_image_object = StringIO.StringIO(test_image_stream)

        upload = self.app.post('/upload', data = {'file': (test_image_object, 'test.jpg')}, follow_redirects=True)
        converted_test_image_stream = test_image_stream.encode('base64').replace('\n', '')
        assert converted_test_image_stream in upload.data

if __name__ == '__main__':
    unittest.main()
