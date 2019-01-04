import sys
from PyQt5 import QtWidgets, QtCore

class CommandPage(QtWidgets.QWidget):
	def __init__(self, label_parameter):
		# initialize CommandPage as a QWidget
		super(CommandPage, self).__init__()
		# add a vertical layout
		self.layout = QtWidgets.QVBoxLayout()
		self.layout.setAlignment(QtCore.Qt.AlignHCenter) # align cells of layout
		self.setLayout(self.layout)
		# add the label parameter to the page
		self.command_label = QtWidgets.QLabel(label_parameter)
		self.command_label.setStyleSheet("QLabel {font-size: 20px; font-weight: bold}")
		# add label to layout
		self.layout.addWidget(self.command_label, 0, QtCore.Qt.AlignTop) # align widget inside cell

class CommandSection(QtWidgets.QWidget):
	def __init__(self, what_parameter, how_parameter):
		# initialize CommandSection as a QWidget
		super(CommandSection, self).__init__()
		# add a vertical layout
		self.layout = QtWidgets.QVBoxLayout()
		self.layout.setAlignment(QtCore.Qt.AlignHCenter)
		self.setLayout(self.layout)
		# add the what parameter to the section as a label
		self.what = QtWidgets.QLabel(what_parameter)
		# add the how parameter to the section as a text area
		self.how = QtWidgets.QLineEdit(how_parameter)

		# add what and how to layout
		self.layout.addWidget(self.what, 0, QtCore.Qt.AlignCenter)
		self.layout.addWidget(self.how, 0, QtCore.Qt.AlignCenter)

class Window(QtWidgets.QMainWindow):
	def __init__(self):
		# initialize Window as a QMainWindow
		super(Window, self).__init__()
		# modify Window
		self.setWindowTitle("Git Memo")
		self.setGeometry(500, 50, 400, 500)


		# test: adding a page to the main window
		self.page1 = CommandPage("Commit")
		self.setCentralWidget(self.page1)
		# test: adding a section to the page
		self.sec1 = CommandSection("Initializing a local git repository", "git init")
		self.page1.layout.addWidget(self.sec1)

	#________________________________________VIEWS_______________________________________





def main():
	app = QtWidgets.QApplication(sys.argv)
	#app.setStyle(QtWidgets.QStyleFactory.create("Fusion"))
	window = Window()
	window.show()
	sys.exit(app.exec_())

if __name__ == "__main__":
	main()
