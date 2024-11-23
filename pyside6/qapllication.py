# QApplication e QPushButton de PySide6.QtWidgets
# QApplication -> O Widget principal da aplicação
# QPushButton -> Um botão
# PySide6.QtWidgets -> Onde estão os widgets do PySide6

# QMainWindow e centralWidget
# -> QApplication (app)
#   -> QMainWindow (window->setCentralWidget)
#       -> CentralWidget (central_widget)
#           -> Layout (layout)
#               -> Widget 1 (botao1)
#               -> Widget 2 (botao2)
#               -> Widget 3 (botao3)
#   -> show
# -> exec
import sys

from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication, QPushButton, QWidget, QGridLayout,
                                QMainWindow) # noqa


class MyWindow(QMainWindow):
    def __init__(self, parent=None):
        # Pegando o init da herança QMainWindow
        super().__init__(parent)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.setWindowTitle('Interface gráfica com PySide6')

        self.botao1 = self.make_button('Texto do botão')
        self.botao1.clicked.connect(self.segunda_acao_marcada)
        self.botao2 = self.make_button('Botão Dois')
        self.botao3 = self.make_button('Botão Três')

        self.grid_layout = QGridLayout()
        self.central_widget.setLayout(self.grid_layout)

        self.grid_layout.addWidget(self.botao1, 1, 1)
        self.grid_layout.addWidget(self.botao2, 2, 1, 1, 2)
        # 2=Linha, 1=Coluna, 1=spanLinha, 2=spanColuna
        self.grid_layout.addWidget(self.botao3, 1, 2)

        # staturBar
        self.status_bar = self.statusBar()
        self.status_bar.showMessage('Mostrar mensagem na barra')

        # menuBar
        self.menu = self.menuBar()
        self.primeiro_menu = self.menu.addMenu('Primeiro menu')
        self.primeira_acao = self.primeiro_menu.addAction('Primeira ação')
        # Usando a lambda para executar a função slot_example
        # com o argumento status_bar
        self.primeira_acao.triggered.connect(self.muda_msg_sttsbar)

        self.segunda_acao = self.primeiro_menu.addAction('Segunda ação')
        self.segunda_acao.setCheckable(True)
        self.segunda_acao.toggled.connect(self.segunda_acao_marcada)
        self.segunda_acao.hovered.connect(self.segunda_acao_marcada)

    @Slot()
    def muda_msg_sttsbar(self):
        self.status_bar.showMessage('O meu slot foi executado')

    @Slot()
    def segunda_acao_marcada(self):
        print('Está marcado? ', self.segunda_acao.isChecked())

    def make_button(self, text):
        btn = QPushButton(text)
        btn.setStyleSheet('font-size: 30px; color:green')
        return btn


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec()
