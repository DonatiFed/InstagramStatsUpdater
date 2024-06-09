
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit
from functools import partial
import InstagramFollowersCheck as IFC

class UserWidget(QWidget):
    def __init__(self, name, username, parent=None):
        super(UserWidget, self).__init__(parent)
        self.name = name
        self.username = username
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.name_label = QLabel("Name: " + self.name)
        layout.addWidget(self.name_label)

        self.username_label = QLabel("Username: " + self.username)
        layout.addWidget(self.username_label)

        self.update_button = QPushButton("Update Profile")
        self.update_button.clicked.connect(self.update_profile)
        layout.addWidget(self.update_button)

        self.setLayout(layout)

    def update_profile(self):
        IFC.update_profile(self.username)

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        # Aggiungi widget utenti
        self.users = [
            {"name": "Mago ", "username": "matteo.postiferi"},
            {"name": "SpotLive", "username": "spotlive.app"},
            {"name": "Teja", "username": "simone_pellicci"},
            {"name": "Danilo", "username": "danilo.popovic___"},
            {"name": "Caps", "username": "federico.donati_"},
            {"name": "Timo", "username": "aletimo__"},
            {"name": "Lauta", "username": "lautaro.cavichia"}
        ]

        self.user_widgets = []
        for user in self.users:
            user_widget = UserWidget(user["name"], user["username"])
            self.user_widgets.append(user_widget)
            self.layout.addWidget(user_widget)

        # Aggiungi pulsante per aggiornare tutti gli utenti
        self.update_all_button = QPushButton("Update All Profiles")
        self.update_all_button.clicked.connect(self.update_all_profiles)
        self.layout.addWidget(self.update_all_button)

        self.setLayout(self.layout)

    def update_all_profiles(self):
        for user_widget in self.user_widgets:
            user_widget.update_profile()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.setWindowTitle('Instagram Profile Updater')
    mainWindow.show()
    sys.exit(app.exec_())

