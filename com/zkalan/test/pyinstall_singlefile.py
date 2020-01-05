# -*- coding: utf-8 -*-
import sys, os
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']


if __name__ == '__main__':
    from PyInstaller.__main__ import run
    opts = ['demo.py', '-w', '-F', '-c', '--icon=favicon.ico']
    run(opts)
