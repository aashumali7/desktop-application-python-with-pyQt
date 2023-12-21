#import area 
import sys
#from topmodule.submodule import elem1,elem2,...
from PyQt6.QtWidgets import QApplication,QWidget,QGridLayout,QPushButton,QLabel,QLineEdit,QHBoxLayout
from PyQt6.QtGui import QIcon


#create class object
app = QApplication([]) #empty list passing 

window = QWidget()
window.showMaximized() #window in a maximized state
window.setWindowTitle("Theaashish")  # Set window title 
window.show()
#co = ClassName
#co.method
button1 = QPushButton('OK')
button2 = QPushButton('How To License')
button3 = QPushButton('Cancel')

fname = QLabel("FirstName")
lname = QLabel("LastName")
email = QLabel("Email")
snumber = QLabel("Serial Number")

fname_input = QLineEdit()
lname_input = QLineEdit()
email_input = QLineEdit()
s_number = QLineEdit()

layout = QGridLayout()

layout.addWidget(fname,0,0)
layout.addWidget(fname_input,0,1)
layout.addWidget(lname,1,0)
layout.addWidget(lname_input,1,1)
layout.addWidget(email,2,0)
layout.addWidget(email_input,2,1)
layout.addWidget(snumber,3,0)
layout.addWidget(s_number,3,1)

ok_button = QPushButton("Ok")
license_button = QPushButton("How To License")
cancel_button = QPushButton("Cancel")

button_layout = QHBoxLayout()

button_layout.addWidget(ok_button)
button_layout.addWidget(license_button)
button_layout.addWidget(cancel_button)

layout.addLayout(button_layout,4,0,1,2)

window.setLayout(layout)
window.show()

window_icon = QIcon("./python.png")  # Replace icon
window.setWindowIcon(window_icon)

app.exec()