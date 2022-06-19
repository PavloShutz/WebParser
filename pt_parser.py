from PyQt5 import QtCore, QtGui, QtWidgets
from get_response import get_links
from PyQt5.QtGui import QIcon


class UiForm:
    def setup_ui(self, form):
        form.setObjectName("Form")
        form.resize(640, 461)
        form.setStyleSheet("background-color: #024f21;")
        form.setWindowIcon(QIcon('icon.png'))
        self.gridLayout_2 = QtWidgets.QGridLayout(form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(form)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color:  #37d765 ;\n"
                                 "color: #fff;")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(form)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: white;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(form)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color:  #37d765 ;\n"
                                   "color: #fff;")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(form)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: white;")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(form)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
                                      "display: inline-block;\n"
                                      "  padding: 15px 25px;\n"
                                      "  cursor: pointer;\n"
                                      "  text-align: center;\n"
                                      "  text-decoration: none;\n"
                                      "  outline: none;\n"
                                      "  color: #fff;\n"
                                      "  background-color: #4CAF50;\n"
                                      "  border: none;\n"
                                      "  border-radius: 15px;\n"
                                      "  box-shadow: 0 9px #999;\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "background-color: #3e8e41\n"
                                      "}\n"
                                      "QPushButton:pressed{\n"
                                      "background-color: #3e8e41;\n"
                                      "  box-shadow: 0 5px #666;\n"
                                      "  transform: translateY(4px);\n"
                                      "}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.__insert_element)
        self.verticalLayout.addWidget(self.pushButton)
        self.listWidget = QtWidgets.QListWidget(form)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet("background-color: white;")
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.gridLayout_2.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.re_translate_ui(form)
        QtCore.QMetaObject.connectSlotsByName(form)

    def re_translate_ui(self, form):
        _translate = QtCore.QCoreApplication.translate
        form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Insert link"))
        self.label_2.setText(_translate("Form", "Insert amount of links"))
        self.pushButton.setText(_translate("Form", "Get links"))

    def __insert_element(self) -> None:
        self.listWidget.clear()
        url = self.lineEdit.text()
        links = get_links(url)
        if links == 'Bad response!':
            self.listWidget.addItem('Bad response!')
            return
        if links == 'No internet connection!':
            self.listWidget.addItem('No internet connection!')
            return
        if not self.lineEdit_2.text().split():
            for i in links:
                self.listWidget.addItem(i)
            return
        else:
            try:
                for i in range(int(self.lineEdit_2.text())):
                    try:
                        self.listWidget.addItem(links[i])
                    except IndexError:
                        break
            except ValueError:
                self.listWidget.addItem('Amount must be a number!')
            return


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = UiForm()
    ui.setup_ui(Form)
    Form.show()
    sys.exit(app.exec_())
