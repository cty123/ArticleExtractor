import requests

from client.translator_client import TranslatorClient
from extractor.readability_extractor import Document, ReadabilityExtractor, TextContent


class Processor:

    def __init__(self) -> None:
        self.extractor = ReadabilityExtractor()
        self.translator = TranslatorClient()

    def process(self, url: str) -> Document:
        raw_html = self.download_html_content(url=url)
        document = self.extractor.parse_document(raw_content=raw_html)
        translated_title = self.translator.translate_text(document.title)
        translated_contents = []
        for content_block in document.contents:
            if isinstance(content_block, TextContent):
                translated_paragraphs = [self.translator.translate_text(
                    paragraph) for paragraph in content_block.paragraphs]
                translated_contents.append(TextContent(
                    paragraphs=translated_paragraphs))
            else:
                translated_contents.append(content_block)

        return Document(title=translated_title, contents=translated_contents)

    def download_html_content(self, url: str) -> str | None:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' +
            'Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            return None

        return response.content
