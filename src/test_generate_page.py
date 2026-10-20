import unittest

from generate_page import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_header(self):
        md = "# title"
        title = extract_title(md)

        self.assertEqual(
            title,
            "title"
        )
    
    def test_strip_header(self):
        md = "# title     "
        title = extract_title(md)

        self.assertEqual(
            title,
            "title"
        )

    def test_header_exception(self):
        md = "## title"
        
        with self.assertRaises(ValueError):
            extract_title(md)
    
    def test_non_header_exception(self):
        md = "some random text"

        with self.assertRaises(ValueError):
            extract_title(md)