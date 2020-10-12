import unittest
import sys
import os

sys.path.insert(0,'bin')

import file_reader as fr
import settings

class TestFileReader(unittest.TestCase):
    def setUp(self):
        self.path_file = os.path.join(settings.PATH_FILE, settings.FILE_NAME)

    def test_read_data(self):
        data = fr.get_data(self.path_file)
        print(len(data))
        print(type(data))
        self.assertEquals(len(data),5001)

        self.assertEquals(True,True)
    
if __name__ == "__main__":
    main()