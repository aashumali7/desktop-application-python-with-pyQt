import sys
import requests
import sqlite3
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLabel, QLineEdit, QHBoxLayout, QMessageBox
from PyQt6.QtGui import QIcon, QDesktopServices
from PyQt6.QtCore import QUrl


         #module.method(actualargument)
connect = sqlite3.connect('aashish.db')
cursor = connect.cursor()

#create table
# ... (previous code)

#create table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT NOT NULL,
        s_number TEXT NOT NULL
    )
""")
connect.commit()

# ... (rest of the code)
  
connect.commit() # Execute/Perform the SQL query     

"""connectionId = sqlite5.connect('a.db')
print(connectionId)"""

def on_ok_clicked():
    payload = {
        "data": {
            "Firstname": fname_input.text(),
            "Lastname": lname_input.text(),
            "email": email_input.text(),
            "sno": s_number.text()
        }
    }

    try:
        cursor.execute("""
            INSERT INTO users (first_name, last_name, email, s_number) 
            VALUES (?, ?, ?, ?)
        """, (
            payload["data"]["Firstname"],
            payload["data"]["Lastname"],
            payload["data"]["email"],
            payload["data"]["sno"]
        ))
        connect.commit()
        aashu("Test", "Registration Successful")
        reset_inputs()
    except Exception as e:
        print(f"An error occurred: {e}")


def aashu(title, text):
    a_box = QMessageBox()
    a_box.setWindowTitle(title)
    a_box.setText(text)
    a_box.exec()

def reset_inputs():
    fname_input.clear()
    lname_input.clear()
    email_input.clear()
    s_number.clear()

def open_google():
    QDesktopServices.openUrl(QUrl("https://www.google.com"))

def close_window():
    window.close()    

app = QApplication([])

window = QWidget()
window.setWindowTitle("Theaashish")
#window.showMaximized()

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
license_button.clicked.connect(open_google)
cancel_button.clicked.connect(close_window)

window.setLayout(layout)
window.show()

window_icon = QIcon("./python.png")
window.setWindowIcon(window_icon)

sys.exit(app.exec())
