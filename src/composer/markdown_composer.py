from src.extractor.readability_extractor import Document, ImageContent, TextContent


class MarkdownComposer:

    def compose(self, document: Document) -> str:
        output = ""

        for content_block in document.contents:
            if isinstance(content_block, TextContent):
                for paragraph in content_block.paragraphs:
                    output += f"<p>{str(paragraph)}</p>"

            if isinstance(content_block, ImageContent):
                output += f"<figure><p><img src={str(content_block.src)} alt={str(content_block.alt)}/></p></figure>"

        return output
