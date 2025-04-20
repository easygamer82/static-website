from textnode import TextNode, TextType

def main():

    textnode = TextNode("Hello", TextType.BOLD_WRAP, "www.yooo.com")
    print(textnode)

if __name__ == "__main__":
    main()