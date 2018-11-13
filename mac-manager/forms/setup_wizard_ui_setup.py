# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/setup_wizard.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_IslandSetupWizzard(object):
    def setupUi(self, IslandSetupWizzard):
        IslandSetupWizzard.setObjectName("IslandSetupWizzard")
        IslandSetupWizzard.setWindowModality(QtCore.Qt.WindowModal)
        IslandSetupWizzard.resize(712, 525)
        IslandSetupWizzard.setMinimumSize(QtCore.QSize(712, 525))
        IslandSetupWizzard.setModal(True)
        IslandSetupWizzard.setWizardStyle(QtWidgets.QWizard.MacStyle)
        IslandSetupWizzard.setOptions(QtWidgets.QWizard.NoCancelButton|QtWidgets.QWizard.NoDefaultButton)
        self.page_vbox_install_1 = QtWidgets.QWizardPage()
        self.page_vbox_install_1.setObjectName("page_vbox_install_1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.page_vbox_install_1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.page_vbox_install_1)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #011e4c")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.textBrowser = QtWidgets.QTextBrowser(self.page_vbox_install_1)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.button_path_to_vboxmanage = QtWidgets.QPushButton(self.page_vbox_install_1)
        self.button_path_to_vboxmanage.setEnabled(False)
        self.button_path_to_vboxmanage.setVisible(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/search"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_path_to_vboxmanage.setIcon(icon)
        self.button_path_to_vboxmanage.setIconSize(QtCore.QSize(32, 32))
        self.button_path_to_vboxmanage.setObjectName("button_path_to_vboxmanage")
        self.horizontalLayout.addWidget(self.button_path_to_vboxmanage)
        self.button_install_vbox = QtWidgets.QPushButton(self.page_vbox_install_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_install_vbox.sizePolicy().hasHeightForWidth())
        self.button_install_vbox.setSizePolicy(sizePolicy)
        self.button_install_vbox.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/download"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_install_vbox.setIcon(icon1)
        self.button_install_vbox.setIconSize(QtCore.QSize(32, 32))
        self.button_install_vbox.setObjectName("button_install_vbox")
        self.horizontalLayout.addWidget(self.button_install_vbox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        IslandSetupWizzard.addPage(self.page_vbox_install_1)
        self.page_vm_install_2 = QtWidgets.QWizardPage()
        self.page_vm_install_2.setObjectName("page_vm_install_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page_vm_install_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.page_vm_install_2)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #011e4c")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.vm_install_output_console = QtWidgets.QTextBrowser(self.page_vm_install_2)
        self.vm_install_output_console.setObjectName("vm_install_output_console")
        self.verticalLayout_2.addWidget(self.vm_install_output_console)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.page_vm_install_2)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.local_port = QtWidgets.QLineEdit(self.page_vm_install_2)
        self.local_port.setObjectName("local_port")
        self.horizontalLayout_4.addWidget(self.local_port)
        self.port_forwarding_enabled = QtWidgets.QCheckBox(self.page_vm_install_2)
        self.port_forwarding_enabled.setChecked(True)
        self.port_forwarding_enabled.setObjectName("port_forwarding_enabled")
        self.horizontalLayout_4.addWidget(self.port_forwarding_enabled)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.page_vm_install_2)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.data_folder_path = QtWidgets.QLineEdit(self.page_vm_install_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.data_folder_path.setFont(font)
        self.data_folder_path.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.data_folder_path.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.data_folder_path.setReadOnly(True)
        self.data_folder_path.setObjectName("data_folder_path")
        self.horizontalLayout_3.addWidget(self.data_folder_path)
        self.button_select_data_path = QtWidgets.QPushButton(self.page_vm_install_2)
        self.button_select_data_path.setObjectName("button_select_data_path")
        self.horizontalLayout_3.addWidget(self.button_select_data_path)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.button_import_ova = QtWidgets.QPushButton(self.page_vm_install_2)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/import"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_import_ova.setIcon(icon2)
        self.button_import_ova.setIconSize(QtCore.QSize(32, 32))
        self.button_import_ova.setObjectName("button_import_ova")
        self.horizontalLayout_2.addWidget(self.button_import_ova)
        self.button_install_islands = QtWidgets.QPushButton(self.page_vm_install_2)
        self.button_install_islands.setIcon(icon1)
        self.button_install_islands.setIconSize(QtCore.QSize(32, 32))
        self.button_install_islands.setObjectName("button_install_islands")
        self.horizontalLayout_2.addWidget(self.button_install_islands)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        IslandSetupWizzard.addPage(self.page_vm_install_2)
        self.page_complete_3 = QtWidgets.QWizardPage()
        self.page_complete_3.setObjectName("page_complete_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page_complete_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.page_complete_3)
        font = QtGui.QFont()
        font.setPointSize(35)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: green;")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.label_4 = QtWidgets.QLabel(self.page_complete_3)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        IslandSetupWizzard.addPage(self.page_complete_3)

        self.retranslateUi(IslandSetupWizzard)
        QtCore.QMetaObject.connectSlotsByName(IslandSetupWizzard)

    def retranslateUi(self, IslandSetupWizzard):
        _translate = QtCore.QCoreApplication.translate
        IslandSetupWizzard.setWindowTitle(_translate("IslandSetupWizzard", "Wizard"))
        self.label.setText(_translate("IslandSetupWizzard", "Step 1 - Virtualbox setup"))
        self.textBrowser.setHtml(_translate("IslandSetupWizzard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.button_path_to_vboxmanage.setText(_translate("IslandSetupWizzard", "Path to vboxmanage "))
        self.button_install_vbox.setText(_translate("IslandSetupWizzard", "Download and isntall Virtualbox"))
        self.label_2.setText(_translate("IslandSetupWizzard", "Step 2 - Islands virtual machine setup"))
        self.label_6.setText(_translate("IslandSetupWizzard", "Island local access port: "))
        self.local_port.setText(_translate("IslandSetupWizzard", "4000"))
        self.port_forwarding_enabled.setText(_translate("IslandSetupWizzard", "Enabled"))
        self.label_5.setText(_translate("IslandSetupWizzard", "Data folder: "))
        self.data_folder_path.setText(_translate("IslandSetupWizzard", "~/islandsData"))
        self.button_select_data_path.setText(_translate("IslandSetupWizzard", "Select"))
        self.button_import_ova.setText(_translate("IslandSetupWizzard", "Import Islands VM"))
        self.button_install_islands.setText(_translate("IslandSetupWizzard", "Install Islands VM"))
        self.label_3.setText(_translate("IslandSetupWizzard", "Setup complete!"))
        self.label_4.setText(_translate("IslandSetupWizzard", "Press \"Done\" to exit setup wizzard"))

import forms.resources_rc
