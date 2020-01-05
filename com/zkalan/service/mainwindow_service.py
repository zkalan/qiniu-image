# -*- coding: utf-8 -*-

import sys, os
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from ui import mainwindow
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QFileDialog
from utils import uploadtoqiniu


class WindowService(QMainWindow, mainwindow.Ui_MainWindow):
    def __init__(self):
        super(WindowService, self).__init__()
        self.setupUi(self)
        # bind slots and signals
        self.pb_select.clicked.connect(self.pb_select_service)

        self.pb_copy_url.clicked.connect(self.pb_copy_url_service)
        self.pb_copy_markdown.clicked.connect(self.pb_copy_markdown_service)
        self.pb_upload.clicked.connect(self.pb_upload_service)

    def le_selectimage_service(self):
        pass

    def pb_select_service(self):
        filename, filetype = QFileDialog.getOpenFileName(self,
                                                         '选择文件',
                                                         os.getcwd(),
                                                         "Images (*.jpg;*.jpeg;*.gif;*.png;*.ico);;All Files (*)")
        if filename == '':
            print('filename is' + filename)
            return
        self.le_selectimage.setText(filename)
        print('filename is' + filename)
        print('文件筛选器类型：', filetype)

    def pb_upload_service(self):
        filepath = self.le_selectimage.text()
        if filepath == '':
            self.maessage_box('select a image')
        else:
            if os.path.exists('settings.cfg'):
                back_url = uploadtoqiniu.upload(filepath)
                self.le_url.setText(back_url)
                self.le_md.setText('![](' + back_url + ')')

                img = QtGui.QImage(filepath)
                scale = img.size().width()/411 if ((img.size().width()/411) > (img.size().height()/201)) else img.size().height()/201
                scale_width = img.size().width()/scale
                scale_height = img.size().height() / scale
                size = QtCore.QSize(scale_width, scale_height)

                image = QtGui.QPixmap.fromImage(img.scaled(size, QtCore.Qt.IgnoreAspectRatio))
                self.l_preview.setPixmap(image)
                print(image.size())
                print(type(image.size()))

                self.maessage_box('Success')
            else:
                self.maessage_box('check setting.cfg')

    def le_url_service(self):
        pass

    def pb_copy_url_service(self):
        clipboard = QApplication.clipboard()
        url = self.le_url.text()
        clipboard.setText(url)
        self.maessage_box('copy to clipkboard')

    def le_md_service(self):
        pass

    def pb_copy_markdown_service(self):
        clipboard = QApplication.clipboard()
        md_url = self.le_md.text()
        clipboard.setText(md_url)
        self.maessage_box('copy to clipkboard')

    def tb_response_text_service(self):
        pass

    def maessage_box(self, message, title='information'):
        box = QMessageBox(self)
        box.setIcon(QMessageBox.Information)
        box.setText(message)
        box.setWindowTitle(title)
        box.setStandardButtons(QMessageBox.Ok)
        box.button(QMessageBox.Ok).animateClick(2*1000)
        box.exec_()
