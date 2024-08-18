from deep_translator import GoogleTranslator

MAX_CHUNK_SIZE = 4000


class TranslatorClient:

    def __init__(self, target_lang: str = "zh-CN") -> None:
        self.translator = GoogleTranslator(source='auto', target=target_lang)
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
        }

    def translate_text(self, text: str, max_chunk_size: int = MAX_CHUNK_SIZE) -> str:
        if len(text) <= max_chunk_size:
            return self.translator.translate(text)

        chunks = split_texts(text=text, max_chunk_size=max_chunk_size)
        translated_trunks = self.translator.translate_batch(batch=chunks)
        return "".join(translated_trunks)


def split_texts(text: str, max_chunk_size: int) -> list[str]:
    chunks = []

    while len(text) > max_chunk_size:
        end = max_chunk_size - 1
        while text[end] != ' ' and end >= 0:
            end -= 1

        if end == -1:
            raise "unable to split the text by spaces"

        chunks.append(text[:end])
        text = text[end+1:]

    return chunks
