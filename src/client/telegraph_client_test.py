import unittest
from unittest.mock import Mock, MagicMock
from src.client.telegraph_client import TelegraphClient


class TestStringMethods(unittest.TestCase):

    def test_telegraph_publish(self):
        # Given
        mocked_client = Mock()
        mocked_client.create_page = MagicMock(return_value={"path": "test"})
        client = TelegraphClient(client=mocked_client)

        # When
        client.create_page(title="foo", full_content="bar")

        # Then
        mocked_client.create_page.assert_called_once_with(
            "foo", html_content="bar")


if __name__ == "__main__":
    unittest.main()
