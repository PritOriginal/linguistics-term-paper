# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QPlainTextEdit, QPushButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(839, 706)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.btnOpenIR = QPushButton(self.centralwidget)
        self.btnOpenIR.setObjectName(u"btnOpenIR")

        self.horizontalLayout_7.addWidget(self.btnOpenIR)

        self.btnGenerate = QPushButton(self.centralwidget)
        self.btnGenerate.setObjectName(u"btnGenerate")

        self.horizontalLayout_7.addWidget(self.btnGenerate)


        self.gridLayout.addLayout(self.horizontalLayout_7, 2, 2, 1, 1)

        self.plainTextIR = QPlainTextEdit(self.centralwidget)
        self.plainTextIR.setObjectName(u"plainTextIR")
        self.plainTextIR.setReadOnly(True)

        self.gridLayout.addWidget(self.plainTextIR, 8, 0, 1, 1)

        self.labelSelectedIRFile = QLabel(self.centralwidget)
        self.labelSelectedIRFile.setObjectName(u"labelSelectedIRFile")

        self.gridLayout.addWidget(self.labelSelectedIRFile, 1, 2, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label, 7, 0, 1, 1)

        self.plainTextEditPascal = QPlainTextEdit(self.centralwidget)
        self.plainTextEditPascal.setObjectName(u"plainTextEditPascal")

        self.gridLayout.addWidget(self.plainTextEditPascal, 6, 2, 3, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 5, 2, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.labelSelectedOriginalFile = QLabel(self.centralwidget)
        self.labelSelectedOriginalFile.setObjectName(u"labelSelectedOriginalFile")

        self.horizontalLayout_2.addWidget(self.labelSelectedOriginalFile)


        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.btnOpenOriginal = QPushButton(self.centralwidget)
        self.btnOpenOriginal.setObjectName(u"btnOpenOriginal")

        self.horizontalLayout_5.addWidget(self.btnOpenOriginal)

        self.btnSaveOriginal = QPushButton(self.centralwidget)
        self.btnSaveOriginal.setObjectName(u"btnSaveOriginal")

        self.horizontalLayout_5.addWidget(self.btnSaveOriginal)


        self.gridLayout.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)

        self.plainTextOriginal = QPlainTextEdit(self.centralwidget)
        self.plainTextOriginal.setObjectName(u"plainTextOriginal")

        self.gridLayout.addWidget(self.plainTextOriginal, 6, 0, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 5, 0, 1, 1)

        self.btnSavePascal = QPushButton(self.centralwidget)
        self.btnSavePascal.setObjectName(u"btnSavePascal")

        self.gridLayout.addWidget(self.btnSavePascal, 3, 2, 1, 1)

        self.btnDisassemble = QPushButton(self.centralwidget)
        self.btnDisassemble.setObjectName(u"btnDisassemble")

        self.gridLayout.addWidget(self.btnDisassemble, 3, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 839, 30))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0445\u043d\u0430\u0442\u0435\u0435\u0432 \u0421.\u0410. | \u0422\u0440\u0430\u043d\u0441\u043b\u044f\u0442\u043e\u0440 - Pascal", None))
        self.btnOpenIR.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0444\u0430\u0439\u043b", None))
        self.btnGenerate.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0433\u0435\u043d\u0435\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.labelSelectedIRFile.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u043d\u043d\u044b\u0439 \u0444\u0430\u0439\u043b: \u0424\u0430\u0439\u043b \u043d\u0435 \u0432\u044b\u0431\u0440\u0430\u043d", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0435\u0435 \u043f\u0440\u0435\u0434\u0441\u0442\u0430\u0432\u043b\u0435\u043d\u0438\u0435 (\u041f\u043e\u0441\u0442\u0444\u0438\u043a\u0441\u043d\u0430\u044f \u0437\u0430\u043f\u0438\u0441\u044c)", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Pascal", None))
        self.labelSelectedOriginalFile.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u043d\u043d\u044b\u0439 \u0444\u0430\u0439\u043b: \u0424\u0430\u0439\u043b \u043d\u0435 \u0432\u044b\u0431\u0440\u0430\u043d", None))
        self.btnOpenOriginal.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0444\u0430\u0439\u043b", None))
        self.btnSaveOriginal.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0440\u0438\u0433\u0438\u043d\u0430\u043b", None))
        self.btnSavePascal.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0441\u0433\u0435\u043d\u0435\u0440\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0439", None))
        self.btnDisassemble.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u043e\u0431\u0440\u0430\u0442\u044c", None))
    # retranslateUi

