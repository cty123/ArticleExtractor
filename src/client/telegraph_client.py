from telegraph import Telegraph


class TelegraphClient:

    def __init__(self, client: Telegraph = Telegraph(), account_name: str = "default") -> None:
        self.telegraph = client
        self.telegraph.create_account(short_name=account_name)

    def create_page(self, title: str, full_content: str) -> str:
        response = self.telegraph.create_page(
            title,
            html_content=full_content
        )

        return 'https://telegra.ph/{}'.format(response['path'])
