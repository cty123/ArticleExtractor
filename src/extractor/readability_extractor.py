from readabilipy import simple_json_from_html_string
from bs4 import BeautifulSoup


class ImageContent:

    def __init__(self, src: str, alt: str) -> None:
        self.src = src
        self.alt = alt


class TextContent:

    def __init__(self, paragraphs: list[str]) -> None:
        self.paragraphs = paragraphs


class Document:

    def __init__(self, title: str, contents: list[ImageContent | TextContent]) -> None:
        self.title = title
        self.contents = contents


class ReadabilityExtractor:

    def __init__(self) -> None:
        pass

    def parse_document(self, raw_content: str) -> Document:
        article_json = simple_json_from_html_string(
            raw_content,
            use_readability=True,
            content_digests=False,
            node_indexes=False
        )

        title = article_json['title']
        content = article_json['content']
        contents = self.analyze_content(content)
        return Document(title=title, contents=contents)

    def analyze_content(self, content: str) -> list[ImageContent | TextContent]:
        soup = BeautifulSoup(content, 'html.parser')
        article_node = soup.find('article')

        if not article_node:
            return None

        contents = []
        for element in article_node.children:
            if element.name == 'figure':
                contents += self.handle_figure(element)
                continue

            if element.name == 'div':
                contents += self.handle_text(element)
                continue

        return contents

    def handle_figure(self, figure: any) -> list[ImageContent]:
        figure_div = figure.find('div', {'data-component': 'image-block'})
        if not figure_div:
            return None

        contents = []
        image_nodes = figure_div.find_all('img')
        for image_node in image_nodes:
            src = image_node.get('src')
            alt = image_node.get('alt')
            contents.append(ImageContent(src=src, alt=alt))

        return contents

    def handle_text(self, text: any) -> list[TextContent]:
        if text.has_attr('data-component') and text['data-component'] == 'text-block':
            paragraphs = []
            for child in text.children:
                if child.name == 'p':
                    paragraphs.append(child.text)

        return [TextContent(paragraphs=paragraphs)]
