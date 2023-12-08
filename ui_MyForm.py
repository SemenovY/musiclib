# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Главное окно.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDial, QFrame,
    QHeaderView, QLabel, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QTabWidget, QTextBrowser, QTreeWidget, QTreeWidgetItem,
    QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1407, 1034)
        MainWindow.setWindowOpacity(1.000000000000000)
        MainWindow.setStyleSheet(u"background-color: rgb(36, 31, 49);\n"
"color: rgb(255, 255, 255);\n"
"selection-color: rgb(249, 240, 107);\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(1197, 20, 131, 29))
        self.pushButton.setStyleSheet(u"background-color: rgb(119, 118, 123);\n"
"font-family: italic 11pt \"Noto Sans\";")
        self.pushButton.setFlat(False)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QRect(30, 20, 1301, 921))
        self.tabWidget.setStyleSheet(u"font-color: rgb(255, 255, 255);")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.treeWidget = QTreeWidget(self.tab)
        QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(self.treeWidget)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setGeometry(QRect(-1, -1, 346, 141))
        self.treeWidget.setWordWrap(False)
        self.treeWidget.setHeaderHidden(False)
        self.listWidget = QListWidget(self.tab)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(-1, 139, 346, 26))
        self.treeWidget_2 = QTreeWidget(self.tab)
        QTreeWidgetItem(self.treeWidget_2)
        QTreeWidgetItem(self.treeWidget_2)
        QTreeWidgetItem(self.treeWidget_2)
        QTreeWidgetItem(self.treeWidget_2)
        self.treeWidget_2.setObjectName(u"treeWidget_2")
        self.treeWidget_2.setGeometry(QRect(-1, 164, 346, 111))
        self.treeWidget_3 = QTreeWidget(self.tab)
        QTreeWidgetItem(self.treeWidget_3)
        QTreeWidgetItem(self.treeWidget_3)
        QTreeWidgetItem(self.treeWidget_3)
        QTreeWidgetItem(self.treeWidget_3)
        self.treeWidget_3.setObjectName(u"treeWidget_3")
        self.treeWidget_3.setGeometry(QRect(-1, 274, 346, 111))
        self.listWidget_2 = QListWidget(self.tab)
        QListWidgetItem(self.listWidget_2)
        self.listWidget_2.setObjectName(u"listWidget_2")
        self.listWidget_2.setGeometry(QRect(-1, 384, 346, 26))
        self.listWidget_5 = QListWidget(self.tab)
        QListWidgetItem(self.listWidget_5)
        self.listWidget_5.setObjectName(u"listWidget_5")
        self.listWidget_5.setGeometry(QRect(0, 480, 346, 26))
        self.listWidget_6 = QListWidget(self.tab)
        QListWidgetItem(self.listWidget_6)
        self.listWidget_6.setObjectName(u"listWidget_6")
        self.listWidget_6.setGeometry(QRect(0, 504, 346, 26))
        self.treeWidget_6 = QTreeWidget(self.tab)
        QTreeWidgetItem(self.treeWidget_6)
        QTreeWidgetItem(self.treeWidget_6)
        self.treeWidget_6.setObjectName(u"treeWidget_6")
        self.treeWidget_6.setGeometry(QRect(0, 410, 345, 71))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.listWidget_7 = QListWidget(self.tab_2)
        QListWidgetItem(self.listWidget_7)
        self.listWidget_7.setObjectName(u"listWidget_7")
        self.listWidget_7.setGeometry(QRect(-1, -1, 346, 25))
        self.treeWidget_4 = QTreeWidget(self.tab_2)
        QTreeWidgetItem(self.treeWidget_4)
        QTreeWidgetItem(self.treeWidget_4)
        QTreeWidgetItem(self.treeWidget_4)
        self.treeWidget_4.setObjectName(u"treeWidget_4")
        self.treeWidget_4.setGeometry(QRect(-1, 23, 346, 91))
        self.treeWidget_5 = QTreeWidget(self.tab_2)
        QTreeWidgetItem(self.treeWidget_5)
        QTreeWidgetItem(self.treeWidget_5)
        QTreeWidgetItem(self.treeWidget_5)
        self.treeWidget_5.setObjectName(u"treeWidget_5")
        self.treeWidget_5.setGeometry(QRect(-1, 113, 346, 91))
        self.treeWidget_7 = QTreeWidget(self.tab_2)
        QTreeWidgetItem(self.treeWidget_7)
        QTreeWidgetItem(self.treeWidget_7)
        QTreeWidgetItem(self.treeWidget_7)
        QTreeWidgetItem(self.treeWidget_7)
        self.treeWidget_7.setObjectName(u"treeWidget_7")
        self.treeWidget_7.setGeometry(QRect(-1, 210, 346, 111))
        self.treeWidget_8 = QTreeWidget(self.tab_2)
        QTreeWidgetItem(self.treeWidget_8)
        QTreeWidgetItem(self.treeWidget_8)
        self.treeWidget_8.setObjectName(u"treeWidget_8")
        self.treeWidget_8.setGeometry(QRect(-1, 320, 346, 71))
        self.treeWidget_9 = QTreeWidget(self.tab_2)
        QTreeWidgetItem(self.treeWidget_9)
        QTreeWidgetItem(self.treeWidget_9)
        QTreeWidgetItem(self.treeWidget_9)
        QTreeWidgetItem(self.treeWidget_9)
        QTreeWidgetItem(self.treeWidget_9)
        self.treeWidget_9.setObjectName(u"treeWidget_9")
        self.treeWidget_9.setGeometry(QRect(-1, 390, 346, 134))
        self.treeWidget_10 = QTreeWidget(self.tab_2)
        QTreeWidgetItem(self.treeWidget_10)
        QTreeWidgetItem(self.treeWidget_10)
        self.treeWidget_10.setObjectName(u"treeWidget_10")
        self.treeWidget_10.setGeometry(QRect(-1, 520, 346, 71))
        self.treeWidget_11 = QTreeWidget(self.tab_2)
        QTreeWidgetItem(self.treeWidget_11)
        QTreeWidgetItem(self.treeWidget_11)
        QTreeWidgetItem(self.treeWidget_11)
        QTreeWidgetItem(self.treeWidget_11)
        QTreeWidgetItem(self.treeWidget_11)
        self.treeWidget_11.setObjectName(u"treeWidget_11")
        self.treeWidget_11.setGeometry(QRect(-1, 590, 346, 132))
        self.listWidget_8 = QListWidget(self.tab_2)
        QListWidgetItem(self.listWidget_8)
        self.listWidget_8.setObjectName(u"listWidget_8")
        self.listWidget_8.setGeometry(QRect(-1, 720, 346, 22))
        self.treeWidget_12 = QTreeWidget(self.tab_2)
        QTreeWidgetItem(self.treeWidget_12)
        QTreeWidgetItem(self.treeWidget_12)
        QTreeWidgetItem(self.treeWidget_12)
        self.treeWidget_12.setObjectName(u"treeWidget_12")
        self.treeWidget_12.setGeometry(QRect(0, 740, 346, 101))
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.listWidget_11 = QListWidget(self.tab_3)
        QListWidgetItem(self.listWidget_11)
        self.listWidget_11.setObjectName(u"listWidget_11")
        self.listWidget_11.setGeometry(QRect(-1, -1, 256, 25))
        self.listWidget_12 = QListWidget(self.tab_3)
        QListWidgetItem(self.listWidget_12)
        self.listWidget_12.setObjectName(u"listWidget_12")
        self.listWidget_12.setGeometry(QRect(-1, 23, 256, 25))
        self.listWidget_13 = QListWidget(self.tab_3)
        QListWidgetItem(self.listWidget_13)
        self.listWidget_13.setObjectName(u"listWidget_13")
        self.listWidget_13.setGeometry(QRect(-1, 47, 256, 25))
        self.listWidget_14 = QListWidget(self.tab_3)
        QListWidgetItem(self.listWidget_14)
        self.listWidget_14.setObjectName(u"listWidget_14")
        self.listWidget_14.setGeometry(QRect(-1, 71, 256, 25))
        self.listWidget_15 = QListWidget(self.tab_3)
        QListWidgetItem(self.listWidget_15)
        self.listWidget_15.setObjectName(u"listWidget_15")
        self.listWidget_15.setGeometry(QRect(-1, 95, 256, 25))
        self.listWidget_16 = QListWidget(self.tab_3)
        QListWidgetItem(self.listWidget_16)
        self.listWidget_16.setObjectName(u"listWidget_16")
        self.listWidget_16.setGeometry(QRect(-1, 119, 256, 25))
        self.listWidget_17 = QListWidget(self.tab_3)
        QListWidgetItem(self.listWidget_17)
        self.listWidget_17.setObjectName(u"listWidget_17")
        self.listWidget_17.setGeometry(QRect(-1, 143, 256, 25))
        self.listWidget_18 = QListWidget(self.tab_3)
        QListWidgetItem(self.listWidget_18)
        self.listWidget_18.setObjectName(u"listWidget_18")
        self.listWidget_18.setGeometry(QRect(-1, 167, 256, 25))
        self.treeWidget_13 = QTreeWidget(self.tab_3)
        QTreeWidgetItem(self.treeWidget_13)
        QTreeWidgetItem(self.treeWidget_13)
        QTreeWidgetItem(self.treeWidget_13)
        QTreeWidgetItem(self.treeWidget_13)
        QTreeWidgetItem(self.treeWidget_13)
        self.treeWidget_13.setObjectName(u"treeWidget_13")
        self.treeWidget_13.setGeometry(QRect(260, 0, 511, 141))
        self.treeWidget_13.setStyleSheet(u"background-color: rgb(61, 56, 70);")
        self.treeWidget_13.setEditTriggers(QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed|QAbstractItemView.SelectedClicked)
        self.treeWidget_14 = QTreeWidget(self.tab_3)
        QTreeWidgetItem(self.treeWidget_14)
        QTreeWidgetItem(self.treeWidget_14)
        QTreeWidgetItem(self.treeWidget_14)
        self.treeWidget_14.setObjectName(u"treeWidget_14")
        self.treeWidget_14.setGeometry(QRect(260, 140, 511, 91))
        self.treeWidget_14.setStyleSheet(u"background-color: rgb(61, 56, 70);")
        self.treeWidget_29 = QTreeWidget(self.tab_3)
        QTreeWidgetItem(self.treeWidget_29)
        QTreeWidgetItem(self.treeWidget_29)
        QTreeWidgetItem(self.treeWidget_29)
        self.treeWidget_29.setObjectName(u"treeWidget_29")
        self.treeWidget_29.setGeometry(QRect(260, 230, 511, 91))
        self.treeWidget_29.setStyleSheet(u"background-color: rgb(61, 56, 70);")
        self.treeWidget_30 = QTreeWidget(self.tab_3)
        QTreeWidgetItem(self.treeWidget_30)
        QTreeWidgetItem(self.treeWidget_30)
        QTreeWidgetItem(self.treeWidget_30)
        QTreeWidgetItem(self.treeWidget_30)
        QTreeWidgetItem(self.treeWidget_30)
        QTreeWidgetItem(self.treeWidget_30)
        QTreeWidgetItem(self.treeWidget_30)
        QTreeWidgetItem(self.treeWidget_30)
        QTreeWidgetItem(self.treeWidget_30)
        QTreeWidgetItem(self.treeWidget_30)
        QTreeWidgetItem(self.treeWidget_30)
        QTreeWidgetItem(self.treeWidget_30)
        QTreeWidgetItem(self.treeWidget_30)
        self.treeWidget_30.setObjectName(u"treeWidget_30")
        self.treeWidget_30.setGeometry(QRect(260, 320, 511, 301))
        self.treeWidget_30.setStyleSheet(u"background-color: rgb(61, 56, 70);")
        self.treeWidget_31 = QTreeWidget(self.tab_3)
        QTreeWidgetItem(self.treeWidget_31)
        QTreeWidgetItem(self.treeWidget_31)
        QTreeWidgetItem(self.treeWidget_31)
        QTreeWidgetItem(self.treeWidget_31)
        QTreeWidgetItem(self.treeWidget_31)
        QTreeWidgetItem(self.treeWidget_31)
        QTreeWidgetItem(self.treeWidget_31)
        QTreeWidgetItem(self.treeWidget_31)
        QTreeWidgetItem(self.treeWidget_31)
        QTreeWidgetItem(self.treeWidget_31)
        QTreeWidgetItem(self.treeWidget_31)
        QTreeWidgetItem(self.treeWidget_31)
        QTreeWidgetItem(self.treeWidget_31)
        self.treeWidget_31.setObjectName(u"treeWidget_31")
        self.treeWidget_31.setGeometry(QRect(260, 620, 511, 251))
        self.treeWidget_31.setStyleSheet(u"background-color: rgb(61, 56, 70);")
        self.textBrowser = QTextBrowser(self.tab_3)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(780, 0, 481, 861))
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.listWidget_23 = QListWidget(self.tab_4)
        QListWidgetItem(self.listWidget_23)
        QListWidgetItem(self.listWidget_23)
        QListWidgetItem(self.listWidget_23)
        QListWidgetItem(self.listWidget_23)
        QListWidgetItem(self.listWidget_23)
        QListWidgetItem(self.listWidget_23)
        QListWidgetItem(self.listWidget_23)
        QListWidgetItem(self.listWidget_23)
        QListWidgetItem(self.listWidget_23)
        QListWidgetItem(self.listWidget_23)
        QListWidgetItem(self.listWidget_23)
        QListWidgetItem(self.listWidget_23)
        QListWidgetItem(self.listWidget_23)
        QListWidgetItem(self.listWidget_23)
        QListWidgetItem(self.listWidget_23)
        QListWidgetItem(self.listWidget_23)
        QListWidgetItem(self.listWidget_23)
        QListWidgetItem(self.listWidget_23)
        QListWidgetItem(self.listWidget_23)
        QListWidgetItem(self.listWidget_23)
        QListWidgetItem(self.listWidget_23)
        QListWidgetItem(self.listWidget_23)
        QListWidgetItem(self.listWidget_23)
        self.listWidget_23.setObjectName(u"listWidget_23")
        self.listWidget_23.setGeometry(QRect(-1, -1, 351, 831))
        self.textBrowser_2 = QTextBrowser(self.tab_4)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setGeometry(QRect(830, 0, 451, 811))
        self.treeWidget_32 = QTreeWidget(self.tab_4)
        QTreeWidgetItem(self.treeWidget_32)
        QTreeWidgetItem(self.treeWidget_32)
        QTreeWidgetItem(self.treeWidget_32)
        QTreeWidgetItem(self.treeWidget_32)
        self.treeWidget_32.setObjectName(u"treeWidget_32")
        self.treeWidget_32.setGeometry(QRect(350, -1, 471, 111))
        self.treeWidget_32.setStyleSheet(u"background-color: rgb(61, 56, 70);")
        self.treeWidget_32.setEditTriggers(QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed|QAbstractItemView.SelectedClicked)
        self.treeWidget_33 = QTreeWidget(self.tab_4)
        QTreeWidgetItem(self.treeWidget_33)
        QTreeWidgetItem(self.treeWidget_33)
        QTreeWidgetItem(self.treeWidget_33)
        QTreeWidgetItem(self.treeWidget_33)
        self.treeWidget_33.setObjectName(u"treeWidget_33")
        self.treeWidget_33.setGeometry(QRect(350, 109, 471, 711))
        self.treeWidget_33.setStyleSheet(u"background-color: rgb(61, 56, 70);")
        self.treeWidget_33.setEditTriggers(QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed|QAbstractItemView.SelectedClicked)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.listWidget_9 = QListWidget(self.tab_5)
        QListWidgetItem(self.listWidget_9)
        self.listWidget_9.setObjectName(u"listWidget_9")
        self.listWidget_9.setGeometry(QRect(-1, -1, 346, 26))
        self.listWidget_10 = QListWidget(self.tab_5)
        QListWidgetItem(self.listWidget_10)
        self.listWidget_10.setObjectName(u"listWidget_10")
        self.listWidget_10.setGeometry(QRect(-1, 24, 346, 26))
        self.tabWidget.addTab(self.tab_5, "")
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(31, 950, 1301, 5))
        self.line.setStyleSheet(u"color: rgb(249, 240, 107);\n"
"background-color: rgb(249, 240, 107);")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.dial = QDial(self.centralwidget)
        self.dial.setObjectName(u"dial")
        self.dial.setGeometry(QRect(1233, 920, 50, 64))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(30, 974, 97, 29))
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(126, 974, 97, 29))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(249, 980, 141, 21))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.pushButton.setDefault(False)
        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043f\u043e\u0432. \u0418\u043d\u0441\u0442\u0440\u0443\u043c\u0435\u043d\u0442\u043e\u0432\u0435\u0434\u0435\u043d\u0438\u0435", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"\u0421\u043a\u0440\u0438\u043f\u043a\u0438", None));

        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.treeWidget.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"\u0421\u043a\u0440\u0438\u043f\u043a\u0430, \u0430\u043b\u044c\u0442, \u0432\u0438\u043e\u043b\u043e\u043d\u0447\u0435\u043b\u044c, \u043a\u043e\u043d\u0442\u0440\u0430\u0431\u0430\u0441", None));
        ___qtreewidgetitem2 = self.treeWidget.topLevelItem(1)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow", u"\u0421\u043a\u0440\u0438\u043f\u043a\u0430", None));
        ___qtreewidgetitem3 = self.treeWidget.topLevelItem(2)
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("MainWindow", u"\u0410\u043b\u044c\u0442", None));
        ___qtreewidgetitem4 = self.treeWidget.topLevelItem(3)
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("MainWindow", u"\u0412\u0438\u043e\u043b\u043e\u043d\u0447\u0435\u043b\u044c", None));
        ___qtreewidgetitem5 = self.treeWidget.topLevelItem(4)
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0442\u0440\u0430\u0431\u0430\u0441", None));
        self.treeWidget.setSortingEnabled(__sortingEnabled)


        __sortingEnabled1 = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043b\u0430\u0441\u0441\u0438\u0447\u0435\u0441\u043a\u0430\u044f \u0433\u0438\u0442\u0430\u0440\u0430", None));
        self.listWidget.setSortingEnabled(__sortingEnabled1)

        ___qtreewidgetitem6 = self.treeWidget_2.headerItem()
        ___qtreewidgetitem6.setText(0, QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043c\u0440\u044b", None));

        __sortingEnabled2 = self.treeWidget_2.isSortingEnabled()
        self.treeWidget_2.setSortingEnabled(False)
        ___qtreewidgetitem7 = self.treeWidget_2.topLevelItem(0)
        ___qtreewidgetitem7.setText(0, QCoreApplication.translate("MainWindow", u"\u041c\u0430\u043b\u0430\u044f \u0434\u043e\u043c\u0440\u0430", None));
        ___qtreewidgetitem8 = self.treeWidget_2.topLevelItem(1)
        ___qtreewidgetitem8.setText(0, QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043c\u0440\u0430 \u043f\u0438\u043a\u043a\u043e\u043b\u043e", None));
        ___qtreewidgetitem9 = self.treeWidget_2.topLevelItem(2)
        ___qtreewidgetitem9.setText(0, QCoreApplication.translate("MainWindow", u"\u0410\u043b\u044c\u0442\u043e\u0432\u0430\u044f \u0434\u043e\u043c\u0440\u0430", None));
        ___qtreewidgetitem10 = self.treeWidget_2.topLevelItem(3)
        ___qtreewidgetitem10.setText(0, QCoreApplication.translate("MainWindow", u"\u0411\u0430\u0441\u043e\u0432\u0430\u044f \u0434\u043e\u043c\u0440\u0430", None));
        self.treeWidget_2.setSortingEnabled(__sortingEnabled2)

        ___qtreewidgetitem11 = self.treeWidget_3.headerItem()
        ___qtreewidgetitem11.setText(0, QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043b\u0430\u043b\u0430\u0439\u043a\u0438", None));

        __sortingEnabled3 = self.treeWidget_3.isSortingEnabled()
        self.treeWidget_3.setSortingEnabled(False)
        ___qtreewidgetitem12 = self.treeWidget_3.topLevelItem(0)
        ___qtreewidgetitem12.setText(0, QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043b\u0430\u043b\u0430\u0439\u043a\u0430 \u043f\u0440\u0438\u043c\u0430", None));
        ___qtreewidgetitem13 = self.treeWidget_3.topLevelItem(1)
        ___qtreewidgetitem13.setText(0, QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043b\u0430\u043b\u0430\u0439\u043a\u0430 \u0441\u0435\u043a\u0443\u043d\u0434\u0430", None));
        ___qtreewidgetitem14 = self.treeWidget_3.topLevelItem(2)
        ___qtreewidgetitem14.setText(0, QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043b\u0430\u043b\u0430\u0439\u043a\u0430 \u0430\u043b\u044c\u0442", None));
        ___qtreewidgetitem15 = self.treeWidget_3.topLevelItem(3)
        ___qtreewidgetitem15.setText(0, QCoreApplication.translate("MainWindow", u"\u0411\u0430\u043b\u0430\u043b\u0430\u0439\u043a\u0430 \u043a\u043e\u043d\u0442\u0440\u0430\u0431\u0430\u0441", None));
        self.treeWidget_3.setSortingEnabled(__sortingEnabled3)


        __sortingEnabled4 = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        ___qlistwidgetitem1 = self.listWidget_2.item(0)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043b\u0430\u0441\u0441\u0438\u0447\u0435\u0441\u043a\u0430\u044f \u0430\u0440\u0444\u0430", None));
        self.listWidget_2.setSortingEnabled(__sortingEnabled4)


        __sortingEnabled5 = self.listWidget_5.isSortingEnabled()
        self.listWidget_5.setSortingEnabled(False)
        ___qlistwidgetitem2 = self.listWidget_5.item(0)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043b\u0430\u0432\u0435\u0441\u0438\u043d", None));
        self.listWidget_5.setSortingEnabled(__sortingEnabled5)


        __sortingEnabled6 = self.listWidget_6.isSortingEnabled()
        self.listWidget_6.setSortingEnabled(False)
        ___qlistwidgetitem3 = self.listWidget_6.item(0)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u0420\u043e\u044f\u043b\u044c", None));
        self.listWidget_6.setSortingEnabled(__sortingEnabled6)

        ___qtreewidgetitem16 = self.treeWidget_6.headerItem()
        ___qtreewidgetitem16.setText(0, QCoreApplication.translate("MainWindow", u"\u0413\u0443\u0441\u043b\u0438", None));

        __sortingEnabled7 = self.treeWidget_6.isSortingEnabled()
        self.treeWidget_6.setSortingEnabled(False)
        ___qtreewidgetitem17 = self.treeWidget_6.topLevelItem(0)
        ___qtreewidgetitem17.setText(0, QCoreApplication.translate("MainWindow", u"\u0417\u0432\u043e\u043d\u0447\u0430\u0442\u044b\u0435 \u0433\u0443\u0441\u043b\u0438 (20-\u0441\u0442\u0440\u0443\u043d\u043d\u044b\u0435)", None));
        ___qtreewidgetitem18 = self.treeWidget_6.topLevelItem(1)
        ___qtreewidgetitem18.setText(0, QCoreApplication.translate("MainWindow", u"\u041a\u043b\u0430\u0432\u0438\u0448\u043d\u044b\u0435 \u0433\u0443\u0441\u043b\u0438", None));
        self.treeWidget_6.setSortingEnabled(__sortingEnabled7)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0440\u0443\u043d\u043d\u044b\u0435", None))

        __sortingEnabled8 = self.listWidget_7.isSortingEnabled()
        self.listWidget_7.setSortingEnabled(False)
        ___qlistwidgetitem4 = self.listWidget_7.item(0)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0435\u0440\u0435\u0432\u044f\u043d\u043d\u044b\u0435 \u0438 \u043c\u0435\u0434\u043d\u044b\u0435 \u0434\u0443\u0445\u043e\u0432\u044b\u0435 \u0438\u043d\u0441\u0442\u0440\u0443\u043c\u0435\u043d\u0442\u044b", None));
        self.listWidget_7.setSortingEnabled(__sortingEnabled8)

        ___qtreewidgetitem19 = self.treeWidget_4.headerItem()
        ___qtreewidgetitem19.setText(0, QCoreApplication.translate("MainWindow", u"\u0410\u043a\u0430\u0434\u0435\u043c\u0438\u0447\u0435\u0441\u043a\u0438\u0435 \u043f\u043e\u043f\u0435\u0440\u0435\u0447\u043d\u044b\u0435 \u0444\u043b\u0435\u0439\u0442\u044b", None));

        __sortingEnabled9 = self.treeWidget_4.isSortingEnabled()
        self.treeWidget_4.setSortingEnabled(False)
        ___qtreewidgetitem20 = self.treeWidget_4.topLevelItem(0)
        ___qtreewidgetitem20.setText(0, QCoreApplication.translate("MainWindow", u"\u0411\u043e\u043b\u044c\u0448\u0430\u044f \u0444\u043b\u0435\u0439\u0442\u0430", None));
        ___qtreewidgetitem21 = self.treeWidget_4.topLevelItem(1)
        ___qtreewidgetitem21.setText(0, QCoreApplication.translate("MainWindow", u"\u0424\u043b\u0435\u0439\u0442\u0430 \u043f\u0438\u043a\u043a\u043e\u043b\u043e", None));
        ___qtreewidgetitem22 = self.treeWidget_4.topLevelItem(2)
        ___qtreewidgetitem22.setText(0, QCoreApplication.translate("MainWindow", u"\u0410\u043b\u044c\u0442\u043e\u0432\u0430\u044f \u0444\u043b\u0435\u0439\u0442\u0430", None));
        self.treeWidget_4.setSortingEnabled(__sortingEnabled9)

        ___qtreewidgetitem23 = self.treeWidget_5.headerItem()
        ___qtreewidgetitem23.setText(0, QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0431\u043e\u0438", None));

        __sortingEnabled10 = self.treeWidget_5.isSortingEnabled()
        self.treeWidget_5.setSortingEnabled(False)
        ___qtreewidgetitem24 = self.treeWidget_5.topLevelItem(0)
        ___qtreewidgetitem24.setText(0, QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0431\u043e\u0439, \u0430\u043d\u0433\u043b\u0438\u0439\u0441\u043a\u0438\u0439 \u0440\u043e\u0436\u043e\u043a, \u0433\u043e\u0431\u043e\u0439 \u0434`\u0430\u043c\u0443\u0440", None));
        ___qtreewidgetitem25 = self.treeWidget_5.topLevelItem(1)
        ___qtreewidgetitem25.setText(0, QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0431\u043e\u0439", None));
        ___qtreewidgetitem26 = self.treeWidget_5.topLevelItem(2)
        ___qtreewidgetitem26.setText(0, QCoreApplication.translate("MainWindow", u"\u0410\u043d\u0433\u043b\u0438\u0439\u0441\u043a\u0438\u0439 \u0440\u043e\u0436\u043e\u043a", None));
        self.treeWidget_5.setSortingEnabled(__sortingEnabled10)

        ___qtreewidgetitem27 = self.treeWidget_7.headerItem()
        ___qtreewidgetitem27.setText(0, QCoreApplication.translate("MainWindow", u"\u041a\u043b\u0430\u0440\u043d\u0435\u0442\u044b", None));

        __sortingEnabled11 = self.treeWidget_7.isSortingEnabled()
        self.treeWidget_7.setSortingEnabled(False)
        ___qtreewidgetitem28 = self.treeWidget_7.topLevelItem(0)
        ___qtreewidgetitem28.setText(0, QCoreApplication.translate("MainWindow", u"\u041a\u043b\u0430\u0440\u043d\u0435\u0442 in B, \u043a\u043b\u0430\u0440\u043d\u0435\u0442 in A", None));
        ___qtreewidgetitem29 = self.treeWidget_7.topLevelItem(1)
        ___qtreewidgetitem29.setText(0, QCoreApplication.translate("MainWindow", u"\u041a\u043b\u0430\u0440\u043d\u0435\u0442 in B", None));
        ___qtreewidgetitem30 = self.treeWidget_7.topLevelItem(2)
        ___qtreewidgetitem30.setText(0, QCoreApplication.translate("MainWindow", u"\u041a\u043b\u0430\u0440\u043d\u0435\u0442 \u043f\u0438\u043a\u043a\u043e\u043b\u043e in Es", None));
        ___qtreewidgetitem31 = self.treeWidget_7.topLevelItem(3)
        ___qtreewidgetitem31.setText(0, QCoreApplication.translate("MainWindow", u"\u0411\u0430\u0441-\u043a\u043b\u0430\u0440\u043d\u0435\u0442 in B", None));
        self.treeWidget_7.setSortingEnabled(__sortingEnabled11)

        ___qtreewidgetitem32 = self.treeWidget_8.headerItem()
        ___qtreewidgetitem32.setText(0, QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0433\u043e\u0442\u044b", None));

        __sortingEnabled12 = self.treeWidget_8.isSortingEnabled()
        self.treeWidget_8.setSortingEnabled(False)
        ___qtreewidgetitem33 = self.treeWidget_8.topLevelItem(0)
        ___qtreewidgetitem33.setText(0, QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0433\u043e\u0442", None));
        ___qtreewidgetitem34 = self.treeWidget_8.topLevelItem(1)
        ___qtreewidgetitem34.setText(0, QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0442\u0440\u0430\u0444\u0430\u0433\u043e\u0442", None));
        self.treeWidget_8.setSortingEnabled(__sortingEnabled12)

        ___qtreewidgetitem35 = self.treeWidget_9.headerItem()
        ___qtreewidgetitem35.setText(0, QCoreApplication.translate("MainWindow", u"\u0421\u0430\u043a\u0441\u043e\u0444\u043e\u043d\u044b", None));

        __sortingEnabled13 = self.treeWidget_9.isSortingEnabled()
        self.treeWidget_9.setSortingEnabled(False)
        ___qtreewidgetitem36 = self.treeWidget_9.topLevelItem(0)
        ___qtreewidgetitem36.setText(0, QCoreApplication.translate("MainWindow", u"\u0427\u0435\u0442\u044b\u0440\u0435 \u0441\u0430\u043a\u0441\u043e\u0444\u043e\u043d\u0430", None));
        ___qtreewidgetitem37 = self.treeWidget_9.topLevelItem(1)
        ___qtreewidgetitem37.setText(0, QCoreApplication.translate("MainWindow", u"\u0410\u043b\u044c\u0442\u043e\u0432\u044b\u0439 \u0441\u0430\u043a\u0441\u043e\u0444\u043e\u043d", None));
        ___qtreewidgetitem38 = self.treeWidget_9.topLevelItem(2)
        ___qtreewidgetitem38.setText(0, QCoreApplication.translate("MainWindow", u"\u0421\u043e\u043f\u0440\u0430\u043d\u043e\u0432\u044b\u0439 \u0441\u0430\u043a\u0441\u043e\u0444\u043e\u043d", None));
        ___qtreewidgetitem39 = self.treeWidget_9.topLevelItem(3)
        ___qtreewidgetitem39.setText(0, QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043d\u043e\u0440\u043e\u0432\u044b\u0439 \u0441\u0430\u043a\u0441\u043e\u0444\u043e\u043d", None));
        ___qtreewidgetitem40 = self.treeWidget_9.topLevelItem(4)
        ___qtreewidgetitem40.setText(0, QCoreApplication.translate("MainWindow", u"\u0411\u0430\u0440\u0438\u0442\u043e\u043d\u043e\u0432\u044b\u0439 \u0441\u0430\u043a\u0441\u043e\u0444\u043e\u043d", None));
        self.treeWidget_9.setSortingEnabled(__sortingEnabled13)

        ___qtreewidgetitem41 = self.treeWidget_10.headerItem()
        ___qtreewidgetitem41.setText(0, QCoreApplication.translate("MainWindow", u"\u0412\u0430\u043b\u0442\u043e\u0440\u043d\u044b", None));

        __sortingEnabled14 = self.treeWidget_10.isSortingEnabled()
        self.treeWidget_10.setSortingEnabled(False)
        ___qtreewidgetitem42 = self.treeWidget_10.topLevelItem(0)
        ___qtreewidgetitem42.setText(0, QCoreApplication.translate("MainWindow", u"\u0414\u0432\u043e\u0439\u043d\u0430\u044f \u0432\u0430\u043b\u0442\u043e\u0440\u043d\u0430, \u0434\u0438\u0441\u043a\u0430\u043d\u0442\u043e\u0432\u0430\u044f \u0432\u0430\u043b\u0442\u043e\u0440\u043d\u0430", None));
        ___qtreewidgetitem43 = self.treeWidget_10.topLevelItem(1)
        ___qtreewidgetitem43.setText(0, QCoreApplication.translate("MainWindow", u"\u0412\u0430\u043b\u0442\u043e\u0440\u043d\u0430 in F (\u0434\u0438\u0441\u043a\u0430\u043d\u0442\u043e\u0432\u0430\u044f)", None));
        self.treeWidget_10.setSortingEnabled(__sortingEnabled14)

        ___qtreewidgetitem44 = self.treeWidget_11.headerItem()
        ___qtreewidgetitem44.setText(0, QCoreApplication.translate("MainWindow", u"\u0422\u0440\u0443\u0431\u044b \u0438 \u0431\u043b\u0438\u0437\u043a\u0438\u0435 \u0438\u043c \u0438\u043d\u0441\u0442\u0440\u0443\u043c\u0435\u043d\u0442\u044b", None));

        __sortingEnabled15 = self.treeWidget_11.isSortingEnabled()
        self.treeWidget_11.setSortingEnabled(False)
        ___qtreewidgetitem45 = self.treeWidget_11.topLevelItem(0)
        ___qtreewidgetitem45.setText(0, QCoreApplication.translate("MainWindow", u"\u0422\u0440\u0443\u0431\u0430, \u043a\u043e\u0440\u043d\u0435\u0442, \u0444\u043b\u044e\u0433\u0435\u043b\u044c\u0433\u043e\u0440\u043d", None));
        ___qtreewidgetitem46 = self.treeWidget_11.topLevelItem(1)
        ___qtreewidgetitem46.setText(0, QCoreApplication.translate("MainWindow", u"\u0422\u0440\u0443\u0431\u0430 in B", None));
        ___qtreewidgetitem47 = self.treeWidget_11.topLevelItem(2)
        ___qtreewidgetitem47.setText(0, QCoreApplication.translate("MainWindow", u"\u0422\u0440\u0443\u0431\u0430 \u043f\u0438\u043a\u043a\u043e\u043b\u043e in B", None));
        ___qtreewidgetitem48 = self.treeWidget_11.topLevelItem(3)
        ___qtreewidgetitem48.setText(0, QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0440\u043d\u0435\u0442 in B", None));
        ___qtreewidgetitem49 = self.treeWidget_11.topLevelItem(4)
        ___qtreewidgetitem49.setText(0, QCoreApplication.translate("MainWindow", u"\u0424\u043b\u044e\u0433\u0435\u043b\u044c\u0433\u043e\u0440\u043d in B", None));
        self.treeWidget_11.setSortingEnabled(__sortingEnabled15)


        __sortingEnabled16 = self.listWidget_8.isSortingEnabled()
        self.listWidget_8.setSortingEnabled(False)
        ___qlistwidgetitem5 = self.listWidget_8.item(0)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u0441\u043e\u0432\u044b\u0439 \u0442\u0440\u043e\u043c\u0431\u043e\u043d", None));
        self.listWidget_8.setSortingEnabled(__sortingEnabled16)

        ___qtreewidgetitem50 = self.treeWidget_12.headerItem()
        ___qtreewidgetitem50.setText(0, QCoreApplication.translate("MainWindow", u"\u0422\u0443\u0431\u044b", None));

        __sortingEnabled17 = self.treeWidget_12.isSortingEnabled()
        self.treeWidget_12.setSortingEnabled(False)
        ___qtreewidgetitem51 = self.treeWidget_12.topLevelItem(0)
        ___qtreewidgetitem51.setText(0, QCoreApplication.translate("MainWindow", u"\u0411\u0430\u0441\u043e\u0432\u0430\u044f \u0442\u0443\u0431\u0430, \u043a\u043e\u043d\u0442\u0440\u0430\u0431\u0430\u0441\u043e\u0432\u0430\u044f \u0442\u0443\u0431\u0430", None));
        ___qtreewidgetitem52 = self.treeWidget_12.topLevelItem(1)
        ___qtreewidgetitem52.setText(0, QCoreApplication.translate("MainWindow", u"\u0411\u0430\u0441\u043e\u0432\u0430\u044f \u0442\u0443\u0431\u0430", None));
        ___qtreewidgetitem53 = self.treeWidget_12.topLevelItem(2)
        ___qtreewidgetitem53.setText(0, QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0442\u0440\u0430\u0431\u0430\u0441\u043e\u0432\u0430\u044f \u0442\u0443\u0431\u0430", None));
        self.treeWidget_12.setSortingEnabled(__sortingEnabled17)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u0414\u0443\u0445\u043e\u0432\u044b\u0435", None))

        __sortingEnabled18 = self.listWidget_11.isSortingEnabled()
        self.listWidget_11.setSortingEnabled(False)
        ___qlistwidgetitem6 = self.listWidget_11.item(0)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0438\u0442\u0430\u0432\u0440\u044b", None));
        self.listWidget_11.setSortingEnabled(__sortingEnabled18)


        __sortingEnabled19 = self.listWidget_12.isSortingEnabled()
        self.listWidget_12.setSortingEnabled(False)
        ___qlistwidgetitem7 = self.listWidget_12.item(0)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u043b\u044b\u0439 \u0431\u0430\u0440\u0430\u0431\u0430\u043d", None));
        self.listWidget_12.setSortingEnabled(__sortingEnabled19)


        __sortingEnabled20 = self.listWidget_13.isSortingEnabled()
        self.listWidget_13.setSortingEnabled(False)
        ___qlistwidgetitem8 = self.listWidget_13.item(0)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u043c-\u0442\u043e\u043c", None));
        self.listWidget_13.setSortingEnabled(__sortingEnabled20)


        __sortingEnabled21 = self.listWidget_14.isSortingEnabled()
        self.listWidget_14.setSortingEnabled(False)
        ___qlistwidgetitem9 = self.listWidget_14.item(0)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u0411\u043e\u043b\u044c\u0448\u043e\u0439 \u0431\u0430\u0440\u0430\u0431\u0430\u043d", None));
        self.listWidget_14.setSortingEnabled(__sortingEnabled21)


        __sortingEnabled22 = self.listWidget_15.isSortingEnabled()
        self.listWidget_15.setSortingEnabled(False)
        ___qlistwidgetitem10 = self.listWidget_15.item(0)
        ___qlistwidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0440\u043a\u0435\u0441\u0442\u0440\u043e\u0432\u044b\u0439 \u0431\u0443\u0431\u0435\u043d", None));
        self.listWidget_15.setSortingEnabled(__sortingEnabled22)


        __sortingEnabled23 = self.listWidget_16.isSortingEnabled()
        self.listWidget_16.setSortingEnabled(False)
        ___qlistwidgetitem11 = self.listWidget_16.item(0)
        ___qlistwidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\u0411\u043e\u043d\u0433\u043e", None));
        self.listWidget_16.setSortingEnabled(__sortingEnabled23)


        __sortingEnabled24 = self.listWidget_17.isSortingEnabled()
        self.listWidget_17.setSortingEnabled(False)
        ___qlistwidgetitem12 = self.listWidget_17.item(0)
        ___qlistwidgetitem12.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0433\u0430\u0441", None));
        self.listWidget_17.setSortingEnabled(__sortingEnabled24)


        __sortingEnabled25 = self.listWidget_18.isSortingEnabled()
        self.listWidget_18.setSortingEnabled(False)
        ___qlistwidgetitem13 = self.listWidget_18.item(0)
        ___qlistwidgetitem13.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0443\u043b\u044c\u0442\u0438\u043f\u0435\u0440\u043a\u0443\u0441\u0441\u0438\u044f", None));
        self.listWidget_18.setSortingEnabled(__sortingEnabled25)

        ___qtreewidgetitem54 = self.treeWidget_13.headerItem()
        ___qtreewidgetitem54.setText(0, QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0430\u043f\u0430\u0437\u043e\u043d \u043a\u0430\u0436\u0434\u043e\u0439 \u043b\u0438\u0442\u0430\u0432\u0440\u044b", None));

        __sortingEnabled26 = self.treeWidget_13.isSortingEnabled()
        self.treeWidget_13.setSortingEnabled(False)
        ___qtreewidgetitem55 = self.treeWidget_13.topLevelItem(0)
        ___qtreewidgetitem55.setText(0, QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0430\u043f\u0430\u0437\u043e\u043d \u043f\u0435\u0440\u0432\u043e\u0439 \u043b\u0438\u0442\u0430\u0432\u0440\u044b", None));
        ___qtreewidgetitem56 = self.treeWidget_13.topLevelItem(1)
        ___qtreewidgetitem56.setText(0, QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0430\u043f\u0430\u0437\u043e\u043d \u0432\u0442\u043e\u0440\u043e\u0439 \u043b\u0438\u0442\u0430\u0432\u0440\u044b", None));
        ___qtreewidgetitem57 = self.treeWidget_13.topLevelItem(2)
        ___qtreewidgetitem57.setText(0, QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0430\u043f\u0430\u0437\u043e\u043d \u0442\u0440\u0435\u0442\u044c\u0435\u0439 \u043b\u0438\u0442\u0430\u0432\u0440\u044b", None));
        ___qtreewidgetitem58 = self.treeWidget_13.topLevelItem(3)
        ___qtreewidgetitem58.setText(0, QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0430\u043f\u0430\u0437\u043e\u043d \u0447\u0435\u0442\u0432\u0451\u0440\u0442\u043e\u0439 \u043b\u0438\u0442\u0430\u0432\u0440\u044b", None));
        ___qtreewidgetitem59 = self.treeWidget_13.topLevelItem(4)
        ___qtreewidgetitem59.setText(0, QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0430\u043f\u0430\u0437\u043e\u043d \u043f\u044f\u0442\u043e\u0439 \u043b\u0438\u0442\u0430\u0432\u0440\u044b", None));
        self.treeWidget_13.setSortingEnabled(__sortingEnabled26)

        ___qtreewidgetitem60 = self.treeWidget_14.headerItem()
        ___qtreewidgetitem60.setText(0, QCoreApplication.translate("MainWindow", u"\u00ab\u041b\u044f\u00bb \u0431\u043e\u043b\u044c\u0448\u043e\u0439 \u043e\u043a\u0442\u0430\u0432\u044b \u043d\u0430 \u0440\u0430\u0437\u043d\u044b\u0445 \u043b\u0438\u0442\u0430\u0432\u0440\u0430\u0445", None));

        __sortingEnabled27 = self.treeWidget_14.isSortingEnabled()
        self.treeWidget_14.setSortingEnabled(False)
        ___qtreewidgetitem61 = self.treeWidget_14.topLevelItem(0)
        ___qtreewidgetitem61.setText(0, QCoreApplication.translate("MainWindow", u"\u041d\u0430 \u043f\u0435\u0440\u0432\u043e\u0439 \u043b\u0438\u0442\u0430\u0432\u0440\u0435", None));
        ___qtreewidgetitem62 = self.treeWidget_14.topLevelItem(1)
        ___qtreewidgetitem62.setText(0, QCoreApplication.translate("MainWindow", u"\u041d\u0430 \u0432\u0442\u043e\u0440\u043e\u0439 \u043b\u0438\u0442\u0430\u0432\u0440\u0435", None));
        ___qtreewidgetitem63 = self.treeWidget_14.topLevelItem(2)
        ___qtreewidgetitem63.setText(0, QCoreApplication.translate("MainWindow", u"\u041d\u0430 \u0442\u0440\u0435\u0442\u044c\u0435\u0439 \u043b\u0438\u0442\u0430\u0432\u0440\u0435", None));
        self.treeWidget_14.setSortingEnabled(__sortingEnabled27)

        ___qtreewidgetitem64 = self.treeWidget_29.headerItem()
        ___qtreewidgetitem64.setText(0, QCoreApplication.translate("MainWindow", u"\u00ab\u041c\u0438\u00bb \u043c\u0430\u043b\u043e\u0439 \u043e\u043a\u0442\u0430\u0432\u044b \u043d\u0430 \u0440\u0430\u0437\u043d\u044b\u0445 \u043b\u0438\u0442\u0430\u0432\u0440\u0430\u0445", None));

        __sortingEnabled28 = self.treeWidget_29.isSortingEnabled()
        self.treeWidget_29.setSortingEnabled(False)
        ___qtreewidgetitem65 = self.treeWidget_29.topLevelItem(0)
        ___qtreewidgetitem65.setText(0, QCoreApplication.translate("MainWindow", u"\u041d\u0430 \u0442\u0440\u0435\u0442\u044c\u0435\u0439 \u043b\u0438\u0442\u0430\u0432\u0440\u0435", None));
        ___qtreewidgetitem66 = self.treeWidget_29.topLevelItem(1)
        ___qtreewidgetitem66.setText(0, QCoreApplication.translate("MainWindow", u"\u041d\u0430 \u0447\u0435\u0442\u0432\u0451\u0440\u0442\u043e\u0439 \u043b\u0438\u0442\u0430\u0432\u0440\u0435", None));
        ___qtreewidgetitem67 = self.treeWidget_29.topLevelItem(2)
        ___qtreewidgetitem67.setText(0, QCoreApplication.translate("MainWindow", u"\u041d\u0430 \u043f\u044f\u0442\u043e\u0439 \u043b\u0438\u0442\u0430\u0432\u0440\u0435", None));
        self.treeWidget_29.setSortingEnabled(__sortingEnabled28)

        ___qtreewidgetitem68 = self.treeWidget_30.headerItem()
        ___qtreewidgetitem68.setText(0, QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u043d\u044b\u043c\u0438 \u043f\u0430\u043b\u043e\u0447\u043a\u0430\u043c\u0438 \u043f\u043e \u043e\u0431\u044b\u0447\u043d\u043e\u0439 \u0437\u043e\u043d\u0435 \u043c\u0435\u043c\u0431\u0440\u0430\u043d\u044b", None));

        __sortingEnabled29 = self.treeWidget_30.isSortingEnabled()
        self.treeWidget_30.setSortingEnabled(False)
        ___qtreewidgetitem69 = self.treeWidget_30.topLevelItem(0)
        ___qtreewidgetitem69.setText(0, QCoreApplication.translate("MainWindow", u"\u041f\u0430\u043b\u043e\u0447\u043a\u0438 \u0434\u043b\u044f \u043b\u0438\u0442\u0430\u0432\u0440 \u0441 \u043c\u044f\u0433\u043a\u0438\u043c \u0444\u0438\u043b\u044c\u0446\u0435\u0432\u044b\u043c \u043d\u0430\u043a\u043e\u043d\u0435\u0447\u043d\u0438\u043a\u043e\u043c", None));
        ___qtreewidgetitem70 = self.treeWidget_30.topLevelItem(1)
        ___qtreewidgetitem70.setText(0, QCoreApplication.translate("MainWindow", u"\u041f\u0430\u043b\u043e\u0447\u043a\u0438 \u0434\u043b\u044f \u043b\u0438\u0442\u0430\u0432\u0440 \u0441 \u043f\u043e\u043b\u0443\u0436\u0451\u0441\u0442\u043a\u0438\u043c \u0444\u0438\u043b\u044c\u0446\u0435\u0432\u044b\u043c \u043d\u0430\u043a\u043e\u043d\u0435\u0447\u043d\u0438\u043a\u043e\u043c", None));
        ___qtreewidgetitem71 = self.treeWidget_30.topLevelItem(2)
        ___qtreewidgetitem71.setText(0, QCoreApplication.translate("MainWindow", u"\u041f\u0430\u043b\u043e\u0447\u043a\u0438 \u0434\u043b\u044f \u043b\u0438\u0442\u0430\u0432\u0440 \u0441 \u0436\u0451\u0441\u0442\u043a\u0438\u043c \u0444\u0438\u043b\u044c\u0446\u0435\u0432\u044b\u043c \u043d\u0430\u043a\u043e\u043d\u0435\u0447\u043d\u0438\u043a\u043e\u043c", None));
        ___qtreewidgetitem72 = self.treeWidget_30.topLevelItem(3)
        ___qtreewidgetitem72.setText(0, QCoreApplication.translate("MainWindow", u"\u041f\u0430\u043b\u043e\u0447\u043a\u0438 \u0434\u043b\u044f \u043a\u0441\u0438\u043b\u043e\u0444\u043e\u043d\u0430 \u0441 \u043c\u044f\u0433\u043a\u0438\u043c \u0440\u0435\u0437\u0438\u043d\u043e\u0432\u044b\u043c \u043d\u0430\u043a\u043e\u043d\u0435\u0447\u043d\u0438\u043a\u043e\u043c", None));
        ___qtreewidgetitem73 = self.treeWidget_30.topLevelItem(4)
        ___qtreewidgetitem73.setText(0, QCoreApplication.translate("MainWindow", u"\u041f\u0430\u043b\u043e\u0447\u043a\u0438 \u0434\u043b\u044f \u043a\u0441\u0438\u043b\u043e\u0444\u043e\u043d\u0430 \u0441 \u0436\u0451\u0441\u0442\u043a\u0438\u043c \u0440\u0435\u0437\u0438\u043d\u043e\u0432\u044b\u043c \u043d\u0430\u043a\u043e\u043d\u0435\u0447\u043d\u0438\u043a\u043e\u043c", None));
        ___qtreewidgetitem74 = self.treeWidget_30.topLevelItem(5)
        ___qtreewidgetitem74.setText(0, QCoreApplication.translate("MainWindow", u"\u041f\u0430\u043b\u043e\u0447\u043a\u0438 \u0434\u043b\u044f \u043c\u0430\u0440\u0438\u043c\u0431\u044b \u0441 \u043c\u044f\u0433\u043a\u0438\u043c \u043d\u0430\u043a\u043e\u043d\u0435\u0447\u043d\u0438\u043a\u043e\u043c", None));
        ___qtreewidgetitem75 = self.treeWidget_30.topLevelItem(6)
        ___qtreewidgetitem75.setText(0, QCoreApplication.translate("MainWindow", u"\u041f\u0430\u043b\u043e\u0447\u043a\u0438 \u0434\u043b\u044f \u043c\u0430\u0440\u0438\u043c\u0431\u044b \u0441 \u043f\u043e\u043b\u0443\u0436\u0451\u0441\u0442\u043a\u0438\u043c \u043d\u0430\u043a\u043e\u043d\u0435\u0447\u043d\u0438\u043a\u043e\u043c", None));
        ___qtreewidgetitem76 = self.treeWidget_30.topLevelItem(7)
        ___qtreewidgetitem76.setText(0, QCoreApplication.translate("MainWindow", u"\u041f\u0430\u043b\u043e\u0447\u043a\u0438 \u0434\u043b\u044f \u043c\u0430\u0440\u0438\u043c\u0431\u044b \u0441 \u0436\u0451\u0441\u0442\u043a\u0438\u043c \u043d\u0430\u043a\u043e\u043d\u0435\u0447\u043d\u0438\u043a\u043e\u043c", None));
        ___qtreewidgetitem77 = self.treeWidget_30.topLevelItem(8)
        ___qtreewidgetitem77.setText(0, QCoreApplication.translate("MainWindow", u"\u0411\u0430\u0440\u0430\u0431\u0430\u043d\u043d\u044b\u0435 \u043f\u0430\u043b\u043e\u0447\u043a\u0438", None));
        ___qtreewidgetitem78 = self.treeWidget_30.topLevelItem(9)
        ___qtreewidgetitem78.setText(0, QCoreApplication.translate("MainWindow", u"\u0420\u0443\u0442\u044b", None));
        ___qtreewidgetitem79 = self.treeWidget_30.topLevelItem(10)
        ___qtreewidgetitem79.setText(0, QCoreApplication.translate("MainWindow", u"\u0429\u0451\u0442\u043e\u0447\u043a\u0438", None));
        ___qtreewidgetitem80 = self.treeWidget_30.topLevelItem(11)
        ___qtreewidgetitem80.setText(0, QCoreApplication.translate("MainWindow", u"\u0414\u0440\u0435\u0432\u043a\u0438 \u043f\u0430\u043b\u043e\u0447\u0435\u043a \u0434\u043b\u044f \u043b\u0438\u0442\u0430\u0432\u0440 (\u0442\u043e\u043b\u0441\u0442\u044b\u0435)", None));
        ___qtreewidgetitem81 = self.treeWidget_30.topLevelItem(12)
        ___qtreewidgetitem81.setText(0, QCoreApplication.translate("MainWindow", u"\u0414\u0440\u0435\u0432\u043a\u0438 \u043f\u0430\u043b\u043e\u0447\u0435\u043a \u0434\u043b\u044f \u043a\u0441\u0438\u043b\u043e\u0444\u043e\u043d\u0430 (\u0442\u043e\u043d\u043a\u0438\u0435)", None));
        self.treeWidget_30.setSortingEnabled(__sortingEnabled29)

        ___qtreewidgetitem82 = self.treeWidget_31.headerItem()
        ___qtreewidgetitem82.setText(0, QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u043d\u044b\u043c\u0438 \u043f\u0430\u043b\u043e\u0447\u043a\u0430\u043c\u0438 \u0431\u043b\u0438\u0436\u0435 \u043a \u043a\u0440\u0430\u044e \u043c\u0435\u043c\u0431\u0440\u0430\u043d\u044b", None));

        __sortingEnabled30 = self.treeWidget_31.isSortingEnabled()
        self.treeWidget_31.setSortingEnabled(False)
        ___qtreewidgetitem83 = self.treeWidget_31.topLevelItem(0)
        ___qtreewidgetitem83.setText(0, QCoreApplication.translate("MainWindow", u"\u041f\u0430\u043b\u043e\u0447\u043a\u0438 \u0434\u043b\u044f \u043b\u0438\u0442\u0430\u0432\u0440 \u0441 \u043c\u044f\u0433\u043a\u0438\u043c \u0444\u0438\u043b\u044c\u0446\u0435\u0432\u044b\u043c \u043d\u0430\u043a\u043e\u043d\u0435\u0447\u043d\u0438\u043a\u043e\u043c", None));
        ___qtreewidgetitem84 = self.treeWidget_31.topLevelItem(1)
        ___qtreewidgetitem84.setText(0, QCoreApplication.translate("MainWindow", u"\u041f\u0430\u043b\u043e\u0447\u043a\u0438 \u0434\u043b\u044f \u043b\u0438\u0442\u0430\u0432\u0440 \u0441 \u043f\u043e\u043b\u0443\u0436\u0451\u0441\u0442\u043a\u0438\u043c \u0444\u0438\u043b\u044c\u0446\u0435\u0432\u044b\u043c \u043d\u0430\u043a\u043e\u043d\u0435\u0447\u043d\u0438\u043a\u043e\u043c", None));
        ___qtreewidgetitem85 = self.treeWidget_31.topLevelItem(2)
        ___qtreewidgetitem85.setText(0, QCoreApplication.translate("MainWindow", u"\u041f\u0430\u043b\u043e\u0447\u043a\u0438 \u0434\u043b\u044f \u043b\u0438\u0442\u0430\u0432\u0440 \u0441 \u0436\u0451\u0441\u0442\u043a\u0438\u043c \u0444\u0438\u043b\u044c\u0446\u0435\u0432\u044b\u043c \u043d\u0430\u043a\u043e\u043d\u0435\u0447\u043d\u0438\u043a\u043e\u043c", None));
        ___qtreewidgetitem86 = self.treeWidget_31.topLevelItem(3)
        ___qtreewidgetitem86.setText(0, QCoreApplication.translate("MainWindow", u"\u041f\u0430\u043b\u043e\u0447\u043a\u0438 \u0434\u043b\u044f \u043a\u0441\u0438\u043b\u043e\u0444\u043e\u043d\u0430 \u0441 \u043c\u044f\u0433\u043a\u0438\u043c \u0440\u0435\u0437\u0438\u043d\u043e\u0432\u044b\u043c \u043d\u0430\u043a\u043e\u043d\u0435\u0447\u043d\u0438\u043a\u043e\u043c", None));
        ___qtreewidgetitem87 = self.treeWidget_31.topLevelItem(4)
        ___qtreewidgetitem87.setText(0, QCoreApplication.translate("MainWindow", u"\u041f\u0430\u043b\u043e\u0447\u043a\u0438 \u0434\u043b\u044f \u043a\u0441\u0438\u043b\u043e\u0444\u043e\u043d\u0430 \u0441 \u0436\u0451\u0441\u0442\u043a\u0438\u043c \u0440\u0435\u0437\u0438\u043d\u043e\u0432\u044b\u043c \u043d\u0430\u043a\u043e\u043d\u0435\u0447\u043d\u0438\u043a\u043e\u043c", None));
        ___qtreewidgetitem88 = self.treeWidget_31.topLevelItem(5)
        ___qtreewidgetitem88.setText(0, QCoreApplication.translate("MainWindow", u"\u041f\u0430\u043b\u043e\u0447\u043a\u0438 \u0434\u043b\u044f \u043c\u0430\u0440\u0438\u043c\u0431\u044b \u0441 \u043c\u044f\u0433\u043a\u0438\u043c \u043d\u0430\u043a\u043e\u043d\u0435\u0447\u043d\u0438\u043a\u043e\u043c", None));
        ___qtreewidgetitem89 = self.treeWidget_31.topLevelItem(6)
        ___qtreewidgetitem89.setText(0, QCoreApplication.translate("MainWindow", u"\u041f\u0430\u043b\u043e\u0447\u043a\u0438 \u0434\u043b\u044f \u043c\u0430\u0440\u0438\u043c\u0431\u044b \u0441 \u043f\u043e\u043b\u0443\u0436\u0451\u0441\u0442\u043a\u0438\u043c \u043d\u0430\u043a\u043e\u043d\u0435\u0447\u043d\u0438\u043a\u043e\u043c", None));
        ___qtreewidgetitem90 = self.treeWidget_31.topLevelItem(7)
        ___qtreewidgetitem90.setText(0, QCoreApplication.translate("MainWindow", u"\u041f\u0430\u043b\u043e\u0447\u043a\u0438 \u0434\u043b\u044f \u043c\u0430\u0440\u0438\u043c\u0431\u044b \u0441 \u0436\u0451\u0441\u0442\u043a\u0438\u043c \u043d\u0430\u043a\u043e\u043d\u0435\u0447\u043d\u0438\u043a\u043e\u043c", None));
        ___qtreewidgetitem91 = self.treeWidget_31.topLevelItem(8)
        ___qtreewidgetitem91.setText(0, QCoreApplication.translate("MainWindow", u"\u0411\u0430\u0440\u0430\u0431\u0430\u043d\u043d\u044b\u0435 \u043f\u0430\u043b\u043e\u0447\u043a\u0438", None));
        ___qtreewidgetitem92 = self.treeWidget_31.topLevelItem(9)
        ___qtreewidgetitem92.setText(0, QCoreApplication.translate("MainWindow", u"\u0420\u0443\u0442\u044b", None));
        ___qtreewidgetitem93 = self.treeWidget_31.topLevelItem(10)
        ___qtreewidgetitem93.setText(0, QCoreApplication.translate("MainWindow", u"\u0429\u0451\u0442\u043e\u0447\u043a\u0438", None));
        ___qtreewidgetitem94 = self.treeWidget_31.topLevelItem(11)
        ___qtreewidgetitem94.setText(0, QCoreApplication.translate("MainWindow", u"\u0414\u0440\u0435\u0432\u043a\u0438 \u043f\u0430\u043b\u043e\u0447\u0435\u043a \u0434\u043b\u044f \u043b\u0438\u0442\u0430\u0432\u0440 (\u0442\u043e\u043b\u0441\u0442\u044b\u0435)", None));
        ___qtreewidgetitem95 = self.treeWidget_31.topLevelItem(12)
        ___qtreewidgetitem95.setText(0, QCoreApplication.translate("MainWindow", u"\u0414\u0440\u0435\u0432\u043a\u0438 \u043f\u0430\u043b\u043e\u0447\u0435\u043a \u0434\u043b\u044f \u043a\u0441\u0438\u043b\u043e\u0444\u043e\u043d\u0430 (\u0442\u043e\u043d\u043a\u0438\u0435)", None));
        self.treeWidget_31.setSortingEnabled(__sortingEnabled30)

        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Noto Sans'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Times New Roman'; font-size:14pt; color:#ffffff;\">\u0412 \u0430\u0443\u0434\u0438\u043e\u043f\u0440\u0438\u043c\u0435\u0440\u0435 \u0437\u0432\u0443\u043a \u0438\u0437\u0432\u043b\u0435\u043a\u0430\u0435\u0442\u0441\u044f \u043f\u0430\u043b\u043e\u0447\u043a\u0430\u043c\u0438 \u0434\u043b\u044f \u043b\u0438\u0442\u0430\u0432\u0440 \u0441 \u043f\u043e\u043b\u0443\u0436\u0451"
                        "\u0441\u0442\u043a\u0438\u043c \u0444\u0438\u043b\u044c\u0446\u0435\u0432\u044b\u043c \u043d\u0430\u043a\u043e\u043d\u0435\u0447\u043d\u0438\u043a\u043e\u043c. \u041f\u043e \u043e\u0431\u044b\u0447\u043d\u043e\u0439 \u0437\u043e\u043d\u0435 \u043c\u0435\u043c\u0431\u0440\u0430\u043d\u044b (\u0443 \u043b\u0438\u0442\u0430\u0432\u0440\u044b \u044d\u0442\u043e \u043d\u0435 \u0446\u0435\u043d\u0442\u0440 \u0438 \u043d\u0435 \u043a\u0440\u0430\u0439).</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">\u00a0</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Times New Roman'; font-size:14pt; color:#ffffff;\">\u0412 \u0430\u0443\u0434\u0438\u043e\u043f\u0440\u0438\u043c\u0435\u0440\u0435 \u0438\u043d\u0441\u0442\u0440\u0443\u043c\u0435\u043d\u0442 \u0437\u0432\u0443\u0447\u0438\u0442\u00a0"
                        "\u0432 \u0434\u0438\u0430\u043f\u0430\u0437\u043e\u043d\u0435 \u043e\u0442 \u00ab\u043c\u0438\u00bb \u0431\u043e\u043b\u044c\u0448\u043e\u0439 \u043e\u043a\u0442\u0430\u0432\u044b \u0434\u043e \u00ab\u0441\u0438\u00bb \u0431\u043e\u043b\u044c\u0448\u043e\u0439 \u043e\u043a\u0442\u0430\u0432\u044b.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Times New Roman'; font-size:12pt; color:#000000;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p st"
                        "yle=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bott"
                        "om:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent"
                        ":0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragr"
                        "aph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/newPrefix/\u041b\u0438\u0442\u0430\u0432\u0440\u044b_\u041f\u0435\u0440\u0432\u0430\u044f \u043b\u0438\u0442\u0430\u0432\u0440\u04303.jpg\" /></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u041c\u0435\u043c\u0431\u0440\u0430\u043d\u043d\u044b\u0435", None))

        __sortingEnabled31 = self.listWidget_23.isSortingEnabled()
        self.listWidget_23.setSortingEnabled(False)
        ___qlistwidgetitem14 = self.listWidget_23.item(0)
        ___qlistwidgetitem14.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0441\u0438\u043b\u043e\u0444\u043e\u043d, \u043c\u0430\u0440\u0438\u043c\u0431\u0430, \u0432\u0438\u0431\u0440\u0430\u0444\u043e\u043d, \u043a\u043e\u043b\u043e\u043a\u043e\u043b\u044c\u0447\u0438\u043a\u0438", None));
        ___qlistwidgetitem15 = self.listWidget_23.item(1)
        ___qlistwidgetitem15.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0441\u0438\u043b\u043e\u0444\u043e\u043d", None));
        ___qlistwidgetitem16 = self.listWidget_23.item(2)
        ___qlistwidgetitem16.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0440\u0438\u043c\u0431\u0430", None));
        ___qlistwidgetitem17 = self.listWidget_23.item(3)
        ___qlistwidgetitem17.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0431\u0440\u0430\u0444\u043e\u043d", None));
        ___qlistwidgetitem18 = self.listWidget_23.item(4)
        ___qlistwidgetitem18.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u043e\u043a\u043e\u043b\u044c\u0447\u0438\u043a\u0438 (\u0433\u043b\u043e\u043a\u0435\u043d\u0448\u043f\u0438\u043b\u044c)", None));
        ___qlistwidgetitem19 = self.listWidget_23.item(5)
        ___qlistwidgetitem19.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u043e\u043a\u043e\u043b\u0430", None));
        ___qlistwidgetitem20 = self.listWidget_23.item(6)
        ___qlistwidgetitem20.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0440\u043e\u0442\u0430\u043b\u0438", None));
        ___qlistwidgetitem21 = self.listWidget_23.item(7)
        ___qlistwidgetitem21.setText(QCoreApplication.translate("MainWindow", u"\u0424\u043b\u0435\u043a\u0441\u0430\u0442\u043e\u043d", None));
        ___qlistwidgetitem22 = self.listWidget_23.item(8)
        ___qlistwidgetitem22.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0432\u0435\u0441\u043d\u0430\u044f \u0442\u0430\u0440\u0435\u043b\u043a\u0430", None));
        ___qlistwidgetitem23 = self.listWidget_23.item(9)
        ___qlistwidgetitem23.setText(QCoreApplication.translate("MainWindow", u"\u0425\u0430\u0439-\u0445\u044d\u0442", None));
        ___qlistwidgetitem24 = self.listWidget_23.item(10)
        ___qlistwidgetitem24.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043d\u044b\u0435 \u0442\u0430\u0440\u0435\u043b\u043a\u0438", None));
        ___qlistwidgetitem25 = self.listWidget_23.item(11)
        ___qlistwidgetitem25.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0430\u043c-\u0442\u0430\u043c", None));
        ___qlistwidgetitem26 = self.listWidget_23.item(12)
        ___qlistwidgetitem26.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0440\u0435\u0443\u0433\u043e\u043b\u044c\u043d\u0438\u043a", None));
        ___qlistwidgetitem27 = self.listWidget_23.item(13)
        ___qlistwidgetitem27.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0435\u0440\u0435\u0432\u044f\u043d\u043d\u0430\u044f \u043a\u043e\u0440\u043e\u0431\u043e\u0447\u043a\u0430 (\u0432\u0443\u0434-\u0431\u043b\u043e\u043a)", None));
        ___qlistwidgetitem28 = self.listWidget_23.item(14)
        ___qlistwidgetitem28.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043b\u0430\u0441\u0442\u0438\u043a\u043e\u0432\u0430\u044f \u043a\u043e\u0440\u043e\u0431\u043e\u0447\u043a\u0430", None));
        ___qlistwidgetitem29 = self.listWidget_23.item(15)
        ___qlistwidgetitem29.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0440\u043e\u0432\u0438\u0439 \u043a\u043e\u043b\u043e\u043a\u043e\u043b\u044c\u0447\u0438\u043a (\u043a\u043e\u0432\u0431\u0435\u043b\u043b)", None));
        ___qlistwidgetitem30 = self.listWidget_23.item(16)
        ___qlistwidgetitem30.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0433\u043e\u0433\u043e", None));
        ___qlistwidgetitem31 = self.listWidget_23.item(17)
        ___qlistwidgetitem31.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0440\u0435\u0449\u043e\u0442\u043a\u0430", None));
        ___qlistwidgetitem32 = self.listWidget_23.item(18)
        ___qlistwidgetitem32.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0443\u0438\u0440\u043e", None));
        ___qlistwidgetitem33 = self.listWidget_23.item(19)
        ___qlistwidgetitem33.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u043e\u0445 \u0434\u043e\u0436\u0434\u044f", None));
        ___qlistwidgetitem34 = self.listWidget_23.item(20)
        ___qlistwidgetitem34.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u0440 \u0447\u0430\u0439\u043c\u0441", None));
        ___qlistwidgetitem35 = self.listWidget_23.item(21)
        ___qlistwidgetitem35.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0430\u0441\u0442\u0440\u0430", None));
        ___qlistwidgetitem36 = self.listWidget_23.item(22)
        ___qlistwidgetitem36.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0440\u0443\u0433\u0438\u0435 \u0438\u043d\u0441\u0442\u0440\u0443\u043c\u0435\u043d\u0442\u044b", None));
        self.listWidget_23.setSortingEnabled(__sortingEnabled31)

        self.textBrowser_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Noto Sans'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Times New Roman'; font-size:14pt; color:#ffffff;\">\u0412 \u0430\u0443\u0434\u0438\u043e\u043f\u0440\u0438\u043c\u0435\u0440\u0435 \u0437\u0432\u0443\u043a \u0438\u0437\u0432\u043b\u0435\u043a\u0430\u0435\u0442\u0441\u044f \u043f\u0430\u043b\u043e\u0447\u043a\u0430\u043c\u0438 \u0434\u043b\u044f \u043a\u0441\u0438\u043b\u043e\u0444\u043e\u043d\u0430 \u0441 \u043f\u043b\u0430"
                        "\u0441\u0442\u0438\u043a\u043e\u0432\u044b\u043c \u043d\u0430\u043a\u043e\u043d\u0435\u0447\u043d\u0438\u043a\u043e\u043c.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-lef"
                        "t:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0p"
                        "x;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/newPrefix/\u041a\u0441\u0438\u043b\u043e\u0444\u043e\u043d, \u043c\u0430\u0440\u0438\u043c\u0431\u0430, \u0432\u0438\u0431\u0440\u0430\u0444\u043e\u043d, \u043a\u043e\u043b\u043e\u043a\u043e\u043b\u044c\u0447\u0438\u043a\u0438_"
                        "\u041a\u0441\u0438\u043b\u043e\u0444\u043e2\u043d.jpg\" /></p></body></html>", None))
        ___qtreewidgetitem96 = self.treeWidget_32.headerItem()
        ___qtreewidgetitem96.setText(0, QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0442\u0438\u044f \u043a\u0441\u0438\u043b\u043e\u0444\u043e\u043d\u0430 \u0438\u0437 \u00ab\u041f\u0443\u0442\u0435\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044f\u2026\u00bb \u0411\u0440\u0438\u0442\u0442\u0435\u043d\u0430 \u043d\u0430 \u0440\u0430\u0437\u043d\u044b\u0445 \u0438\u043d\u0441\u0442\u0440\u0443\u043c\u0435\u043d\u0442\u0430\u0445", None));

        __sortingEnabled32 = self.treeWidget_32.isSortingEnabled()
        self.treeWidget_32.setSortingEnabled(False)
        ___qtreewidgetitem97 = self.treeWidget_32.topLevelItem(0)
        ___qtreewidgetitem97.setText(0, QCoreApplication.translate("MainWindow", u"\u041a\u0441\u0438\u043b\u043e\u0444\u043e\u043d", None));
        ___qtreewidgetitem98 = self.treeWidget_32.topLevelItem(1)
        ___qtreewidgetitem98.setText(0, QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0440\u0438\u043c\u0431\u0430", None));
        ___qtreewidgetitem99 = self.treeWidget_32.topLevelItem(2)
        ___qtreewidgetitem99.setText(0, QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0431\u0440\u0430\u0444\u043e\u043d", None));
        ___qtreewidgetitem100 = self.treeWidget_32.topLevelItem(3)
        ___qtreewidgetitem100.setText(0, QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u043e\u043a\u043e\u043b\u044c\u0447\u0438\u043a\u0438", None));
        self.treeWidget_32.setSortingEnabled(__sortingEnabled32)

        ___qtreewidgetitem101 = self.treeWidget_33.headerItem()
        ___qtreewidgetitem101.setText(0, QCoreApplication.translate("MainWindow", u"\u0422\u0430 \u0436\u0435 \u043f\u0430\u0440\u0442\u0438\u044f \u043d\u0430 \u043e\u043a\u0442\u0430\u0432\u0443 \u043d\u0438\u0436\u0435", None));

        __sortingEnabled33 = self.treeWidget_33.isSortingEnabled()
        self.treeWidget_33.setSortingEnabled(False)
        ___qtreewidgetitem102 = self.treeWidget_33.topLevelItem(0)
        ___qtreewidgetitem102.setText(0, QCoreApplication.translate("MainWindow", u"\u041a\u0441\u0438\u043b\u043e\u0444\u043e\u043d", None));
        ___qtreewidgetitem103 = self.treeWidget_33.topLevelItem(1)
        ___qtreewidgetitem103.setText(0, QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0440\u0438\u043c\u0431\u0430", None));
        ___qtreewidgetitem104 = self.treeWidget_33.topLevelItem(2)
        ___qtreewidgetitem104.setText(0, QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0431\u0440\u0430\u0444\u043e\u043d", None));
        ___qtreewidgetitem105 = self.treeWidget_33.topLevelItem(3)
        ___qtreewidgetitem105.setText(0, QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u043e\u043a\u043e\u043b\u044c\u0447\u0438\u043a\u0438", None));
        self.treeWidget_33.setSortingEnabled(__sortingEnabled33)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"\u0421\u0430\u043c\u043e\u0437\u0432\u0443\u0447\u0430\u0449\u0438\u0435", None))

        __sortingEnabled34 = self.listWidget_9.isSortingEnabled()
        self.listWidget_9.setSortingEnabled(False)
        ___qlistwidgetitem37 = self.listWidget_9.item(0)
        ___qlistwidgetitem37.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u044f\u043d", None));
        self.listWidget_9.setSortingEnabled(__sortingEnabled34)


        __sortingEnabled35 = self.listWidget_10.isSortingEnabled()
        self.listWidget_10.setSortingEnabled(False)
        ___qlistwidgetitem38 = self.listWidget_10.item(0)
        ___qlistwidgetitem38.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0440\u0433\u0430\u043d", None));
        self.listWidget_10.setSortingEnabled(__sortingEnabled35)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"\u0411\u0430\u044f\u043d \u0438 \u043e\u0440\u0433\u0430\u043d", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0441\u0438\u043b\u043e\u0444\u043e\u043d", None))
    # retranslateUi
