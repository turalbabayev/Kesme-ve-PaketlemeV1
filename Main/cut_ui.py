# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Aydin\Desktop\Kesme-ve-Paketleme-main\Orginal\cut.ui'
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\Aydin\\Desktop\\Kesme-ve-Paketleme-main\\Orginal\\../../Kesme ve Paketleme/Orginal/icons/WhatsApp Image 2023-11-27 at 22.01.04.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 1151, 741))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tabWidget.setFont(font)
        self.tabWidget.setMouseTracking(False)
        self.tabWidget.setTabletTracking(False)
        self.tabWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
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
        self.matplotlib.setEnabled(True)
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
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblYontem.setFont(font)
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
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btnNextFit.setFont(font)
        self.btnNextFit.setObjectName("btnNextFit")
        self.verticalLayout_2.addWidget(self.btnNextFit)
        self.btnGenetic = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnGenetic.sizePolicy().hasHeightForWidth())
        self.btnGenetic.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btnGenetic.setFont(font)
        self.btnGenetic.setObjectName("btnGenetic")
        self.verticalLayout_2.addWidget(self.btnGenetic)
        self.btnGreedy = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnGreedy.sizePolicy().hasHeightForWidth())
        self.btnGreedy.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btnGreedy.setFont(font)
        self.btnGreedy.setObjectName("btnGreedy")
        self.verticalLayout_2.addWidget(self.btnGreedy)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 450, 821, 183))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.textBoxMessage = QtWidgets.QTextEdit(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.textBoxMessage.setFont(font)
        self.textBoxMessage.setPlaceholderText("")
        self.textBoxMessage.setObjectName("textBoxMessage")
        self.verticalLayout_3.addWidget(self.textBoxMessage)
        self.progressBar = QtWidgets.QProgressBar(self.verticalLayoutWidget_3)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_3.addWidget(self.progressBar)
        self.lblBaslik = QtWidgets.QLabel(self.tab)
        self.lblBaslik.setGeometry(QtCore.QRect(350, -10, 461, 81))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lblBaslik.setFont(font)
        self.lblBaslik.setMouseTracking(False)
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
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblIslem.setFont(font)
        self.lblIslem.setObjectName("lblIslem")
        self.verticalLayout_4.addWidget(self.lblIslem)
        self.btnVeriSec = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnVeriSec.sizePolicy().hasHeightForWidth())
        self.btnVeriSec.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btnVeriSec.setFont(font)
        self.btnVeriSec.setStyleSheet("\n"
"image: url(:/newPrefix/plus_50px.png);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("c:\\Users\\Aydin\\Desktop\\Kesme-ve-Paketleme-main\\Orginal\\../../Kesme ve Paketleme/Orginal/icons/plus_50px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnVeriSec.setIcon(icon1)
        self.btnVeriSec.setObjectName("btnVeriSec")
        self.verticalLayout_4.addWidget(self.btnVeriSec)
        self.btnSaveSVG = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSaveSVG.sizePolicy().hasHeightForWidth())
        self.btnSaveSVG.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btnSaveSVG.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("c:\\Users\\Aydin\\Desktop\\Kesme-ve-Paketleme-main\\Orginal\\../../Kesme ve Paketleme/Orginal/icons/mms_50px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSaveSVG.setIcon(icon2)
        self.btnSaveSVG.setObjectName("btnSaveSVG")
        self.verticalLayout_4.addWidget(self.btnSaveSVG)
        self.btnSonucGoruntule = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSonucGoruntule.sizePolicy().hasHeightForWidth())
        self.btnSonucGoruntule.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btnSonucGoruntule.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("c:\\Users\\Aydin\\Desktop\\Kesme-ve-Paketleme-main\\Orginal\\../../Kesme ve Paketleme/Orginal/icons/eye.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSonucGoruntule.setIcon(icon3)
        self.btnSonucGoruntule.setObjectName("btnSonucGoruntule")
        self.verticalLayout_4.addWidget(self.btnSonucGoruntule)
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.listWidget = QtWidgets.QListWidget(self.tab_3)
        self.listWidget.setGeometry(QtCore.QRect(10, 30, 821, 211))
        self.listWidget.setObjectName("listWidget")
        self.lblIslem_2 = QtWidgets.QLabel(self.tab_3)
        self.lblIslem_2.setGeometry(QtCore.QRect(10, 10, 71, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblIslem_2.sizePolicy().hasHeightForWidth())
        self.lblIslem_2.setSizePolicy(sizePolicy)
        self.lblIslem_2.setObjectName("lblIslem_2")
        self.showResult = QtWidgets.QPushButton(self.tab_3)
        self.showResult.setGeometry(QtCore.QRect(840, 100, 301, 61))
        self.showResult.setObjectName("showResult")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.tab_3)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(10, 260, 821, 371))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.matplotlib_2 = QtWidgets.QWidget(self.verticalLayoutWidget_5)
        self.matplotlib_2.setObjectName("matplotlib_2")
        self.verticalLayout_5.addWidget(self.matplotlib_2)
        self.showResult_2 = QtWidgets.QPushButton(self.tab_3)
        self.showResult_2.setGeometry(QtCore.QRect(840, 30, 301, 61))
        self.showResult_2.setObjectName("showResult_2")
        self.showResult_3 = QtWidgets.QPushButton(self.tab_3)
        self.showResult_3.setGeometry(QtCore.QRect(840, 170, 301, 61))
        self.showResult_3.setObjectName("showResult_3")
        self.showResult_4 = QtWidgets.QPushButton(self.tab_3)
        self.showResult_4.setGeometry(QtCore.QRect(840, 240, 301, 61))
        self.showResult_4.setObjectName("showResult_4")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.widget = QtWidgets.QWidget(self.tab_2)
        self.widget.setGeometry(QtCore.QRect(140, 20, 831, 431))
        self.widget.setObjectName("widget")
        self.resim_label = QtWidgets.QLabel(self.widget)
        self.resim_label.setGeometry(QtCore.QRect(0, 0, 821, 421))
        self.resim_label.setObjectName("resim_label")
        self.goster_goruntu_isleme = QtWidgets.QPushButton(self.tab_2)
        self.goster_goruntu_isleme.setGeometry(QtCore.QRect(580, 460, 261, 61))
        self.goster_goruntu_isleme.setObjectName("goster_goruntu_isleme")
        self.dosyasec_goruntu_isleme = QtWidgets.QPushButton(self.tab_2)
        self.dosyasec_goruntu_isleme.setGeometry(QtCore.QRect(310, 460, 261, 61))
        self.dosyasec_goruntu_isleme.setObjectName("dosyasec_goruntu_isleme")
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
        self.btnGreedy.setText(_translate("MainWindow", "Greedy Algoritma"))
        self.lblBaslik.setText(_translate("MainWindow", "Kesme ve Paketleme Problemi Uygulama Arayüzü"))
        self.lblIslem.setText(_translate("MainWindow", "İşlemler"))
        self.btnVeriSec.setText(_translate("MainWindow", "Veri Seç"))
        self.btnSaveSVG.setText(_translate("MainWindow", "SVG Olarak Kaydet"))
        self.btnSonucGoruntule.setText(_translate("MainWindow", "Sonuçları Görüntüle"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Ana Sayfa"))
        self.lblIslem_2.setText(_translate("MainWindow", "Sonuçlar"))
        self.showResult.setText(_translate("MainWindow", "Görselleştir"))
        self.showResult_2.setText(_translate("MainWindow", "Sonuçları Yükle"))
        self.showResult_3.setText(_translate("MainWindow", "Seçilen Sonuçları Sil"))
        self.showResult_4.setText(_translate("MainWindow", "Tüm Sonuçları Sil"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Sonuçlar"))
        self.resim_label.setText(_translate("MainWindow", "                                                                                             Görüntü Yok"))
        self.goster_goruntu_isleme.setText(_translate("MainWindow", "Göster"))
        self.dosyasec_goruntu_isleme.setText(_translate("MainWindow", "Dosya Seç"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Görüntü İşleme"))
import icons_rc
