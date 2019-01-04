import sys, re
from PyQt5 import QtWidgets, QtCore
from classes import *

class Window(QtWidgets.QMainWindow):
	def __init__(self):
		# initialize Window as a QMainWindow
		super(Window, self).__init__()
		# modify Window
		self.setWindowTitle("Git Memo")
		self.setGeometry(500, 50, 400, 500)

		# generate UI pages from text file attached
		self.generator()

	#_________________________________GENERATING VIEWS_______________________________________

	def generator(self):
		with open("notes.txt", "r") as file:
			for line in file:
				# check if line contains a heading / what / how using regex
				heading = re.search(r'{(.*?)}:', line)
				what = re.search(r'- (.*?):', line)
				how = re.search(r'  \((.*?)\)', line)
				if heading:
					#print(heading.group(1))
					self.page = CommandPage(heading.group(1))
				elif what:
					hold_what = what
				elif how:
					#print(hold_what.group(1), how.group(1))
					self.section = CommandSection(hold_what.group(1), how.group(1))
					self.page.layout.addWidget(self.section, 0, QtCore.Qt.AlignCenter)

		self.setCentralWidget(self.page)

		

def main():
	app = QtWidgets.QApplication(sys.argv)
	app.setStyle(QtWidgets.QStyleFactory.create("Fusion"))
	window = Window()
	window.show()
	sys.exit(app.exec_())

if __name__ == "__main__":
	main()
