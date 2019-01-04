import sys
from PyQt5 import QtWidgets, QtCore

class CommandPage(QtWidgets.QWidget):
	def __init__(self, label_parameter):
		# initialize CommandPage as a QWidget
		super(CommandPage, self).__init__()
		# add a vertical layout
		self.layout = QtWidgets.QVBoxLayout()
		self.layout.setAlignment(QtCore.Qt.AlignTop) # align cells of layout
		self.setLayout(self.layout)
		# add the label parameter to the page
		self.command_label = QtWidgets.QLabel(label_parameter)
		self.command_label.setStyleSheet("""
			QLabel {color:green; 
			        font-size: 20px; 
			        font-weight: bold; 
			        margin: 20px; 
			        padding: 5px;
			        border: 1px solid black;
			        border-radius: 2px
			        }""")
		# add label to layout
		self.layout.addWidget(self.command_label, 0, QtCore.Qt.AlignCenter) # align widget inside cell

class CommandSection(QtWidgets.QWidget):
	def __init__(self, what_parameter, how_parameter):
		# initialize CommandSection as a QWidget
		super(CommandSection, self).__init__()
		# add a vertical layout
		self.layout = QtWidgets.QVBoxLayout()
		self.layout.setAlignment(QtCore.Qt.AlignTop)
		self.setLayout(self.layout)
		# add the what parameter to the section as a label
		self.what = QtWidgets.QLabel(what_parameter)
		self.what.setFixedWidth(500)
		self.what.setWordWrap(True)
		self.what.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed) # no expanding in x, y
		self.what.setStyleSheet("QLabel {font-size: 14px}")
		# add the how parameter to the section as a text area
		self.how = QtWidgets.QLineEdit(how_parameter)
		self.how.setReadOnly(True)
		self.how.setFixedSize(500, 30)
		self.how.setStyleSheet("""
			QLineEdit {font-size: 14px; 
			           background-color: #5b7bad; 
			           color: white; 
			           padding-left: 5px}""")
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
		self.page1 = CommandPage("init")
		self.setCentralWidget(self.page1)
		# test: adding a section to the page
		self.sec1 = CommandSection("- Initializing a local git repository in the current directory", "git init")
		self.page1.layout.addWidget(self.sec1)

		self.sec2 = CommandSection("- Add changes in the current working directory to the staging area before committing any changes.", "git add .")
		self.page1.layout.addWidget(self.sec2)


	#________________________________________VIEWS_______________________________________





def main():
	app = QtWidgets.QApplication(sys.argv)
	app.setStyle(QtWidgets.QStyleFactory.create("Fusion"))
	window = Window()
	window.show()
	sys.exit(app.exec_())

if __name__ == "__main__":
	main()
