from typing import Any

from task.tools.users.base import BaseUserServiceTool
from task.tools.users.models.user_info import UserUpdate


class UpdateUserTool(BaseUserServiceTool):

    @property
    def name(self) -> str:
        #TODO: Provide tool name as `update_user`
        return 'update_user'

    @property
    def description(self) -> str:
        #TODO: Provide description of this tool
        return 'Tool to update an existing user in the system by ID.'

    @property
    def input_schema(self) -> dict[str, Any]:
        #TODO:
        # Provide tool params Schema:
        # - id: number, required, User ID that should be updated.
        # - new_info: UserUpdate.model_json_schema()
        return {
            "type": "object",
            "properties": {
                "id": {
                    "type": "integer",
                    "description": "The ID of the user to be updated"
                },
                "new_info": UserUpdate.model_json_schema()
            },
            "required": [
                "id",
                "new_info"
            ]
        }

    def execute(self, arguments: dict[str, Any]) -> str:
        #TODO:
        # 1. Get user `id` from `arguments`
        user_id = arguments["id"]
        # 2. Get `new_info` from `arguments` and create `UserUpdate` via pydentic `UserUpdate.model_validate`
        new_info = UserUpdate.model_validate(arguments["new_info"])
        # 3. Call user_client update_user and return its results
        # 4. Optional: You can wrap it with `try-except` and return error as string `f"Error while creating a new user: {str(e)}"`
        # -- example response:
        # User successfully updated: {"id":1016,"name":"Aydin","surname":"Bulut","email":"aydin_dev@gmail.com","phone":"06596565","date_of_birth":"1992-01-01","address":{"country":"Netherlands","city":"Amsterdam","street":"danzigerakde","flat_house":"4 1013ap"},"gender":"male","company":"epam","salary":10000.0,"about_me":"I am a software engineer","credit_card":null,"created_at":"2026-01-15T07:03:30.436177"}
        try:
            result = self.user_client.update_user(user_id=user_id, user_update_model=new_info)
            return result
        except Exception as e:
            return f"Error while updating user: {str(e)}"