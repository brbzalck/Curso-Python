import sys

from PySide6.QtGui import QIcon
from variables import WINDOW_ICON_PATH
from PySide6.QtWidgets import QApplication
from info import Info
from display import Display
from main_window import MainWindow
from styles import setupTheme
from buttons import ButtonsGrid

if __name__ == '__main__':
    app = QApplication(sys.argv)
    setupTheme(app)
    window = MainWindow()

    # Define Ícone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)
    if sys.platform.startswith('win'):
        import ctypes
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
            u'CompanyName.ProductName.SubProduct.VersionInformation')

    # Info
    info = Info('Sua conta')
    window.addWidgetToVLayout(info)

    # Display
    display = Display()
    window.addWidgetToVLayout(display)

    # Grid
    buttonsGrid = ButtonsGrid(display, info, window)
    window.vLayout.addLayout(buttonsGrid)

    window.adjustFixedSize()
    window.show()
    app.exec()
