from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        # Configurando o layout básico
        self.cw = QWidget()
        self.v_layout = QVBoxLayout()
        self.cw.setLayout(self.v_layout)
        self.setCentralWidget(self.cw)

        # Configurando título da janela
        self.setWindowTitle('Calculadora')

    def adjustFixedSize(self):
        # Ajustando janela ao conteúdo
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())
