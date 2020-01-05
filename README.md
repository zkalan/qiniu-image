---
title: PyQt5小程序上传图片到七牛云
date: 2020-01-05 21:50:18
author: 团麻
categories:
- PyQt5
tags:
- pyqt5
- python
- 七牛云
- pyinstaller
- pycharm
---

>github地址
>https://github.com/zkalan/qiniu-image.git

## 绘制软件界面

使用Qt Designer绘制程序界面，设置图标，修改控件id等。这个过程还包括几个配置步骤：

- 在pycharm中安装PyQt5
- 在pycharm中安装PyQt5-tools
- 配置pycharm，方便的通过tools界面启动dedigner和其他工具

## slots和signals

这是两个PyQt中的概念，signal就是信号，是动作的发出者；slot就是槽，是动作的相应者。代码如下：

```python
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

    def pb_copy_url_service(self):
        clipboard = QApplication.clipboard()
        url = self.le_url.text()
        clipboard.setText(url)
        self.maessage_box('copy to clipkboard')

    def pb_copy_markdown_service(self):
        clipboard = QApplication.clipboard()
        md_url = self.le_md.text()
        clipboard.setText(md_url)
        self.maessage_box('copy to clipkboard')

    def maessage_box(self, message, title='information'):
        box = QMessageBox(self)
        box.setIcon(QMessageBox.Information)
        box.setText(message)
        box.setWindowTitle(title)
        box.setStandardButtons(QMessageBox.Ok)
        box.button(QMessageBox.Ok).animateClick(2*1000)
        box.exec_()
```

## 使用pyinstaller打包

pyinstaller打包总是问题百出，PyQt5自己也有不少bug。遇到这些问题

### ImportError: unable to find Qt5Core.dll on PATH

解决办法如下

>https://blog.csdn.net/zwyact/article/details/99778898
>在主程序中pyqt5库import之前就对系统变量进行手动设置

```python
import sys, os
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
```

### NameError: name 'exit' is not defined

解决办法就是这样写sys.exit

## 效果预览

settings.cfg是配置文件，其中需要配置各个字段。可以配置是否使用水印。

### 主界面

![](http://cdn.zkalan.com/VJOdMYuW8Ti4om0gBQvx08Ckr44=/FnGYihfO9pvjDnA77RSIAtexgUkK)

### 上传图片

上传完图片还能快速获取访问链接。

![](http://cdn.zkalan.com/VJOdMYuW8Ti4om0gBQvx08Ckr44=/FmM6w11zg5p5KhkNlnekF3mYpT6a)

>github地址
>https://github.com/zkalan/qiniu-image.git
