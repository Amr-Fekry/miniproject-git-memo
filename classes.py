from PyQt5 import QtWidgets, QtCore
import pyperclip

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
		self.command_label.setObjectName("command_label")
		self.command_label.setStyleSheet("""
			#command_label {color:green; 
			        		font-size: 20px; 
			    		    font-weight: bold; 
			   		        margin: 20px; 
			    		    padding: 5px;
			        		border: 1px solid black;
			        		border-radius: 2px}""")
		# add label to layout
		self.layout.addWidget(self.command_label, 0, QtCore.Qt.AlignCenter) # align widget inside cell

class CommandSection(QtWidgets.QFrame):
	def __init__(self, what_parameter, how_parameter):
		# initialize CommandSection as a QFrame
		super(CommandSection, self).__init__()
		# add a border to the CommandSection QFrame
		self.setObjectName("CommandSection")
		self.setStyleSheet("""
			#CommandSection {border: 1px solid lightgray;
			                 border-radius: 5px;
			                 background-color: #b3c0d6;
			                 margin: 0 0 10 0}""")
		# add a vertical layout
		self.layout = QtWidgets.QVBoxLayout()
		self.layout.setAlignment(QtCore.Qt.AlignTop)
		self.setLayout(self.layout)
		# add the what parameter to the section as a label
		self.what = QtWidgets.QLabel(what_parameter)
		self.what.setFixedWidth(500)
		self.what.setWordWrap(True)
		self.what.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed) # no expanding in x, y
		self.what.setObjectName("what")
		self.what.setStyleSheet("#what {font-size: 14px}")
		# add the how parameter to the section as a text area
		self.how = QtWidgets.QPushButton(how_parameter)
		self.how.setToolTip("Click to copy")
		self.how.clicked.connect(self.copy_text)
		self.how.setFixedSize(500, 30)
		self.how.setObjectName("how")
		self.how.setStyleSheet("""
			#how {font-size: 14px; 
			      background-color: #1b2535; 
			      color: white; 
			      padding-left: 5px;
			      text-align: left;
			      margin-top: 5px}""")
		# add what and how to layout
		self.layout.addWidget(self.what, 0, QtCore.Qt.AlignCenter)
		self.layout.addWidget(self.how, 0, QtCore.Qt.AlignCenter)

	def copy_text(self):
		# get text on btton
		text = self.how.text()
		# copy to clip board
		pyperclip.copy(text)
		# display massege on status bar of oldest parent window()
		self.window().status.showMessage("Copied ( " + text + " )")
		
