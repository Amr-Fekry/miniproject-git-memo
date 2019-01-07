import sys, re
from PyQt5 import QtWidgets, QtCore
from classes import *
from functools import partial

class Window(QtWidgets.QMainWindow):
	def __init__(self):
		# initialize Window as a QMainWindow
		super(Window, self).__init__()
		# modify Window
		self.setWindowTitle("Git Memo")
		self.setGeometry(500, 50, 600, 500)
		# add a menu bar
		self.main_menu = self.menuBar()
		# add a status bar
		self.status = self.statusBar()
		# add a stacked widget for multiple pages
		self.pages = QtWidgets.QStackedWidget()
		# add a scroll area
		self.scroll = QtWidgets.QScrollArea()
		self.scroll.setWidget(self.pages)
		self.scroll.setWidgetResizable(True)
		# show scroll area with stacked widget
		self.setCentralWidget(self.scroll)
		# generate UI pages from text file attached
		self.generator()

	#_________________________________GENERATING VIEWS_______________________________________

	def generator(self):
		# initialize a dictionary to store pages names and indeces
		self.page_dict = {}
		# index counter
		self.index = 0

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
					self.generate_page(name)
				elif what:
					# store for the next round
					hold_what = what
				elif how:
					self.section = CommandSection(hold_what.group(1), how.group(1))
					self.page.layout.addWidget(self.section, 0, QtCore.Qt.AlignCenter)

		self.generate_commands_menu()

	def generate_page(self, name):
		# create a page for the command
		self.page = CommandPage(name)
		# add the page to the stacked widgeet "pages"
		self.pages.addWidget(self.page)
		# add (name: index to) the dictionary
		self.page_dict[name] = self.index
		self.index += 1

	def generate_commands_menu(self):
		# add a sub menu for commands
		commands_menu = self.main_menu.addMenu("&Commands list")
		# generate commands
		for command, page_index in sorted(self.page_dict.items()):
			action = QtWidgets.QAction("&"+command, self)
			action.triggered.connect(partial(self.switch_page, page_index))
			commands_menu.addAction(action)

	def switch_page(self, page_index):
		# access page by page_index
		self.pages.setCurrentIndex(page_index)
		#self.pages.setCurrentIndex(self.page_dict[command_name]) # by command_name

def main():
	app = QtWidgets.QApplication(sys.argv)
	app.setStyle(QtWidgets.QStyleFactory.create("Fusion"))
	window = Window()
	window.show()
	sys.exit(app.exec_())

if __name__ == "__main__":
	main()
