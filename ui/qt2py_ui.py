# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt2py.ui',
# licensing of 'qt2py.ui' applies.
#
# Created: Thu Oct  3 17:05:19 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(662, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(0, 0))
        Form.setMaximumSize(QtCore.QSize(662, 500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/res/qt2py.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setWindowOpacity(1.0)
        Form.setStyleSheet("")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(640, 500))
        self.tabWidget.setMaximumSize(QtCore.QSize(640, 500))
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(20, 20))
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setObjectName("tabWidget")
        self.pyqt5_tab = QtWidgets.QWidget()
        self.pyqt5_tab.setMinimumSize(QtCore.QSize(0, 0))
        self.pyqt5_tab.setObjectName("pyqt5_tab")
        self.frame = QtWidgets.QFrame(self.pyqt5_tab)
        self.frame.setGeometry(QtCore.QRect(9, 80, 621, 361))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lineEdit_filepath_pyqt = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_filepath_pyqt.setGeometry(QtCore.QRect(10, 30, 451, 31))
        self.lineEdit_filepath_pyqt.setStyleSheet("padding: 6px 12px;\n"
"font-size: 14;\n"
"color: #555;\n"
"background-color: #fff;\n"
"border: 1px solid #ccc;\n"
"border-radius: 8px")
        self.lineEdit_filepath_pyqt.setObjectName("lineEdit_filepath_pyqt")
        self.pushButton_Browse_pyqt = QtWidgets.QPushButton(self.frame)
        self.pushButton_Browse_pyqt.setGeometry(QtCore.QRect(470, 30, 151, 31))
        self.pushButton_Browse_pyqt.setMinimumSize(QtCore.QSize(0, 31))
        self.pushButton_Browse_pyqt.setStyleSheet("QPushButton{\n"
"font-size: 14;\n"
"color: #fff;\n"
"background-color: #428bca;\n"
"border: 1px solid #ccc;\n"
"border-radius: 4px;\n"
"border-color: #357ebd;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: #fff;\n"
"background-color: #3071a9;\n"
"border-color: #285e8e;\n"
"}")
        self.pushButton_Browse_pyqt.setObjectName("pushButton_Browse_pyqt")
        self.lineEdit_srcFile_pyqt = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_srcFile_pyqt.setGeometry(QtCore.QRect(10, 100, 261, 31))
        self.lineEdit_srcFile_pyqt.setStyleSheet("padding: 6px 12px;\n"
"font-size: 14;\n"
"color: #555;\n"
"background-color: #fff;\n"
"border: 1px solid #ccc;\n"
"border-radius: 8px")
        self.lineEdit_srcFile_pyqt.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_srcFile_pyqt.setClearButtonEnabled(False)
        self.lineEdit_srcFile_pyqt.setObjectName("lineEdit_srcFile_pyqt")
        self.pushButton_Generate_pyqt = QtWidgets.QPushButton(self.frame)
        self.pushButton_Generate_pyqt.setGeometry(QtCore.QRect(177, 170, 281, 101))
        self.pushButton_Generate_pyqt.setMinimumSize(QtCore.QSize(0, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(75)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setBold(True)
        self.pushButton_Generate_pyqt.setFont(font)
        self.pushButton_Generate_pyqt.setStyleSheet("QPushButton{\n"
"font-size: 14;\n"
"color: #fff;\n"
"background-color: #555aaa;\n"
"border: 1px solid #ccc;\n"
"border-radius: 25px;\n"
"border-color: #357ebd;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: #fff;\n"
"background-color: #3071a9;\n"
"border-color: #285e8e;\n"
"}")
        self.pushButton_Generate_pyqt.setObjectName("pushButton_Generate_pyqt")
        self.lineEdit_outFile_pyqt = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_outFile_pyqt.setGeometry(QtCore.QRect(360, 100, 261, 31))
        self.lineEdit_outFile_pyqt.setStyleSheet("padding: 6px 12px;\n"
"font-size: 14;\n"
"color: #555;\n"
"background-color: #fff;\n"
"border: 1px solid #ccc;\n"
"border-radius: 8px")
        self.lineEdit_outFile_pyqt.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_outFile_pyqt.setObjectName("lineEdit_outFile_pyqt")
        self.label_sourceFileName = QtWidgets.QLabel(self.frame)
        self.label_sourceFileName.setGeometry(QtCore.QRect(110, 290, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_sourceFileName.setFont(font)
        self.label_sourceFileName.setStyleSheet("color: #555;\n"
"\n"
"\n"
"")
        self.label_sourceFileName.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_sourceFileName.setObjectName("label_sourceFileName")
        self.label_targetFileName = QtWidgets.QLabel(self.frame)
        self.label_targetFileName.setGeometry(QtCore.QRect(340, 290, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_targetFileName.setFont(font)
        self.label_targetFileName.setStyleSheet("color: #555;\n"
"\n"
"\n"
"")
        self.label_targetFileName.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_targetFileName.setObjectName("label_targetFileName")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(290, 296, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #555;\n"
"\n"
"\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.compilerSelect = QtWidgets.QComboBox(self.pyqt5_tab)
        self.compilerSelect.setGeometry(QtCore.QRect(250, 20, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.compilerSelect.setFont(font)
        self.compilerSelect.setStyleSheet("padding: 6px 12px;\n"
"font-size: 14;\n"
"color: #555;\n"
"background-color: #fff;\n"
"border: 1px solid #ccc;\n"
"border-radius: 8px")
        self.compilerSelect.setObjectName("compilerSelect")
        self.compilerSelect.addItem("")
        self.compilerSelect.addItem("")
        self.tabWidget.addTab(self.pyqt5_tab, "")
        self.aboutTab = QtWidgets.QWidget()
        self.aboutTab.setObjectName("aboutTab")
        self.pushButton_github = QtWidgets.QToolButton(self.aboutTab)
        self.pushButton_github.setGeometry(QtCore.QRect(380, 200, 181, 171))
        self.pushButton_github.setStyleSheet("QToolButton{\n"
"padding: 6px 12px;\n"
"font-size: 14;\n"
"color: #555;\n"
"background-color: #fff;\n"
"border: 1px solid #ccc;\n"
"border-radius: 85px;\n"
"}\n"
"\n"
"QToolButton:Hover{\n"
"color: #fff;\n"
"background-color: #FF4040;\n"
"border-color: #285e8e;\n"
"}")
        self.pushButton_github.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/res/git.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_github.setIcon(icon1)
        self.pushButton_github.setIconSize(QtCore.QSize(300, 300))
        self.pushButton_github.setObjectName("pushButton_github")
        self.label_sourceFileName_2 = QtWidgets.QLabel(self.aboutTab)
        self.label_sourceFileName_2.setGeometry(QtCore.QRect(320, 400, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_sourceFileName_2.setFont(font)
        self.label_sourceFileName_2.setStyleSheet("color: #555;\n"
"\n"
"\n"
"")
        self.label_sourceFileName_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_sourceFileName_2.setObjectName("label_sourceFileName_2")
        self.pushButton_q2p = QtWidgets.QToolButton(self.aboutTab)
        self.pushButton_q2p.setGeometry(QtCore.QRect(30, 30, 181, 171))
        self.pushButton_q2p.setStyleSheet("QToolButton{\n"
"padding: 6px 12px;\n"
"font-size: 14;\n"
"color: #555;\n"
"background-color: #fff;\n"
"border: 1px solid #ccc;\n"
"border-radius: 85px;\n"
"}\n"
"\n"
"QToolButton:Hover{\n"
"color: #fff;\n"
"background-color: #409BFF;\n"
"border-color: #285e8e;\n"
"}")
        self.pushButton_q2p.setText("")
        self.pushButton_q2p.setIcon(icon)
        self.pushButton_q2p.setIconSize(QtCore.QSize(300, 300))
        self.pushButton_q2p.setObjectName("pushButton_q2p")
        self.label_sourceFileName_3 = QtWidgets.QLabel(self.aboutTab)
        self.label_sourceFileName_3.setGeometry(QtCore.QRect(0, 220, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_sourceFileName_3.setFont(font)
        self.label_sourceFileName_3.setStyleSheet("color: #555;\n"
"\n"
"\n"
"")
        self.label_sourceFileName_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_sourceFileName_3.setObjectName("label_sourceFileName_3")
        self.tabWidget.addTab(self.aboutTab, "")
        self.horizontalLayout.addWidget(self.tabWidget)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        self.compilerSelect.setCurrentIndex(0)
        QtCore.QObject.connect(self.lineEdit_outFile_pyqt, QtCore.SIGNAL("textChanged(QString)"), self.label_targetFileName.setText)
        QtCore.QObject.connect(self.lineEdit_srcFile_pyqt, QtCore.SIGNAL("textChanged(QString)"), self.label_sourceFileName.setText)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Qt2Py v1.0", None, -1))
        self.lineEdit_filepath_pyqt.setPlaceholderText(QtWidgets.QApplication.translate("Form", "File Path", None, -1))
        self.pushButton_Browse_pyqt.setText(QtWidgets.QApplication.translate("Form", "Browse", None, -1))
        self.lineEdit_srcFile_pyqt.setPlaceholderText(QtWidgets.QApplication.translate("Form", "QT *.Ui File Name", None, -1))
        self.pushButton_Generate_pyqt.setText(QtWidgets.QApplication.translate("Form", "Generate", None, -1))
        self.lineEdit_outFile_pyqt.setPlaceholderText(QtWidgets.QApplication.translate("Form", "Target *.py UI File Name", None, -1))
        self.label_sourceFileName.setText(QtWidgets.QApplication.translate("Form", "Source", None, -1))
        self.label_targetFileName.setText(QtWidgets.QApplication.translate("Form", "Target", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "=", None, -1))
        self.compilerSelect.setItemText(0, QtWidgets.QApplication.translate("Form", "PyQt5", None, -1))
        self.compilerSelect.setItemText(1, QtWidgets.QApplication.translate("Form", "PySide2", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pyqt5_tab), QtWidgets.QApplication.translate("Form", "Q2P Compiler", None, -1))
        self.label_sourceFileName_2.setText(QtWidgets.QApplication.translate("Form", "GitHub @lakshbhatnagar", None, -1))
        self.label_sourceFileName_3.setText(QtWidgets.QApplication.translate("Form", "v0.1", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.aboutTab), QtWidgets.QApplication.translate("Form", "About", None, -1))

from ui import q2p_rc
