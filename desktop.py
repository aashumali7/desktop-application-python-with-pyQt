#import area 
import sys
#from topmodule.submodule import elem1,elem2,...
from PyQt6.QtWidgets import QApplication,QMainWindow,QMenu
from PyQt6.QtGui import QIcon


#create class object
app = QApplication([]) #empty list passing 

window = QMainWindow()
window.showMaximized() #window in a maximized state
window.setWindowTitle("Theaashish")  # Set window title 
window.show()

window_icon = QIcon("./python.png")  # Replace icon
window.setWindowIcon(window_icon)

#create a menu bar
menu_bar = window.menuBar()
calculator_menu = menu_bar.addMenu("Calculator")
standard_menu = calculator_menu.addMenu("standard")
standard_menu = calculator_menu.addMenu("New")
standard_menu = calculator_menu.addMenu("Select all")
standard_submenu = standard_menu.addMenu('Save')
Convertor_menu = menu_bar.addMenu("Convertor")
setting_menu = menu_bar.addMenu("Setting")

app.exec()
