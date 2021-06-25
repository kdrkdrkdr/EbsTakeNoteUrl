# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, SIGNAL, QThread)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


import chromedriver_autoinstaller
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.common import exceptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from subprocess import CREATE_NO_WINDOW

import os, pathlib
from time import sleep
from requests import get, exceptions




class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle("EBS 온클 필기를 위한 링크 열기 프로그램")
        QObject.connect(self.extractBtn, SIGNAL('clicked()'), self.extractUrl)
        
        self.options = Options()
        self.options.add_argument(f"--user-data-dir={pathlib.Path.home()}\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
        self.options.add_experimental_option("excludeSwitches" , ["enable-automation", "load-extension", "enable-logging"])


        os.system('taskkill /f /im chromedriver.exe')
        self.path = chromedriver_autoinstaller.install('./')
        self.chrome_service = ChromeService(self.path)
        self.chrome_service.creationflags = CREATE_NO_WINDOW
        self.driver = Chrome(options=self.options, service=self.chrome_service)
        self.driver.get('https://www.ebsoc.co.kr/')

        
        self.show()



    def extractUrl(self):
        iframe_player = self.driver.find_element(By.XPATH, '//*[@id="player"]')
        self.driver.switch_to.frame(iframe_player)
        sleep(2)

        try:
            apiLink = self.driver.find_element(By.ID, 'lx-player_html5_api')
        except:
            apiLink = self.driver.find_element(By.ID, 'lx-player_youtube_api')


        final_url = apiLink.get_attribute('src')

        self.driver.switch_to.default_content()
        self.linkBox.setText(final_url)





    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(694, 79)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.extractBtn = QPushButton(self.centralwidget)
        self.extractBtn.setObjectName(u"extractBtn")
        self.extractBtn.setGeometry(QRect(10, 5, 121, 51))
        self.linkBox = QLineEdit(self.centralwidget)
        self.linkBox.setObjectName(u"linkBox")
        self.linkBox.setGeometry(QRect(140, 33, 541, 20))
        self.msg = QLabel(self.centralwidget)
        self.msg.setObjectName(u"msg")
        self.msg.setGeometry(QRect(141, 10, 541, 16))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.extractBtn.setText(QCoreApplication.translate("MainWindow", u"ebs \uc628\ud074\n"
"\ud544\uae30\uac00 \ud3b8\ud55c\n"
"\uc601\uc0c1 \ub9c1\ud06c \uc5f4\uae30", None))
        self.linkBox.setText("")
        self.msg.setText(QCoreApplication.translate("MainWindow", u"\ub9c1\ud06c\ub97c \uc5bb\uace0 \uc2f6\uc740 \ub3d9\uc601\uc0c1\uc774 \uc788\ub294 \uac15\uc88c\uc5d0 \ub4e4\uc5b4\uac04 \ud6c4 \uc606 \ubc84\ud2bc\uc744 \ub204\ub974\uc2dc\uba74 \uc544\ub798 \uc0c1\uc790\uc5d0 \ub9c1\ud06c\uac00 \ub098\uc635\ub2c8\ub2e4.", None))
    # retranslateUi










if __name__ in '__main__':
    import sys
    app = QApplication(sys.argv)
    e = Ui_MainWindow()
    e.show()
    app.exec_()
    e.driver.quit()
    sys.exit()