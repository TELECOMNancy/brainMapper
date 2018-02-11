# NAME
#		  calculationView
#
# DESCRIPTION
#
#		 'calculationView' contains the Qwidget for the calculation view
#
# HISTORY
#
# 15 january 2018 - Initial design and coding. (@maximeCluchague, Maxime C.)

from PyQt4 import QtGui
from PyQt4.Qt import *

import sys

from os import path

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from BrainMapper import *

import resources


class CalculationView(QtGui.QWidget):
    # -- ! ATTRIBUTES SHARED by EVERY class instance ! --

    # ------ pyqt Signals ------
    # We will use signals to know when to change the central view (central widget) of our app
    # In our custom widgets (like this one), buttons will emit a given signal, and the change of views will be handled
    # by the HomePage widgets' instances (see UI.py, class HomePage)

    showMain = pyqtSignal()

    def __init__(self):
        super(CalculationView, self).__init__()
        self.leftlist = QListWidget()
        self.leftlist.insertItem(0, 'Addition')
        self.leftlist.insertItem(1, 'Boolean Interserction')
        self.leftlist.insertItem(2, 'Boolean Union')
        self.leftlist.insertItem(3, 'Centroide')
        self.leftlist.insertItem(4, 'Dilation')
        self.leftlist.insertItem(5, 'Entropy')
        self.leftlist.insertItem(6, 'Erosion')
        self.leftlist.insertItem(7, 'Linear combination')
        self.leftlist.insertItem(8, 'Mean')
        self.leftlist.insertItem(9, 'Normalization')
        self.leftlist.insertItem(10, 'Substraction')

        self.stack1 = QWidget()
        self.stack2 = QWidget()
        self.stack3 = QWidget()
        self.stack4 = QWidget()
        self.stack5 = QWidget()
        self.stack6 = QWidget()
        self.stack7 = QWidget()
        self.stack8 = QWidget()
        self.stack9 = QWidget()
        self.stack10 = QWidget()
        self.stack11 = QWidget()

        self.stack1UI()
        self.stack2UI()
        self.stack3UI()
        self.stack4UI()
        self.stack5UI()
        self.stack6UI()
        self.stack7UI()
        self.stack8UI()
        self.stack9UI()
        self.stack10UI()
        self.stack11UI()
        
        self.Stack = QStackedWidget(self)
        self.Stack.addWidget(self.stack1)
        self.Stack.addWidget(self.stack2)
        self.Stack.addWidget(self.stack3)
        self.Stack.addWidget(self.stack4)
        self.Stack.addWidget(self.stack5)
        self.Stack.addWidget(self.stack6)
        self.Stack.addWidget(self.stack7)
        self.Stack.addWidget(self.stack8)
        self.Stack.addWidget(self.stack9)
        self.Stack.addWidget(self.stack10)
        self.Stack.addWidget(self.stack11)

        self.goHomeButton = QtGui.QPushButton('Go back')
        self.goHomeButton.setIcon(QtGui.QIcon(':ressources/app_icons_png/home-2.png'))
        self.goHomeButton.setToolTip("Return to main page")
        self.goHomeButton.clicked.connect(self.showMain.emit)

        self.runOpperationButton = QtGui.QPushButton('Calculate')
        self.runOpperationButton.setIcon(QtGui.QIcon(':ressources/app_icons_png/calculator.png'))
        self.runOpperationButton.setToolTip("Run selected opperation")
        self.runOpperationButton.clicked.connect(lambda: self.runCalculation())

        # self.saveFile = QtGui.QPushButton('Save file')
        # self.saveFile.setIcon(QtGui.QIcon(':ressources/app_icons_png/download.png'))
        # self.saveFile.setToolTip("Save the calculated resulting file")

        vbox = QVBoxLayout(self)

        hbox = QHBoxLayout(self)
        hbox.addWidget(self.leftlist)
        hbox.addWidget(self.Stack)
        
        hbox.addWidget
        
        
        vbox.addLayout(hbox)

        self.console = QTextEdit(">>>")
        self.console.setReadOnly(True)
        self.console.setFixedHeight(220)
        vbox.addWidget(self.console)        
        
        buttonbox = QtGui.QHBoxLayout()
        buttonbox.addStretch(0)
        buttonbox.addWidget(self.goHomeButton)

        buttonbox.addStretch(1)
        buttonbox.addWidget(self.runOpperationButton)

        vbox.addLayout(buttonbox)

        self.setLayout(vbox)
        self.leftlist.currentRowChanged.connect(self.display)
        self.show()

    # ----- Addition ------------------------------------
    def stack1UI(self):
        vbox = QVBoxLayout(self)
        layout = QFormLayout()
        vbox.addLayout(layout)

        options = QLabel("Options")
        options.setStyleSheet("background-color: #FFCC33;")
        layout.addRow(options)

        descrip = QLabel("Description")
        descrip.setStyleSheet("background-color: #FFCC33;")
        layout.addRow(QLabel("\n"))
        layout.addRow(descrip)

        descbox = QtGui.QVBoxLayout()
        description = QTextEdit("The Addition algorithm make a addition with a collection of nifti makes the term some term of each voxel")
        description.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        description.setReadOnly(True)

        descbox.addWidget(description)
        description.setStyleSheet("background-color: #e2dfdd; padding:5px; border-radius:7px; border: solid #bdbbb6; ")
        vbox.addLayout(descbox)
        # self.setTabText(0,"Calculation Details")
        self.stack1.setLayout(vbox)

    # ----- Boolean Intersection -----------------------
    def stack2UI(self):
        vbox = QVBoxLayout(self)
        layout = QFormLayout()
        vbox.addLayout(layout)

        options = QLabel("Options")
        options.setStyleSheet("background-color: #FFCC33;")
        layout.addRow(options)

        descrip = QLabel("Description")
        descrip.setStyleSheet("background-color: #FFCC33;")
        layout.addRow(QLabel("\n"))
        layout.addRow(descrip)

        descbox = QtGui.QVBoxLayout()
        description = QTextEdit("The Boolean intersection takes a set of files and returns a binary file of 0 and 1. A voxel with 1 value means that for every file this voxels have strictely positive intensity")
        description.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        description.setReadOnly(True)

        descbox.addWidget(description)
        description.setStyleSheet("background-color: #e2dfdd; padding:5px; border-radius:7px; border: solid #bdbbb6; ")
        vbox.addLayout(descbox)
        self.stack2.setLayout(vbox)

    # ----- Boolean Union ----------------------------
    def stack3UI(self):
        vbox = QVBoxLayout(self)
        layout = QFormLayout()
        vbox.addLayout(layout)

        options = QLabel("Options")
        options.setStyleSheet("background-color: #FFCC33;")
        layout.addRow(options)

        descrip = QLabel("Description")
        descrip.setStyleSheet("background-color: #FFCC33;")
        layout.addRow(QLabel("\n"))
        layout.addRow(descrip)

        descbox = QtGui.QVBoxLayout()
        description = QTextEdit("The Boolean union takes a set of files and returns a binary file of 0 and 1. A voxel with 1 value means that there exists in at least some files nifti a voxel whose intensity is strictly positive")
        description.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        description.setReadOnly(True)

        descbox.addWidget(description)
        description.setStyleSheet("background-color: #e2dfdd; padding:5px; border-radius:7px; border: solid #bdbbb6; ")
        vbox.addLayout(descbox)
        self.stack3.setLayout(vbox)

    # ----- Centroide ------------------------------------
    def stack4UI(self):
        vbox = QVBoxLayout(self)
        layout = QFormLayout()
        vbox.addLayout(layout)

        options = QLabel("Options")
        options.setStyleSheet("background-color: #FFCC33;")
        layout.addRow(options)

        descrip = QLabel("Description")
        descrip.setStyleSheet("background-color: #FFCC33;")
        layout.addRow(QLabel("\n"))
        layout.addRow(descrip)

        descbox = QtGui.QVBoxLayout()
        description = QTextEdit("This algorithm calculates the centroid of each cluster present in one or a set of nifti files")
        description.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        description.setReadOnly(True)

        descbox.addWidget(description)
        description.setStyleSheet("background-color: #e2dfdd; padding:5px; border-radius:7px; border: solid #bdbbb6; ")
        vbox.addLayout(descbox)
        self.stack4.setLayout(vbox)

    # ----- Dilatation ---------------------------
    def stack5UI(self):
        vbox = QVBoxLayout(self)
        layout = QFormLayout()
        vbox.addLayout(layout)

        options = QLabel("Options")
        options.setStyleSheet("background-color: #FFCC33;")
        layout.addRow(options)

        descrip = QLabel("Description")
        descrip.setStyleSheet("background-color: #FFCC33;")
        layout.addRow(QLabel("\n"))
        layout.addRow(descrip)

        descbox = QtGui.QVBoxLayout()
        description = QTextEdit("TO DO")
        description.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        description.setReadOnly(True)

        descbox.addWidget(description)
        description.setStyleSheet("background-color: #e2dfdd; padding:5px; border-radius:7px; border: solid #bdbbb6; ")
        vbox.addLayout(descbox)
        self.stack5.setLayout(vbox)

    # ----- Entropy -----------------------------
    def stack6UI(self):
        vbox = QVBoxLayout(self)
        layout = QFormLayout()
        vbox.addLayout(layout)

        options = QLabel("Options")
        options.setStyleSheet("background-color: #FFCC33;")
        layout.addRow(options)

        descrip = QLabel("Description")
        descrip.setStyleSheet("background-color: #FFCC33;")
        layout.addRow(QLabel("\n"))
        layout.addRow(descrip)

        descbox = QtGui.QVBoxLayout()
        description = QTextEdit("TO WRITE")
        description.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        description.setReadOnly(True)

        descbox.addWidget(description)
        description.setStyleSheet("background-color: #e2dfdd; padding:5px; border-radius:7px; border: solid #bdbbb6; ")
        vbox.addLayout(descbox)
        self.stack6.setLayout(vbox)

    # ----- Erosion ------------------------------
    def stack7UI(self):
        vbox = QVBoxLayout(self)
        layout = QFormLayout()
        vbox.addLayout(layout)

        options = QLabel("Options")
        options.setStyleSheet("background-color: #FFCC33;")
        layout.addRow(options)

        descrip = QLabel("Description")
        descrip.setStyleSheet("background-color: #FFCC33;")
        layout.addRow(QLabel("\n"))
        layout.addRow(descrip)

        descbox = QtGui.QVBoxLayout()
        description = QTextEdit("TO WRITE")
        description.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        description.setReadOnly(True)

        descbox.addWidget(description)
        description.setStyleSheet("background-color: #e2dfdd; padding:5px; border-radius:7px; border: solid #bdbbb6; ")
        vbox.addLayout(descbox)
        self.stack7.setLayout(vbox)

    # ----- Linear combination ---------------------------
    def stack8UI(self):
        vbox = QVBoxLayout(self)
        layout = QFormLayout()
        vbox.addLayout(layout)

        options = QLabel("Options")
        options.setStyleSheet("background-color: #FFCC33;")
        layout.addRow(options)
        layout.addRow("option1", QLineEdit())
        layout.addRow("option2", QLineEdit())

        descrip = QLabel("Description")
        descrip.setStyleSheet("background-color: #FFCC33;")
        layout.addRow(QLabel("\n"))
        layout.addRow(descrip)

        descbox = QtGui.QVBoxLayout()
        description = QTextEdit("This algorithm makes the sum of a set of nifti files by associating a weight to each one of them (to caracterizes the importance)")
        description.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        description.setReadOnly(True)

        descbox.addWidget(description)
        description.setStyleSheet("background-color: #e2dfdd; padding:5px; border-radius:7px; border: solid #bdbbb6; ")
        vbox.addLayout(descbox)
        self.stack8.setLayout(vbox)

    # ----- Mean ---------------------------------
    def stack9UI(self):
        vbox = QVBoxLayout(self)
        layout = QFormLayout()
        vbox.addLayout(layout)

        options = QLabel("Options")
        options.setStyleSheet("background-color: #FFCC33;")
        layout.addRow(options)

        descrip = QLabel("Description")
        descrip.setStyleSheet("background-color: #FFCC33;")
        layout.addRow(QLabel("\n"))
        layout.addRow(descrip)

        descbox = QtGui.QVBoxLayout()
        description = QTextEdit("The Mean process averages a set of nifti files. The algorithm performs the sum for all voxels present in each file the divides the value obtained by the number of files")
        description.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        description.setReadOnly(True)

        descbox.addWidget(description)
        description.setStyleSheet("background-color: #e2dfdd; padding:5px; border-radius:7px; border: solid #bdbbb6; ")
        vbox.addLayout(descbox)
        self.stack9.setLayout(vbox)

    # ----- Normalization ------------------------------------
    def stack10UI(self):
        vbox = QVBoxLayout(self)
        layout = QFormLayout()
        vbox.addLayout(layout)

        options = QLabel("Options")
        options.setStyleSheet("background-color: #FFCC33;")
        layout.addRow(options)

        descrip = QLabel("Description")
        descrip.setStyleSheet("background-color: #FFCC33;")
        layout.addRow(QLabel("\n"))
        layout.addRow(descrip)

        descbox = QtGui.QVBoxLayout()
        description = QTextEdit("The normalization algorithm creates one nifti file result for each input nifti file. This algorithm create a file where the values for each voxel are between 0 and 1. Different ways exit to normalize a nifti file, you can select in the options panel the desired method")
        description.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        description.setReadOnly(True)

        descbox.addWidget(description)
        description.setStyleSheet("background-color: #e2dfdd; padding:5px; border-radius:7px; border: solid #bdbbb6; ")
        vbox.addLayout(descbox)
        self.stack10.setLayout(vbox)

    # ----- Substraction ------------------------------------
    def stack11UI(self):
        vbox = QVBoxLayout(self)
        layout = QFormLayout()
        vbox.addLayout(layout)

        options = QLabel("Options")
        options.setStyleSheet("background-color: #FFCC33;")
        layout.addRow(options)

        descrip = QLabel("Description")
        descrip.setStyleSheet("background-color: #FFCC33;")
        layout.addRow(QLabel("\n"))
        layout.addRow(descrip)

        descbox = QtGui.QVBoxLayout()
        description = QTextEdit("TO WRITE")
        description.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        description.setReadOnly(True)

        descbox.addWidget(description)
        description.setStyleSheet("background-color: #e2dfdd; padding:5px; border-radius:7px; border: solid #bdbbb6; ")
        vbox.addLayout(descbox)
        self.stack11.setLayout(vbox)

    # def stack2UI(self):
    #	layout = QFormLayout()
    #	sex = QHBoxLayout()
    #	sex.addWidget(QRadioButton("option1"))
    #	sex.addWidget(QRadioButton("option2"))
    #	layout.addRow(QLabel("blabla"),sex)
    #	layout.addRow("blabla",QLineEdit())
    #
    #	self.stack2.setLayout(layout)

    # def stack3UI(self):
    #	layout = QFormLayout()#QHBoxLayout()
    #	layout.addWidget(QLabel("option1"))
    #	layout.addWidget(QCheckBox("option2"))
    #	layout.addWidget(QCheckBox("option2"))
    #	self.stack3.setLayout(layout)

    def display(self, i):
        self.Stack.setCurrentIndex(i)

    # --------------------- Action for CALCULATE button -------------------
    def runCalculation(self):
        print("calculation in progress...")
        print currentUsableDataset
        algorithm = self.leftlist.selectedItems()[0].text()
        # extraction of arguments here
        #
        #  ... TO DO ...
        #
        arguments = []
        nifti_selected = []
        
        for collection in selected:
            for nifti in collection.nifimage_dict.values():
                nifti_selected.append(nifti.filename)
        
        if algorithm=="Mean":
            try:
                algorithm_result, output = run_calculation(algorithm, nifti_selected, arguments)
                self.console.setText(">>> \n"+output)
                QtGui.QMessageBox.information(self, "SUCCESS",
                                              "Algorithm " + algorithm + " correctly applicated on nifti(s) file(s)")
            except:
                QtGui.QMessageBox.warning(self, "ERROR",
                                          "Impossible to execute "+algorithm+" algorithm")
                                          
        if algorithm=="Linear combination":
            try:
                algorithm_result, output = run_calculation(algorithm, nifti_selected, arguments)
                QtGui.QMessageBox.information(self, "SUCCESS",
                                              "Algorithm " + algorithm + " correctly applicated on nifti(s) file(s)")
            except:
                QtGui.QMessageBox.warning(self, "ERROR",
                                          "Impossible to execute "+algorithm+" algorithm. Please check if you have correctly entering the coefficent list")
                                          
        if algorithm=="Boolean Intersection":
            try:
                algorithm_result, output = run_calculation(algorithm, nifti_selected, arguments)
                QtGui.QMessageBox.information(self, "SUCCESS",
                                              "Algorithm " + algorithm + " correctly applicated on nifti(s) file(s)")
            except:
                QtGui.QMessageBox.warning(self, "ERROR",
                                          "Impossible to execute "+algorithm+" algorithm")
        if algorithm=="Boolean Union":
            try:
                algorithm_result, output = run_calculation(algorithm, nifti_selected, arguments)
                QtGui.QMessageBox.information(self, "SUCCESS",
                                              "Algorithm " + algorithm + " correctly applicated on nifti(s) file(s)")
            except:
                QtGui.QMessageBox.warning(self, "ERROR",
                                          "Impossible to execute "+algorithm+" algorithm")
        if algorithm=="Normalization":
            try:
                algorithm_result, output = run_calculation(algorithm, nifti_selected, arguments)
                QtGui.QMessageBox.information(self, "SUCCESS",
                                              "Algorithm " + algorithm + " correctly applicated on nifti(s) file(s)")
            except:
                QtGui.QMessageBox.warning(self, "ERROR",
                                          "Impossible to execute "+algorithm+" algorithm")


