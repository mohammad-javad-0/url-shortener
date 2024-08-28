from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox
import requests


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(684, 455)
        MainWindow.setStyleSheet('''
        background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, 
        stop:0.410112 rgba(200, 234, 0, 10), stop:1 rgba(25, 185, 225, 225));
        color:white
        ''')
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # create label header project
        # create font for header
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(17)
        font.setItalic(True)

        self.header = QtWidgets.QLabel(parent=self.centralwidget)
        self.header.setGeometry(QtCore.QRect(182, 60, 320, 50))
        self.header.setFont(font)
        self.header.setStyleSheet("background-color:None;")
        self.header.setCursor(QtCore.Qt.CursorShape.ForbiddenCursor)
        self.header.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.header.setObjectName("header")

        # create font for labels and line edit
        font = QtGui.QFont("Arial")
        font.setPointSize(12)
        font.setBold(True)

        # create url and result url labels and wait label
        self.enter_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.enter_label.setGeometry(QtCore.QRect(40, 145, 90, 30))
        self.enter_label.setFont(font)
        self.enter_label.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ForbiddenCursor))
        self.enter_label.setStyleSheet("background-color: None;")
        self.enter_label.setObjectName("enter_label")

        self.result_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.result_label.setGeometry(QtCore.QRect(40, 250, 90, 30))
        self.result_label.setFont(font)
        self.result_label.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ForbiddenCursor))
        self.result_label.setStyleSheet("background-color: None;")
        self.result_label.setObjectName("result_label")

        self.wait_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.wait_label.setGeometry(QtCore.QRect(217, 350, 250, 30))
        self.wait_label.setFont(font)
        self.wait_label.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ForbiddenCursor))
        self.wait_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.wait_label.setStyleSheet("background-color: None;color:black;")
        self.wait_label.setHidden(True)
        self.wait_label.setObjectName("wait_label")

        # create url line edit and result url text browser
        font.setBold(False)

        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(130, 145, 520, 30))
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color:black;")
        self.lineEdit.setObjectName("lineEdit")

        self.textBrowser = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(130, 250, 520, 30))
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("background-color:black;")
        self.textBrowser.setObjectName("textBrowser")

        # create push button
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(254, 350, 141, 31))
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton.setStyleSheet('''
        QPushButton {
        color: qlineargradient(spread:repeat, x1:0.171875, y1:0, x2:1, y2:0.528182,
        stop:0.304688 rgba(170, 255, 255, 255), stop:0.710938 rgba(255, 255, 255, 255));
        border:3px solid black;}
        QPushButton:hover {color:black;}
        ''')
        self.pushButton.setObjectName("pushButton")
        self.pushButton.pressed.connect(lambda: self.wait_label.setHidden(False) or self.pushButton.setHidden(True))
        self.pushButton.clicked.connect(self.change_url)


        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "URL Shortener"))
        self.result_label.setText(_translate("MainWindow", "Result URL"))
        self.enter_label.setText(_translate("MainWindow", "Enter URL"))
        self.wait_label.setText(_translate("MainWindow", "Shortening the link. Please wait"))
        self.pushButton.setText(_translate("MainWindow", "Short URL"))
        self.header.setText(_translate("MainWindow", "Long url   →   Short url"))

    def change_url(self):
        try:
            url = self.lineEdit.text()
            api = f"https://ulvis.net/API/write/get?url={url}"
            print(api)
            req = requests.get(api)
            res = req.json()
            print(res)
            if not res["success"]:
                raise ValueError(res["error"]["msg"])
            self.textBrowser.append(res["data"]["url"])

        except Exception as err:
            msgbox = QMessageBox()
            QMessageBox.critical(msgbox, "Error", str(err))
        finally:
            self.pushButton.setHidden(False)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
