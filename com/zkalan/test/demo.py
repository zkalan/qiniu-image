import sys, os
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from service import mainwindow_service
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = mainwindow_service.WindowService()
    ui.show()
    sys.exit(app.exec_())


