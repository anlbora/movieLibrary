from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_logInPage(object):

    def setupUi(self, logInPage):
        logInPage.setObjectName("logInPage")
        logInPage.setWindowModality(QtCore.Qt.ApplicationModal)
        logInPage.resize(800, 600)
        logInPage.setMinimumSize(QtCore.QSize(800, 600))
        logInPage.setMaximumSize(QtCore.QSize(800, 600))
        font = QtGui.QFont()
        font.setPointSize(12)
        logInPage.setFont(font)
        logInPage.setAutoFillBackground(True)
        self.groupBox = QtWidgets.QGroupBox(logInPage)
        self.groupBox.setGeometry(QtCore.QRect(410, 2, 381, 311))
        self.groupBox.setObjectName("groupBox")
        self.formLayout_4 = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setObjectName("label_10")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.signup_name = QtWidgets.QLineEdit(self.groupBox)
        self.signup_name.setFrame(False)
        self.signup_name.setObjectName("signup_name")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.signup_name)
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setObjectName("label_11")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.signup_surname = QtWidgets.QLineEdit(self.groupBox)
        self.signup_surname.setFrame(False)
        self.signup_surname.setObjectName("signup_surname")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.signup_surname)
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setObjectName("label_12")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.signup_age = QtWidgets.QLineEdit(self.groupBox)
        self.signup_age.setFrame(False)
        self.signup_age.setObjectName("signup_age")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.signup_age)
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setObjectName("label_13")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.signup_username = QtWidgets.QLineEdit(self.groupBox)
        self.signup_username.setFrame(False)
        self.signup_username.setObjectName("signup_username")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.signup_username)
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        self.label_14.setObjectName("label_14")
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.signup_password = QtWidgets.QLineEdit(self.groupBox)
        self.signup_password.setFrame(False)
        self.signup_password.setObjectName("signup_password")
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.signup_password)
        self.label_15 = QtWidgets.QLabel(self.groupBox)
        self.label_15.setObjectName("label_15")
        self.formLayout_4.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.signup_email = QtWidgets.QLineEdit(self.groupBox)
        self.signup_email.setFrame(False)
        self.signup_email.setObjectName("signup_email")
        self.formLayout_4.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.signup_email)
        self.signup_btn = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.signup_btn.setFont(font)
        self.signup_btn.setObjectName("signup_btn")
        self.formLayout_4.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.signup_btn)
        self.groupBox_2 = QtWidgets.QGroupBox(logInPage)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 0, 391, 161))
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox_2)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.login_username = QtWidgets.QLineEdit(self.groupBox_2)
        self.login_username.setFrame(False)
        self.login_username.setObjectName("login_username")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.login_username)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.login_password = QtWidgets.QLineEdit(self.groupBox_2)
        self.login_password.setFrame(False)
        self.login_password.setObjectName("login_password")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.login_password)
        self.login_btn = QtWidgets.QPushButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.login_btn.setFont(font)
        self.login_btn.setObjectName("login_btn")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.login_btn)
        self.groupBox_3 = QtWidgets.QGroupBox(logInPage)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 160, 391, 241))
        self.groupBox_3.setObjectName("groupBox_3")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBox_3)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.reset_username = QtWidgets.QLineEdit(self.groupBox_3)
        self.reset_username.setFrame(False)
        self.reset_username.setObjectName("reset_username")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.reset_username)
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.reset_email = QtWidgets.QLineEdit(self.groupBox_3)
        self.reset_email.setFrame(False)
        self.reset_email.setObjectName("reset_email")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.reset_email)
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.reset_newpassword = QtWidgets.QLineEdit(self.groupBox_3)
        self.reset_newpassword.setFrame(False)
        self.reset_newpassword.setObjectName("reset_newpassword")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.reset_newpassword)
        self.reset_btn = QtWidgets.QPushButton(self.groupBox_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.reset_btn.setFont(font)
        self.reset_btn.setObjectName("reset_btn")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.reset_btn)
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.reset_password = QtWidgets.QLineEdit(self.groupBox_3)
        self.reset_password.setFrame(False)
        self.reset_password.setObjectName("reset_password")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.reset_password)
        self.groupBox_4 = QtWidgets.QGroupBox(logInPage)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 400, 391, 191))
        self.groupBox_4.setObjectName("groupBox_4")
        self.formLayout_3 = QtWidgets.QFormLayout(self.groupBox_4)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_7 = QtWidgets.QLabel(self.groupBox_4)
        self.label_7.setObjectName("label_7")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.delete_username = QtWidgets.QLineEdit(self.groupBox_4)
        self.delete_username.setFrame(False)
        self.delete_username.setObjectName("delete_username")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.delete_username)
        self.label_8 = QtWidgets.QLabel(self.groupBox_4)
        self.label_8.setObjectName("label_8")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.delete_password = QtWidgets.QLineEdit(self.groupBox_4)
        self.delete_password.setFrame(False)
        self.delete_password.setObjectName("delete_password")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.delete_password)
        self.label_9 = QtWidgets.QLabel(self.groupBox_4)
        self.label_9.setObjectName("label_9")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.delete_email = QtWidgets.QLineEdit(self.groupBox_4)
        self.delete_email.setFrame(False)
        self.delete_email.setObjectName("delete_email")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.delete_email)
        self.delete_btn = QtWidgets.QPushButton(self.groupBox_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.delete_btn.setFont(font)
        self.delete_btn.setObjectName("delete_btn")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.delete_btn)
        self.calendarWidget = QtWidgets.QCalendarWidget(logInPage)
        self.calendarWidget.setGeometry(QtCore.QRect(410, 325, 381, 261))
        self.calendarWidget.setObjectName("calendarWidget")

        self.retranslateUi(logInPage)
        QtCore.QMetaObject.connectSlotsByName(logInPage)

    def retranslateUi(self, logInPage):
        _translate = QtCore.QCoreApplication.translate
        logInPage.setWindowTitle(_translate("logInPage", "Welcome to Movie Library"))
        self.groupBox.setTitle(_translate("logInPage", "Sign Up"))
        self.label_10.setText(_translate("logInPage", "Name:"))
        self.label_11.setText(_translate("logInPage", "Surname:"))
        self.label_12.setText(_translate("logInPage", "Age:"))
        self.label_13.setText(_translate("logInPage", "Username:"))
        self.label_14.setText(_translate("logInPage", "Password:"))
        self.label_15.setText(_translate("logInPage", "Email:"))
        self.signup_btn.setText(_translate("logInPage", "Sign Up"))
        self.groupBox_2.setTitle(_translate("logInPage", "Log In"))
        self.label.setText(_translate("logInPage", "Username:"))
        self.label_2.setText(_translate("logInPage", "Password:"))
        self.login_btn.setText(_translate("logInPage", "Log In"))
        self.groupBox_3.setTitle(_translate("logInPage", "Reset Password"))
        self.label_3.setText(_translate("logInPage", "Username:"))
        self.label_4.setText(_translate("logInPage", "Email:"))
        self.label_5.setText(_translate("logInPage", "New Password:"))
        self.reset_btn.setText(_translate("logInPage", "Reset my Password"))
        self.label_6.setText(_translate("logInPage", "New Password:"))
        self.groupBox_4.setTitle(_translate("logInPage", "Delete User"))
        self.label_7.setText(_translate("logInPage", "Username:"))
        self.label_8.setText(_translate("logInPage", "Password:"))
        self.label_9.setText(_translate("logInPage", "Email:"))
        self.delete_btn.setText(_translate("logInPage", "Delete my Account"))
