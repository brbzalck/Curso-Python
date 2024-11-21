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
                                QMainWindow)


app = QApplication(sys.argv)
window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)
window.setWindowTitle('Interface gráfica com PySide6')


botao = QPushButton('Texto do botão')
botao.setStyleSheet('font-size: 30px; color:green')

botao2 = QPushButton('Texto do botão2')
botao.setStyleSheet('font-size: 30px; color:dark-cyan')

botao3 = QPushButton('Texto do botão3')
botao3.setStyleSheet('font-size: 30px; color:red')


layout = QGridLayout()
central_widget.setLayout(layout)

layout.addWidget(botao, 1, 1)
layout.addWidget(botao2, 2, 1, 1, 2)
# 2=Linha, 1=Coluna, 1=spanLinha, 2=spanColuna
layout.addWidget(botao3, 1, 2)

@Slot()
def slot_example(status_bar):
    def inner():
        status_bar.showMessage('O meu slot foi executado')
    return inner


@Slot()
def outro_slot(checked):
    print('Está marcado? ', checked)

@Slot()
def terceiro_slot(action):
    def inner():
        outro_slot(action.isChecked()) # Retorna um Bool 
    return inner

# staturBar
status_bar = window.statusBar()
status_bar.showMessage('Mostrar mensagem na barra')

# menuBar
menu = window.menuBar()
primeiro_menu = menu.addMenu('Primeiro menu')
primeira_acao = primeiro_menu.addAction('Primeira ação')
# Usando a lambda para executar a função slot_example
# com o argumento status_bar
primeira_acao.triggered.connect(slot_example(status_bar))

segunda_acao = primeiro_menu.addAction('Segunda ação')
segunda_acao.setCheckable(True)
segunda_acao.toggled.connect(outro_slot)
segunda_acao.hovered.connect(terceiro_slot(segunda_acao))

botao.clicked.connect(terceiro_slot(segunda_acao))

window.show()
app.exec()
