import unittest
from textnode import TextNode, TextType
from node_processing import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link, text_to_textnodes

class TestNodeProcessing(unittest.TestCase):
    def test_no_nodes_in_list(self):
        with self.assertRaises(ValueError):
            split_nodes_delimiter(None, None, None)
    
    def test_node_not_text_type(self):
        test_node = [TextNode("`code node`", TextType.CODE)]
        self.assertEqual(
            split_nodes_delimiter(test_node, "`", TextType.CODE),
            test_node
        )

    def test_node_odd_number_delimiters(self):
        test_node = TextNode(
            "unfinished **bold word",
            TextType.TEXT
        )
        with self.assertRaises(ValueError):
            split_nodes_delimiter(
                [test_node],
                "**",
                TextType.BOLD
            )
    
    def test_bold_node(self):
        test_node = TextNode(
            "finished **bold** word",
            TextType.TEXT
        )
        converted_node = split_nodes_delimiter(
            [test_node],
            "**",
            TextType.BOLD
        )
        self.assertEqual(
            converted_node,
            [
                TextNode("finished ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" word", TextType.TEXT)
            ]
        )
    
    def test_multiple_nodes(self):
        node1 = TextNode(
            "this is a **bold** word",
            TextType.TEXT
        )
        node2 = TextNode(
            "this is **not an italic** word",
            TextType.TEXT
        )
        converted_nodes = split_nodes_delimiter(
            [node1, node2],
            "**",
            TextType.BOLD
        )
        self.assertEqual(
            converted_nodes,
            [
                TextNode("this is a ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
                TextNode("this is ", TextType.TEXT),
                TextNode("not an italic", TextType.BOLD),
                TextNode(" word", TextType.TEXT)
            ]
        )
    
    def test_multiple_texttype(self):
        node = TextNode(
            "this **is bold** and this **is bold too** okay",
            TextType.TEXT
        )
        self.assertEqual(
            split_nodes_delimiter(
                [node],
                "**",
                TextType.BOLD
            ),
            [
                TextNode("this ", TextType.TEXT),
                TextNode("is bold", TextType.BOLD),
                TextNode(" and this ", TextType.TEXT),
                TextNode("is bold too", TextType.BOLD),
                TextNode(" okay", TextType.TEXT),
            ]
        )

    def test_no_delimeters(self):
        node = TextNode(
            "This is not the delimeter you are looking for",
            TextType.TEXT
        )
        self.assertEqual(
            split_nodes_delimiter(
                [node],
                "**",
                TextType.BOLD
            ),
            [
                TextNode("This is not the delimeter you are looking for", TextType.TEXT)
            ]
        )

    def test_delimiter_at_boundary(self):
        node = TextNode(
            "**bold** at the start, chill at the **end**",
            TextType.TEXT
        )
        self.assertEqual(
            split_nodes_delimiter(
                [node],
                "**",
                TextType.BOLD
            ),
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" at the start, chill at the ", TextType.TEXT),
                TextNode("end", TextType.BOLD)
            ]
        )

    def test_mixed_type_input(self):
        node = TextNode(
            "**bold** but want `code` instead **yo**",
            TextType.TEXT
        )
        self.assertEqual(
            split_nodes_delimiter(
                [node],
                "`",
                TextType.CODE
            ),
            [
                TextNode("**bold** but want ", TextType.TEXT),
                TextNode("code", TextType.CODE),
                TextNode(" instead **yo**", TextType.TEXT)
            ]
        )
    
    # Now testing extract markdown images

    def test_extract_markdown_images_1(self):
        matches = extract_markdown_images(
            "This is text and an ![image](fake_link_goes_here)"
        )
        self.assertEqual(
            [("image", "fake_link_goes_here")],
            matches
        )

    def test_extract_markdown_images_2(self):
        matches = extract_markdown_images(
            "Text here and a [bad](output)"
        )
        self.assertEqual(
            [],
            matches
        )

    # Now testing extract markdown links

    def test_extract_markdown_links_1(self):
        matches = extract_markdown_links(
            "Text, followed by a [link](goes here!!)"
        )
        self.assertEqual(
            [("link", "goes here!!")],
            matches
        )
    
    def test_extract_markdown_links_2(self):
        matches = extract_markdown_links(
            "Text, followed by an ![image](is linked here)"
        )
        self.assertEqual(
            [],
            matches
        )
    
    # Hard tests: split nodes to extract images!!!
    # 1. Check it works with one image
    def test_split_nodes_image_01(self):
        split_image = split_nodes_image(
            [
                TextNode('This is text and an ![image](fake_link_goes_here)', TextType.TEXT)
            ]
        )
        self.assertEqual(
            [
                TextNode('This is text and an ', TextType.TEXT),
                TextNode('image', TextType.IMAGE, 'fake_link_goes_here')
            ],
            split_image
        )
    
    # 2. Check it works with two images
    def test_split_nodes_image_02(self):
        split_image = split_nodes_image(
            [
                TextNode('This is text and an ![image](fake_link_goes_here)', TextType.TEXT),
                TextNode('This is text2 and an ![image2](fake2_link2_goes2_here)', TextType.TEXT)
            ]
        )
        self.assertEqual(
            [
                TextNode('This is text and an ', TextType.TEXT),
                TextNode('image', TextType.IMAGE, 'fake_link_goes_here'),
                TextNode('This is text2 and an ', TextType.TEXT),
                TextNode('image2', TextType.IMAGE, 'fake2_link2_goes2_here')
            ],
            split_image
        )
    
    # 3. Check it works with an image and trailing text
    def test_split_nodes_image_03(self):
        split_image = split_nodes_image(
            [
                TextNode('This is text and an ![image](fake_link_goes_here) followed by some additional text', TextType.TEXT)
            ]
        )
        self.assertEqual(
            [
                TextNode('This is text and an ', TextType.TEXT),
                TextNode('image', TextType.IMAGE, 'fake_link_goes_here'),
                TextNode(' followed by some additional text', TextType.TEXT)
            ],
            split_image
        )
    
    # 4. Check it works with two images
    def test_split_nodes_image_04(self):
        split_image = split_nodes_image(
            [
                TextNode("This is text with a link ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)", TextType.TEXT)
            ]
        )
        self.assertEqual(
            [
                TextNode('This is text with a link ', TextType.TEXT),
                TextNode('to boot dev', TextType.IMAGE, 'https://www.boot.dev'),
                TextNode(' and ', TextType.TEXT),
                TextNode('to youtube', TextType.IMAGE, 'https://www.youtube.com/@bootdotdev')
            ],
            split_image
        )
    
    # 5. Check it works with the same image twice
    def test_split_nodes_image_05(self):
        split_image = split_nodes_image(
            [
                TextNode("This is text with a link ![to boot dev](https://www.boot.dev) and ![to boot dev](https://www.boot.dev)", TextType.TEXT)
            ]
        )
        self.assertEqual(
            [
                TextNode('This is text with a link ', TextType.TEXT),
                TextNode('to boot dev', TextType.IMAGE, 'https://www.boot.dev'),
                TextNode(' and ', TextType.TEXT),
                TextNode('to boot dev', TextType.IMAGE, 'https://www.boot.dev')
            ],
            split_image
        )
    
    # 6. Check it doesn't pick up a link
    def test_split_nodes_image_06(self):
        split_image = split_nodes_image(
            [
                TextNode("This is text with a link ![to boot dev](https://www.boot.dev) and [to boot dev](https://www.boot.dev)", TextType.TEXT)
            ]
        )
        self.assertEqual(
            [
                TextNode('This is text with a link ', TextType.TEXT),
                TextNode('to boot dev', TextType.IMAGE, 'https://www.boot.dev'),
                TextNode(' and [to boot dev](https://www.boot.dev)', TextType.TEXT)
            ],
            split_image
        )
    
    # 7. Check it handles text with nothing
    def test_split_nodes_image_07(self):
        split_image = split_nodes_image(
            [
                TextNode("This is text with a link [to boot dev](https://www.boot.dev)", TextType.TEXT)
            ]
        )
        self.assertEqual(
            [
                TextNode('This is text with a link [to boot dev](https://www.boot.dev)', TextType.TEXT)
            ],
            split_image
        )
    
    # 8. Check it handles nothing
    def test_split_nodes_image_08(self):
        split_image = split_nodes_image(
            [
                
            ]
        )
        self.assertEqual(
            [
                
            ],
            split_image
        )

    # 9. Checking it handles a node that isn't text correctly
    def test_split_nodes_image_09(self):
        split_image = split_nodes_image(
            [
                TextNode('This is text and an ![image](fake_link_goes_here)', TextType.BOLD)
            ]
        )
        self.assertEqual(
            [
                TextNode('This is text and an ![image](fake_link_goes_here)', TextType.BOLD)
            ],
            split_image
        )
    
    # 10. Just an image, nothing else
    def test_split_nodes_image_10(self):
        split_image = split_nodes_image(
            [
                TextNode('![image](fake_link_goes_here)', TextType.TEXT)
            ]
        )
        self.assertEqual(
            [
                TextNode('image', TextType.IMAGE, 'fake_link_goes_here')
            ],
            split_image
        )
    
    # 11. Check two consecutive images
    def test_split_nodes_image_11(self):
        split_image = split_nodes_image(
            [
                TextNode('![image](fake_link_goes_here)![image2](fake2_link2_goes2_here)', TextType.TEXT)
            ]
        )
        self.assertEqual(
            [
                TextNode('image', TextType.IMAGE, 'fake_link_goes_here'),
                TextNode('image2', TextType.IMAGE, 'fake2_link2_goes2_here')
            ],
            split_image
        )
    
    # 12. Check an image then a link consecutively
    def test_split_nodes_image_12(self):
        split_image = split_nodes_image(
            [
                TextNode('![image](fake_link_goes_here)[image2](fake2_link2_goes2_here)', TextType.TEXT)
            ]
        )
        self.assertEqual(
            [
                TextNode('image', TextType.IMAGE, 'fake_link_goes_here'),
                TextNode('[image2](fake2_link2_goes2_here)', TextType.TEXT)
            ],
            split_image
        )

    
    # Now running effectively the same tests for the link!
    # 1. Check it works with one link
    def test_split_nodes_link_01(self):
        split_link = split_nodes_link(
            [
                TextNode('This is text and an [link](fake_link_goes_here)', TextType.TEXT)
            ]
        )
        self.assertEqual(
            [
                TextNode('This is text and an ', TextType.TEXT),
                TextNode('link', TextType.LINK, 'fake_link_goes_here')
            ],
            split_link
        )
    
    # 2. Check it works with two links
    def test_split_nodes_link_02(self):
        split_link = split_nodes_link(
            [
                TextNode('This is text and an [link](fake_link_goes_here)', TextType.TEXT),
                TextNode('This is text2 and an [link2](fake2_link2_goes2_here)', TextType.TEXT)
            ]
        )
        self.assertEqual(
            [
                TextNode('This is text and an ', TextType.TEXT),
                TextNode('link', TextType.LINK, 'fake_link_goes_here'),
                TextNode('This is text2 and an ', TextType.TEXT),
                TextNode('link2', TextType.LINK, 'fake2_link2_goes2_here')
            ],
            split_link
        )
    
    # 3. Check it works with a link and trailing text
    def test_split_nodes_link_03(self):
        split_link = split_nodes_link(
            [
                TextNode('This is text and an [link](fake_link_goes_here) followed by some additional text', TextType.TEXT)
            ]
        )
        self.assertEqual(
            [
                TextNode('This is text and an ', TextType.TEXT),
                TextNode('link', TextType.LINK, 'fake_link_goes_here'),
                TextNode(' followed by some additional text', TextType.TEXT)
            ],
            split_link
        )
    
    # 4. Check it works with two links
    def test_split_nodes_link_04(self):
        split_link = split_nodes_link(
            [
                TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.TEXT)
            ]
        )
        self.assertEqual(
            [
                TextNode('This is text with a link ', TextType.TEXT),
                TextNode('to boot dev', TextType.LINK, 'https://www.boot.dev'),
                TextNode(' and ', TextType.TEXT),
                TextNode('to youtube', TextType.LINK, 'https://www.youtube.com/@bootdotdev')
            ],
            split_link
        )
    
    # 5. Check it works with the same link twice
    def test_split_nodes_link_05(self):
        split_link = split_nodes_link(
            [
                TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to boot dev](https://www.boot.dev)", TextType.TEXT)
            ]
        )
        self.assertEqual(
            [
                TextNode('This is text with a link ', TextType.TEXT),
                TextNode('to boot dev', TextType.LINK, 'https://www.boot.dev'),
                TextNode(' and ', TextType.TEXT),
                TextNode('to boot dev', TextType.LINK, 'https://www.boot.dev')
            ],
            split_link
        )
    
    # 6. Check it doesn't pick up an image
    def test_split_nodes_link_06(self):
        split_link = split_nodes_link(
            [
                TextNode("This is text with a link [to boot dev](https://www.boot.dev) and ![to boot dev](https://www.boot.dev)", TextType.TEXT)
            ]
        )
        self.assertEqual(
            [
                TextNode('This is text with a link ', TextType.TEXT),
                TextNode('to boot dev', TextType.LINK, 'https://www.boot.dev'),
                TextNode(' and ![to boot dev](https://www.boot.dev)', TextType.TEXT)
            ],
            split_link
        )
    
    # 7. Check it handles text with nothing
    def test_split_nodes_link_07(self):
        split_link = split_nodes_link(
            [
                TextNode("This is text with a link ![to boot dev](https://www.boot.dev)", TextType.TEXT)
            ]
        )
        self.assertEqual(
            [
                TextNode('This is text with a link ![to boot dev](https://www.boot.dev)', TextType.TEXT)
            ],
            split_link
        )
    
    # 8. Check it handles nothing
    def test_split_nodes_link_08(self):
        split_link = split_nodes_link(
            [
                
            ]
        )
        self.assertEqual(
            [
                
            ],
            split_link
        )

    # 9. Checking it handles a node that isn't text correctly
    def test_split_nodes_link_09(self):
        split_link = split_nodes_link(
            [
                TextNode('This is text and an [link](fake_link_goes_here)', TextType.BOLD)
            ]
        )
        self.assertEqual(
            [
                TextNode('This is text and an [link](fake_link_goes_here)', TextType.BOLD)
            ],
            split_link
        )
    
    # 10. Just a link, nothing else
    def test_split_nodes_link_10(self):
        split_link = split_nodes_link(
            [
                TextNode('[link](fake_link_goes_here)', TextType.TEXT)
            ]
        )
        self.assertEqual(
            [
                TextNode('link', TextType.LINK, 'fake_link_goes_here')
            ],
            split_link
        )
    
    # 11. Check two consecutive links
    def test_split_nodes_link_11(self):
        split_link = split_nodes_link(
            [
                TextNode('[link](fake_link_goes_here)[link2](fake2_link2_goes2_here)', TextType.TEXT)
            ]
        )
        self.assertEqual(
            [
                TextNode('link', TextType.LINK, 'fake_link_goes_here'),
                TextNode('link2', TextType.LINK, 'fake2_link2_goes2_here')
            ],
            split_link
        )
    
    # Lastly testing the text_to_text_node function
    def test_text_to_text_nodes_bold(self):
        nodes_created = text_to_textnodes(
            'This is **bold** text yo'
        )
        self.assertEqual(
            [
                TextNode('This is ', TextType.TEXT),
                TextNode('bold', TextType.BOLD),
                TextNode(' text yo', TextType.TEXT)
            ],
            nodes_created
        )

    def test_text_to_text_nodes_italic(self):
        nodes_created = text_to_textnodes(
            'This is _italic_ text yo'
        )
        self.assertEqual(
            [
                TextNode('This is ', TextType.TEXT),
                TextNode('italic', TextType.ITALIC),
                TextNode(' text yo', TextType.TEXT)
            ],
            nodes_created
        )

    def test_text_to_text_nodes_code(self):
        nodes_created = text_to_textnodes(
            'This is `code` text yo'
        )
        self.assertEqual(
            [
                TextNode('This is ', TextType.TEXT),
                TextNode('code', TextType.CODE),
                TextNode(' text yo', TextType.TEXT)
            ],
            nodes_created
        )

    def test_text_to_text_nodes_image(self):
        nodes_created = text_to_textnodes(
            'This is ![image](crazy link here) text yo'
        )
        self.assertEqual(
            [
                TextNode('This is ', TextType.TEXT),
                TextNode('image', TextType.IMAGE, 'crazy link here'),
                TextNode(' text yo', TextType.TEXT)
            ],
            nodes_created
        )

    def test_text_to_text_nodes_link(self):
        nodes_created = text_to_textnodes(
            'This is [link](crazy link here) text yo'
        )
        self.assertEqual(
            [
                TextNode('This is ', TextType.TEXT),
                TextNode('link', TextType.LINK, 'crazy link here'),
                TextNode(' text yo', TextType.TEXT)
            ],
            nodes_created
        )

    def test_text_to_text_nodes_all_types(self):
        nodes_created = text_to_textnodes(
            'This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)'
        )
        self.assertEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev")
            ],
            nodes_created
        )
    
    def test_text_to_text_nodes_all_types_except_text(self):
        nodes_created = text_to_textnodes(
            '**text**_italic_`code block`![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg)[link](https://boot.dev)'
        )
        self.assertEqual(
            [
                TextNode("text", TextType.BOLD),
                TextNode("italic", TextType.ITALIC),
                TextNode("code block", TextType.CODE),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode("link", TextType.LINK, "https://boot.dev")
            ],
            nodes_created
        )