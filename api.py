import sys
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLabel, QLineEdit, QHBoxLayout
from PyQt6.QtGui import QIcon
import requests

def on_ok_clicked():
    api_url = "http://localhost:1337/api/registrations"
    payload = {
        "data": {
            "Firstname": "Aashu",
            "Lastname": "mali",
            "email": "Aashumali98@gmail.com",
            "sno": "7"
        }
    }

    headers = {
        "Content-Type": "application/json",
        # Add any additional headers or authentication details here
    }

    try:
        response = requests.post(api_url, json=payload, headers=headers)

        if response.status_code == 200:
            print("Registration successful")
            print("Response:", response.text)
        else:
            print(f"Registration failed. Status code: {response.status_code}")
            print("Response:", response.text)

    except Exception as e:
        print(f"An error occurred: {e}")


app = QApplication([])

window = QWidget()
window.setWindowTitle("Theaashish")
window.showMaximized()

layout = QGridLayout()

fname = QLabel("FirstName")
lname = QLabel("LastName")
email = QLabel("Email")
snumber = QLabel("Serial Number")

fname_input = QLineEdit()
lname_input = QLineEdit()
email_input = QLineEdit()
s_number = QLineEdit()

layout.addWidget(fname, 0, 0)
layout.addWidget(fname_input, 0, 1)
layout.addWidget(lname, 1, 0)
layout.addWidget(lname_input, 1, 1)
layout.addWidget(email, 2, 0)
layout.addWidget(email_input, 2, 1)
layout.addWidget(snumber, 3, 0)
layout.addWidget(s_number, 3, 1)

ok_button = QPushButton("Ok")
license_button = QPushButton("How To License")
cancel_button = QPushButton("Cancel")

button_layout = QHBoxLayout()

button_layout.addWidget(ok_button)
button_layout.addWidget(license_button)
button_layout.addWidget(cancel_button)

layout.addLayout(button_layout, 4, 0, 1, 2)

ok_button.clicked.connect(on_ok_clicked)

window.setLayout(layout)
window.show()

window_icon = QIcon("./python.png")
window.setWindowIcon(window_icon)

sys.exit(app.exec())
