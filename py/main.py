from PyQt5 import QtWidgets
from UI.SignUpUI import Ui_MainWindow as win_signup
from UI.SignInUI import Ui_MainWindow as win_signin
from UI.mainUI import Ui_MainWindow as win_main
from UI.lkUI import Ui_MainWindow as win_lk
import dataBase
import bcrypt
import sys


class SignUp(QtWidgets.QMainWindow):
    def __init__(self):
        super(SignUp, self).__init__()
        self.ui = win_signup()
        self.ui.setupUi(self)
        self.ui.signUp.clicked.connect(self.registration)
        self.ArrABC = [i for i in 'qwertyuiopasdfghjklzxcvbnm0123456789_']

    def registration(self):
        self.clear_label()
        self.login = self.ui.line_login.text()
        self.password = self.ui.line_password.text()
        self.password_repeat = self.ui.line_password_repeat.text()

        self.check_error = {
            "check_users_in_db": [self.check_login_in_db(self.login), self.ui.error_login.setText,
                                  "Пользователь с данным логиным существует"],
            "check_len_login": [len(self.login) < 6, self.ui.error_login.setText,
                                "Длинна логина меньше 6"],
            "check_symbol": [not all([i.lower() in self.ArrABC for i in self.login]),
                             self.ui.error_login.setText,
                             "Логин должен состоять из лат. символов"],
            "check_len_password": [len(self.password) < 3,
                                   self.ui.error_password.setText,
                                   "Длинна пароля меньше 3"],
            "check_idenity_password": [self.password != self.password_repeat,
                                       self.ui.error_password_repeat.setText,
                                       "Пароли не совпадают"]}
        for i in self.check_error:
            if self.check_error[i][0]:
                text = self.check_error[i][2]
                return self.check_error[i][1](text)
        else:
            hashAndSalt = bcrypt.hashpw(self.password.encode(), bcrypt.gensalt()).decode('utf-8')
            dataBase.execute_into(f"""INSERT INTO users (login, password, position) 
                                            VALUES('{self.login}', '{hashAndSalt}', 0)""")
            self.show_SignIn()

    def check_login_in_db(self, login):
        query = f"""SELECT * FROM users WHERE login = '{login}'"""
        return bool(len([i for i in dataBase.execute_sel(query)]))

    def clear_label(self):
        self.ui.error_login.setText("")
        self.ui.error_password.setText("")
        self.ui.error_password_repeat.setText("")

    def show_SignIn(self):
        self.hide()
        self.w = SignIn()
        self.w.show()


class SignIn(QtWidgets.QMainWindow):
    def __init__(self):
        super(SignIn, self).__init__()
        self.ui = win_signin()
        self.ui.setupUi(self)
        self.ui.signIn.clicked.connect(self.open)


    def open(self):
        self.login = self.ui.login_line.text()
        self.password = self.ui.password_line.text()
        self.check(self.login, self.password)

    def check(self, login, password):
        passwordHash = [i for i in dataBase.execute_sel(f"""SELECT password FROM users 
                                    WHERE login = '{login}'""")]
        if bool(passwordHash):
            valid = bcrypt.checkpw(password.encode(), str.encode(passwordHash[0][0]))
            if (valid):
                return self.show_Main()
        return self.ui.error.setText("Логин или пароль не верны")

    def show_SignUp(self):
        self.hide()
        self.w = SignUp()
        self.w.show()

    def show_Main(self):
        self.hide()
        self.w = Main()
        self.w.show()


class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.ui = win_main()
        self.ui.setupUi(self)
        self.ui.lk.triggered.connect(self.open_lk)

    def open_lk(self):
        print(123)
        self.w = LK()
        self.w.show()


class LK(QtWidgets.QMainWindow):
    def __init__(self):
        super(LK, self).__init__()
        self.ui = win_lk()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = SignUp()
    application.show()
    sys.exit(app.exec())
