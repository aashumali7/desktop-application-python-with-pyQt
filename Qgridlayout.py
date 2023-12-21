#import area 
import sys
#from topmodule.submodule import elem1,elem2,...
from PyQt6.QtWidgets import QApplication,QWidget,QGridLayout,QPushButton
from PyQt6.QtGui import QIcon


#create class object
app = QApplication([]) #empty list passing 

window = QWidget()
window.showMaximized() #window in a maximized state
window.setWindowTitle("Theaashish")  # Set window title 
window.show()
#co = ClassName
#co.method
button1 = QPushButton('widget 1')
button2 = QPushButton('widget 2')
button3 = QPushButton('widget 3')
button4 = QPushButton('widget 4')

layout = QGridLayout()

layout.addWidget(button1,0,0)
layout.addWidget(button2,0,2)
layout.addWidget(button3,1,0)
layout.addWidget(button4,1,2)


window.setLayout(layout)
window.show()

window_icon = QIcon("./python.png")  # Replace icon
window.setWindowIcon(window_icon)

app.exec()