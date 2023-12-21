#import area 
import sys
#from topmodule.submodule import elem1,elem2,...
from PyQt6.QtWidgets import QApplication,QWidget,QVBoxLayout,QPushButton
from PyQt6.QtGui import QIcon


#create class object
app = QApplication([]) #empty list passing 

window = QWidget()
window.showMaximized() #window in a maximized state
window.setWindowTitle("Theaashish")  # Set window title 
window.show()
#co = ClassName
#co.method
layout = QVBoxLayout()

layout.addWidget(QPushButton("Widget 1"))
layout.addWidget(QPushButton("Widget 2"))
layout.addWidget(QPushButton("Widget 3"))
layout.addWidget(QPushButton("Widget 4"))


window.setLayout(layout)
window.show()

window_icon = QIcon("./python.png")  # Replace icon
window.setWindowIcon(window_icon)

app.exec()