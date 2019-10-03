try:
    from PySide2.QtGui import *
    from PySide2.QtCore import *
    from PySide2.QtWidgets import *
except:
     from PyQt5.QtGui import *
     from PyQt5.QtCore import *
     from PyQt5.QtWidgets import *
import sys
import os
import subprocess
import webbrowser
from ui import qt2py_ui

# Creating GUI
class Q2P_Window(QWidget, qt2py_ui.Ui_Form):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)

        ##############################
        ##############################
        #     P2P Compiler    #
        ##############################
        ##############################

        # Source File Browser
        self.pushButton_Browse_pyqt.clicked.connect(self.sourceBrowser)

        # Generate File
        self.pushButton_Generate_pyqt.clicked.connect(self.pyside_generate)

        # Github Page
        self.pushButton_github.clicked.connect(self.openGithub)

    def openGithub(self):
        webbrowser.open("https://github.com/lakshbhatnagar/qt2py")

    def sourceBrowser(self):
        options = QFileDialog.Options()
        self.filename = QFileDialog.getExistingDirectory(self, "Open Directory")
        self.lineEdit_filepath_pyqt.setText(self.filename)

    def pyside_generate(self):
        # Store Source Qt Ui File
        self.getSourceFileName = self.label_sourceFileName.text()

        # Store Save Python Qt Ui File
        self.getOutFileName = self.label_targetFileName.text()

        # Store File Path
        self.getFilePath = self.lineEdit_filepath_pyqt.text()

        # Export Converted File
        self.export_Q2P_pyqt()

    def export_Q2P_pyqt(self):
        currentID = str(self.compilerSelect.currentIndex())
        print(currentID)

        self.currentCompiler = ""

        if(currentID == "0"):
            self.currentCompiler = "pyuic5"
        else:
            self.currentCompiler = "pyside2-uic"


        print(self.currentCompiler)


        # Creating temp file for data
        tempFile = open(file="tmp.bat", mode='w')

        # Change Compiler
        #self.compilerSelect.currentIndex()

        # Write data to temp file
        writelines = "cd " + self.getFilePath + "\n" + self.currentCompiler + " " + self.getSourceFileName + " -o " + self.getOutFileName
        tempFile.writelines(writelines)
        tempFile.close()

        # Run Command
        subprocess.call([r'tmp.bat'])

        # Delete Temp File
        os.remove(tempFile.name)

        #Debug
        #print("Source = " + self.getSourceFileName + "\n" + " Out = " + self.getOutFileName + "\n" + "File Path = " + self.getFilePath)

app = QApplication(sys.argv)
window = Q2P_Window()
window.show()
app.exec_()
