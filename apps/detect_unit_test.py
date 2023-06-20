import os, cv2, unittest, detect

class TestImageDisplay(unittest.TestCase):
    def test_read_image(self):
        current_dir =  os.path.dirname(os.path.realpath(__file__))
        parent_directory = os.path.dirname(current_dir)
        img = cv2.imread(os.path.join(parent_directory, 'static', 'assets', 'agilim.png'))
        self.assertIsNotNone(img)
        expected_height = 515
        expected_width = 511
        actual_height, actual_width, _ = img.shape
        self.assertEqual(expected_height, actual_height)
        self.assertEqual(expected_width, actual_width)
    
    def test_path_image(self):
        current_dir = os.getcwd()
        #print("Current:", current_dir)
        dir_path = os.path.dirname(os.path.realpath(__file__))
        #print("Directory:", dir_path)
        parent_directory = os.path.dirname(dir_path)
        self.assertEqual(current_dir, parent_directory)

    def test_print_image(self):
        img = detect.ObjDetect('perfil.JPG')
        img.save_detect_picture()

if __name__ == '__main__':
    unittest.main()