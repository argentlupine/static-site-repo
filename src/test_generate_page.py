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
    
    def test_header_on_different_line(self):
        md = """
line 1

# real header line

line 2
"""
        title = extract_title(md)
        
        self.assertEqual(
            title,
            "real header line"
        )
    
    def test_two_headers(self):
        md = """
# header 1

# header 2
"""
        title = extract_title(md)

        self.assertEqual(
            title,
            "header 1"
        )
    
    def test_empty_string(self):
        md = ""
        
        with self.assertRaises(ValueError):
            extract_title(md)
    
    def test_hastag_no_space(self):
        md = "#title"
        
        with self.assertRaises(ValueError):
            extract_title(md)
