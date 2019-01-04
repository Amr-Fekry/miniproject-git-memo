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
		# add a the label parameter to the page
		self.command_label = QtWidgets.QLabel(label_parameter)
		self.command_label.setStyleSheet("QLabel {font-size: 20px; font-weight: bold}")
		# add label to layout
		self.layout.addWidget(self.command_label, 0, QtCore.Qt.AlignTop) # align widget inside cell


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

	#________________________________________VIEWS_______________________________________





def main():
	app = QtWidgets.QApplication(sys.argv)
	#app.setStyle(QtWidgets.QStyleFactory.create("Fusion"))
	window = Window()
	window.show()
	sys.exit(app.exec_())

if __name__ == "__main__":
	main()
