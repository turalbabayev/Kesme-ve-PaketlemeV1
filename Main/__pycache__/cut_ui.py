# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Aydin\Desktop\Kesme-ve-Paketleme-main\Orginal\__pycache__\cut.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1167, 723)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1167, 723))
        MainWindow.setMaximumSize(QtCore.QSize(1167, 723))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 1151, 741))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 60, 821, 381))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.matplotlib = QtWidgets.QWidget(self.verticalLayoutWidget)
        self.matplotlib.setObjectName("matplotlib")
        self.verticalLayout.addWidget(self.matplotlib)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(840, 60, 291, 261))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lblYontem = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblYontem.sizePolicy().hasHeightForWidth())
        self.lblYontem.setSizePolicy(sizePolicy)
        self.lblYontem.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblYontem.setAutoFillBackground(False)
        self.lblYontem.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblYontem.setObjectName("lblYontem")
        self.verticalLayout_2.addWidget(self.lblYontem)
        self.btnNextFit = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnNextFit.sizePolicy().hasHeightForWidth())
        self.btnNextFit.setSizePolicy(sizePolicy)
        self.btnNextFit.setObjectName("btnNextFit")
        self.verticalLayout_2.addWidget(self.btnNextFit)
        self.btnGenetic = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnGenetic.sizePolicy().hasHeightForWidth())
        self.btnGenetic.setSizePolicy(sizePolicy)
        self.btnGenetic.setObjectName("btnGenetic")
        self.verticalLayout_2.addWidget(self.btnGenetic)
        self.btnEkYontem = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnEkYontem.sizePolicy().hasHeightForWidth())
        self.btnEkYontem.setSizePolicy(sizePolicy)
        self.btnEkYontem.setObjectName("btnEkYontem")
        self.verticalLayout_2.addWidget(self.btnEkYontem)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 450, 821, 171))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.textBoxMessage = QtWidgets.QTextEdit(self.verticalLayoutWidget_3)
        self.textBoxMessage.setPlaceholderText("")
        self.textBoxMessage.setObjectName("textBoxMessage")
        self.verticalLayout_3.addWidget(self.textBoxMessage)
        self.lblBaslik = QtWidgets.QLabel(self.tab)
        self.lblBaslik.setGeometry(QtCore.QRect(410, -10, 801, 81))
        self.lblBaslik.setScaledContents(False)
        self.lblBaslik.setObjectName("lblBaslik")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(840, 350, 291, 271))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lblIslem = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblIslem.sizePolicy().hasHeightForWidth())
        self.lblIslem.setSizePolicy(sizePolicy)
        self.lblIslem.setObjectName("lblIslem")
        self.verticalLayout_4.addWidget(self.lblIslem)
        self.btnVeriSec = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnVeriSec.sizePolicy().hasHeightForWidth())
        self.btnVeriSec.setSizePolicy(sizePolicy)
        self.btnVeriSec.setStyleSheet("\n"
"image: url(:/newPrefix/plus_50px.png);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/plus_50px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnVeriSec.setIcon(icon)
        self.btnVeriSec.setObjectName("btnVeriSec")
        self.verticalLayout_4.addWidget(self.btnVeriSec)
        self.btnSVGKaydet = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSVGKaydet.sizePolicy().hasHeightForWidth())
        self.btnSVGKaydet.setSizePolicy(sizePolicy)
        self.btnSVGKaydet.setObjectName("btnSVGKaydet")
        self.verticalLayout_4.addWidget(self.btnSVGKaydet)
        self.btnSonucGoruntule = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSonucGoruntule.sizePolicy().hasHeightForWidth())
        self.btnSonucGoruntule.setSizePolicy(sizePolicy)
        self.btnSonucGoruntule.setObjectName("btnSonucGoruntule")
        self.verticalLayout_4.addWidget(self.btnSonucGoruntule)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1167, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Kesme ve Paketleme Problem Arayüzü"))
        self.lblYontem.setText(_translate("MainWindow", "Yöntemler"))
        self.btnNextFit.setText(_translate("MainWindow", "Next-Fit Yöntemi"))
        self.btnGenetic.setText(_translate("MainWindow", "Genetik Algoritma"))
        self.btnEkYontem.setText(_translate("MainWindow", "Ek Yöntem"))
        self.lblBaslik.setText(_translate("MainWindow", "Kesme ve Paketleme Problemi Uygulama Arayüzü"))
        self.lblIslem.setText(_translate("MainWindow", "İşlemler"))
        self.btnVeriSec.setText(_translate("MainWindow", "Veri Seç"))
        self.btnSVGKaydet.setText(_translate("MainWindow", "SVG Olarak Kaydet"))
        self.btnSonucGoruntule.setText(_translate("MainWindow", "Sonuçları Görüntüle"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Ana Sayfa"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Hakkımızda"))
import icons_rc
