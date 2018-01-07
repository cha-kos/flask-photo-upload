import os
import app
import unittest
import StringIO
from pdb import set_trace as bp

class UploadTestCase(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.app.test_client()


    def tearDown(self):
        app.testing = False

    def test_photo_upload(self):

        with open('test_files/test_image.jpg') as test:
            # create file like object with test_image_stream
            test_image_stream = test.read()
            test_image_object = StringIO.StringIO(test_image_stream)

        upload = self.app.post('/upload', data = {'file': (test_image_object, 'test_image.jpg')}, follow_redirects=True)

        # convert image stream locally and assert it is in the response body of the upload
        converted_test_image_stream = test_image_stream.encode('base64').replace('\n', '')
        assert converted_test_image_stream in upload.data

if __name__ == '__main__':
    unittest.main()
