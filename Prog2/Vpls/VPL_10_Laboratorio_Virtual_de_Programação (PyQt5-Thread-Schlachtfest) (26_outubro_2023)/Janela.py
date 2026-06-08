import sys
from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QGridLayout
from PyQt5.QtGui import QColor
from ThreadSchlacht import ThreadSchlacht

class Janela(QWidget):
    _LEd1 = None
    _LEd2 = None
    _LEd3 = None
    _Bt_Abertura = None
    _Bt_Fechamento = None
    Barraca1 = None
    Barraca2 = None
    Barraca3 = None

    def __init__(self, Str="Janela", x1=400, y1=200, dx=640, dy=480, cor="orange"):
        super().__init__()
        self.setWindowTitle(Str)
        self.setGeometry(x1, y1, dx, dy)
        self.setAutoFillBackground(True)
        
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor(cor))
        self.setPalette(p)
        
        self.inicialize()

    def closeEvent(self, event):
        self.Barraca1.parar()
        self.Barraca2.parar()
        self.Barraca3.parar()
        self.destroy()
        sys.exit(0)

    def action_abertura(self):
        self.Barraca1.iniciar(60)
        self.Barraca2.iniciar(60)
        self.Barraca3.iniciar(60)

    def action_fechamento(self):
        self.Barraca1.parar()
        self.Barraca2.parar()
        self.Barraca3.parar()

    def inicialize(self):
        grid = QGridLayout()
        self.setLayout(grid)

        self._LEd1 = QLineEdit()
        self._LEd2 = QLineEdit()
        self._LEd3 = QLineEdit()

        self._LEd1.setText('0')
        self._LEd2.setText('0')
        self._LEd3.setText('0')

        self._Bt_Abertura = QPushButton('Abertura')
        self._Bt_Fechamento = QPushButton('Fechamento')

        self._Bt_Abertura.clicked.connect(self.action_abertura)
        self._Bt_Fechamento.clicked.connect(self.action_fechamento)

        # Adicionando os componentes ao Layout para que apareçam na tela
        grid.addWidget(self._LEd1, 0, 0)
        grid.addWidget(self._LEd2, 0, 1)
        grid.addWidget(self._LEd3, 0, 2)
        grid.addWidget(self._Bt_Abertura, 1, 0, 1, 3)
        grid.addWidget(self._Bt_Fechamento, 2, 0, 1, 3)

        self.Barraca1 = ThreadSchlacht(self._LEd1)
        self.Barraca2 = ThreadSchlacht(self._LEd2)
        self.Barraca3 = ThreadSchlacht(self._LEd3)
