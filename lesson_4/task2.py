from abc import ABC
from datetime import date


class Authorization(ABC):
    users = dict()

    def sign_up(self, login, password, confirm_password):
        if password == confirm_password:
            self.users.update({login: password})
            print('You have successfully registered')
        else:
            print('Passwords do not match!!!')

    def log_in(self, login, password):
        if login in self.users:
            if self.users.values(login) == password:
                print('You have successfully signed in to your account')
            else:
                print('Wrong password!!!')
        else:
            print('Wrong login!!!')


class Post():
    posts = list()

    def post(self, content):
        date_ = date.today()
        self.posts.append(content)
        self.posts.append(date_)
        print(Post.posts)


class Admin(Authorization):

    def print_(self):
        print(Authorization.users)
        print(Post.posts)


A = Authorization()
check = 'zero'

while check == "Reg" or check == "Log" or check == "zero":

    if check == "Reg":
        print("Register")
        login = input("login: ")
        password = input("password: ")
        confirm_password = input("confirm password: ")
        A.sign_up(login, password, confirm_password)
    if check == "Log":
        print("Login")
        login = input("login:")
        password = input("password:")
        A.log_in(login, password)
        # break
    check = input("If you want to register write 'Reg', if you want to login write 'Log': ")

account = 'zero'
while account == 'user' or account == 'code' or account == 'zero':
    if account == 'code':
        admin = Admin(A)
        admin.print_()
    elif account == 'user':
        P = Post()
        post = input("if you want to create a post, write 'post' if you want to view all your posts write 'view': ")
        if post == "post":
            content = input("Enter post content: ")
            P.post(content)
        elif post == "view":
            print(P.posts)
    account = input("If you want to register write 'Reg', if you want to login write 'Log': ")
