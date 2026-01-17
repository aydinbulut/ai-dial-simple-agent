from typing import Any

from task.tools.users.base import BaseUserServiceTool


class SearchUsersTool(BaseUserServiceTool):

    @property
    def name(self) -> str:
        #TODO: Provide tool name as `search_users`
        return 'search_users'

    @property
    def description(self) -> str:
        #TODO: Provide description of this tool
        return 'Tool to search for users in the system based on provided criteria. At least one of the parameters should be provided.'

    @property
    def input_schema(self) -> dict[str, Any]:
        #TODO:
        # Provide tool params Schema:
        # - name: str
        # - surname: str
        # - email: str
        # - gender: str
        # None of them are required (see UserClient.search_users method)
        return {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "The first name of the user to search for"
                },
                "surname": {
                    "type": "string",
                    "description": "The last name of the user to search for"
                },
                "email": {
                    "type": "string",
                    "description": "The email of the user to search for"
                },
                "gender": {
                    "type": "string",
                    "description": "The gender of the user to search for"
                }
            },
            "required": []
        }

    def execute(self, arguments: dict[str, Any]) -> str:
        #TODO:
        # 1. Call user_client search_users (with `**arguments`) and return its results
        # 2. Optional: You can wrap it with `try-except` and return error as string `f"Error while searching users: {str(e)}"`
        # -- example response:
        # ```\n  id: 1016\n  name: Aydin\n  surname: Bulut\n  email: aydin@gmail.com\n  phone: 06596565\n  date_of_birth: 1992-01-01\n  address: {'country': 'Netherlands', 'city': 'Amsterdam', 'street': 'danzigerakde', 'flat_house': '4 1013ap'}\n  gender: male\n  company: epam\n  salary: 10000.0\n  about_me: I am a software engineer\n  credit_card: None\n  created_at: 2026-01-15T07:03:30.436177\n```\n```\n  id: 1017\n  name: Aydin\n  surname: Bulut\n  email: aydin2@gmail.com\n  phone: 06596565\n  date_of_birth: 1992-01-01\n  address: {'country': 'Netherlands', 'city': 'Amsterdam', 'street': 'danzigerakde', 'flat_house': '4 1013ap'}\n  gender: man\n  company: epam\n  salary: 10000.0\n  about_me: I am a software engineer\n  credit_card: None\n  created_at: 2026-01-15T07:04:07.198232\n```\n```\n  id: 1021\n  name: Aydin\n  surname: Bulut\n  email: aydin_bulut@epam.com\n  phone: 06596565\n  date_of_birth: 1992-01-01\n  address: {'country': 'Netherlands', 'city': 'Amsterdam', 'street': 'danzigerakde', 'flat_house': '4 1013ap'}\n  gender: male\n  company: epam\n  salary: 10000.0\n  about_me: I am a software engineer\n  credit_card: None\n  created_at: 2026-01-15T07:06:16.533179\n```\n```\n  id: 1022\n  name: Aydin\n  surname: Bulut\n  email: fdgdfgdfg_ghfgfghfgh@epam.com\n  phone: 06596565\n  date_of_birth: 1992-01-01\n  address: {'country': 'Netherlands', 'city': 'Amsterdam', 'street': 'danzigerakde', 'flat_house': '4 1013ap'}\n  gender: male\n  company: epam\n  salary: 10000.0\n  about_me: I am a software engineer\n  credit_card: None\n  created_at: 2026-01-15T07:06:34.345466\n```\n```\n  id: 1023\n  name: Aydin\n  surname: Bulut\n  email: fdgdfg_fghfghgfh@epam.com\n  phone: 06596565\n  date_of_birth: 1992-01-01\n  address: {'country': 'Netherlands', 'city': 'Amsterdam', 'street': 'danzigerakde', 'flat_house': '4 1013ap'}\n  gender: male\n  company: epam\n  salary: 10000.0\n  about_me: I am a software engineer\n  credit_card: None\n  created_at: 2026-01-15T07:08:20.935794\n```
        try:
            result = self.user_client.search_users(**arguments)
            return result
        except Exception as e:
            return f"Error while searching users: {str(e)}"