import sys
from PyQt5 import QtWidgets, QtCore
from classes import *

class Window(QtWidgets.QMainWindow):
	def __init__(self):
		# initialize Window as a QMainWindow
		super(Window, self).__init__()
		# modify Window
		self.setWindowTitle("Git Memo")
		self.setGeometry(500, 50, 400, 500)

		"""
		# test: adding a page to the main window
		self.page1 = CommandPage("init")
		self.setCentralWidget(self.page1)
		# test: adding a section to the page
		self.sec1 = CommandSection("- Initializing a local git repository in the current directory", "git init")
		self.page1.layout.addWidget(self.sec1, 0, QtCore.Qt.AlignCenter)

		self.sec2 = CommandSection("- Add changes in the current working directory to the staging area before committing any changes.", "git add .")
		self.page1.layout.addWidget(self.sec2, 0, QtCore.Qt.AlignCenter)
		"""





def main():
	app = QtWidgets.QApplication(sys.argv)
	app.setStyle(QtWidgets.QStyleFactory.create("Fusion"))
	window = Window()
	window.show()
	sys.exit(app.exec_())

if __name__ == "__main__":
	main()
