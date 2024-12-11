from PySide6.QtWidgets import QApplication, QWidget
from ui_workerui import Ui_myWidget
import sys
import time


class MyWidget(QWidget, Ui_myWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.button1.clicked.connect(self.hardWorker1)
        self.button2.clicked.connect(self.hardWorker2)

    def hardWorker1(self):
        for i in range(5):
            print(i)
            time.sleep(1)
        self.label1.setText('1 terminado')

    def hardWorker2(self):
        for i in range(5):
            print(i)
            time.sleep(1)
        self.label2.setText('2 terminado')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWidget = MyWidget()
    myWidget.show()
    app.exec()