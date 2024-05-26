from blacksheep.server.controllers import Controller, post
from ...core.dto.auth import LoginData
from ...services.auth import AuthService


class AuthRouter(Controller):
    @post("/login")
    async def login(self, login_data: LoginData, auth_service: AuthService):
        return await auth_service.authenticate(login_data)
