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
		# add a menu bar
		self.main_menu = self.menuBar()
		# add a sub menu for commands
		self.commands_menu = self.main_menu.addMenu("&Commands Menu")
		# add a stacked widget for multiple pages
		self.pages = QtWidgets.QStackedWidget()
		# show stacked widget
		self.setCentralWidget(self.pages)
		# generate UI pages from text file attached
		self.generator()

	#_________________________________GENERATING VIEWS_______________________________________

	def generator(self):
		# a dictionary to store pages with indeces
		page_dict = {}
		# index counter
		index = 0
		# open text file and read line by line
		with open("notes.txt", "r") as file:
			for line in file:
				# check if line contains a heading / what / how using regex
				heading = re.search(r'{(.*?)}:', line)
				what = re.search(r'- (.*?):', line)
				how = re.search(r'  \((.*?)\)', line)
				if heading:
					# store the heading (command name)
					name = heading.group(1)
					# create a page for the command
					self.page = CommandPage(name)
					# add the page to the staked widgeet "pages"
					self.pages.addWidget(self.page)
					# add (name: index to) the dictionary
					page_dict[name] = index
					index += 1
				elif what:
					hold_what = what
				elif how:
					self.section = CommandSection(hold_what.group(1), how.group(1))
					self.page.layout.addWidget(self.section, 0, QtCore.Qt.AlignCenter)

		# access page by command "name"
		self.pages.setCurrentIndex(page_dict["init"])



def main():
	app = QtWidgets.QApplication(sys.argv)
	app.setStyle(QtWidgets.QStyleFactory.create("Fusion"))
	window = Window()
	window.show()
	sys.exit(app.exec_())

if __name__ == "__main__":
	main()
