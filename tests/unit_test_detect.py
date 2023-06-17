import os, cv2, unittest

class TestImageDisplay(unittest.TestCase):
    def test_read_image(self):
        current_dir = os.getcwd()
        #parent_directory = os.path.dirname(current_dir)
        img = cv2.imread(os.path.join(current_dir, 'static', 'assets', 'agilim.png'))
        self.assertIsNotNone(img)
        expected_height = 515
        expected_width = 511
        actual_height, actual_width, _ = img.shape
        self.assertEqual(expected_height, actual_height)
        self.assertEqual(expected_width, actual_width)

if __name__ == '__main__':
    unittest.main()