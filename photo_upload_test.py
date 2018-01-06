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
        # self.test_image =  open('test_files/test_image.jpg')


    def tearDown(self):
        app.testing = False

    def test_photo_upload(self):

        with open('test_files/test_image.jpg') as test:
            imgStringIO = StringIO.StringIO(test.read())

        upload = self.app.post('/upload', data = {'file': (imgStringIO, 'test.jpg')}, follow_redirects=True)
        assert upload.status == '200 OK'

if __name__ == '__main__':
    unittest.main()


    # size = (50,50)
    # color = (0, 0, 0)
    # image = Image.new("RGB", size, color)
    # print image
    # image_file = StringIO.StringIO(image.tobytes())
    # bp()
    # print image_file.name
