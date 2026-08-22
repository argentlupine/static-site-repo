import src.htmlnode
import src.textnode
import src.node_processing

def main():
    print("Hello from static-site-repo!")
    print("Testing split nodes image")
    image_to_test = ['This is text and an ![image](fake_link_goes_here)']
    return split_nodes_image(image_to_test)


if __name__ == "__main__":
    main()
