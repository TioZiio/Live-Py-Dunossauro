
# Arquivo de Documentação / Entitles

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def is_valid(self):
        return len(self.password) > 6

# Arquivo de configuração / User Cases

class LoginUseCase:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def execute(self, username, password):
        user = self.user_repository.find_by_username(username)
        print(user.username, user.password)
        if user.username == username and user.password == password:
            return {"success": True, "username": user.username}
        return {"success": False}

# Arquivo de Controllers

class LoginController:
    def __init__(self, login_use_case):
        self.login_use_case = login_use_case

    def handle(self, username, password):
        result = self.login_use_case.execute(username, password)
        return result


# Arquivo de Presenters

class LoginPresenter:
    def present(self, result):
        if result["success"]:
            return f"Welcome, {result['username']}!"
        return "Login failed. Try again."

# Arquivo de Gateway

class UserRepository:
    def __init__(self):
        self.users = {"david": User("david", "123")}

    def find_by_username(self, username):
        return self.users.get(username)

# Arquivo de Interface do Usuário

# Simula a interação do usuário com o sistema
def cli_login_interface():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Chamando o controlador
    controller = LoginController(LoginUseCase(UserRepository()))
    result = controller.handle(username, password)

    # Usando o Presenter para formatar a resposta
    presenter = LoginPresenter()
    message = presenter.present(result)

    print(message)

if __name__ == "__main__":
    cli_login_interface()

