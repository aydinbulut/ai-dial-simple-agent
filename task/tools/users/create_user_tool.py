from typing import Any

from task.tools.users.base import BaseUserServiceTool
from task.tools.users.models.user_info import UserCreate


class CreateUserTool(BaseUserServiceTool):

    @property
    def name(self) -> str:
        #TODO: Provide tool name as `add_user`
        return 'add_user'

    @property
    def description(self) -> str:
        #TODO: Provide description of this tool
        return 'Tool to create a new user in the system.'

    @property
    def input_schema(self) -> dict[str, Any]:
        #TODO: Provide tool params Schema. To do that you can create json schema from UserCreate pydentic model ` UserCreate.model_json_schema()`
        return UserCreate.model_json_schema()

    def execute(self, arguments: dict[str, Any]) -> str:
        #TODO:
        # 1. Validate arguments with `UserCreate.model_validate`
        user_data = UserCreate.model_validate(arguments)
        # 2. Call user_client add user and return its results
        # 3. Optional: You can wrap it with `try-except` and return error as string `f"Error while creating a new user: {str(e)}"`
        # -- example response:
        # User successfully added: {"id":1023,"name":"Aydin","surname":"Bulut","email":"fdgdfg_fghfghgfh@epam.com","phone":"06596565","date_of_birth":"1992-01-01","address":{"country":"Netherlands","city":"Amsterdam","street":"danzigerakde","flat_house":"4 1013ap"},"gender":"male","company":"epam","salary":10000.0,"about_me":"I am a software engineer","credit_card":null,"created_at":"2026-01-15T07:08:20.935794"}
        try:
            result = self.user_client.add_user(user_create_model=user_data)
            return result
        except Exception as e:
            return f"Error while creating a new user: {str(e)}"