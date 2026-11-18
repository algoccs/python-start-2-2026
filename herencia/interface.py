from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QRadioButton, QMessageBox 

def show_correct():
    victory_screen = QMessageBox()
    victory_screen.setText('Correcto! Ganaste una PS5 Pro!')
    victory_screen.exec_()

def show_wrong():
    lose_screen = QMessageBox()
    lose_screen.setText('Incorrecto, Gracias por participar!')
    lose_screen.exec_()


app = QApplication([])
window = QWidget()
window.setWindowTitle('Competición de Crazy People!')
window.resize(400, 200)

# WIDGETS
pregunta = QLabel('En que año se lanzo Pokemon?')
radio_1 = QRadioButton('1996') # RESPUESTA CORRECTA
radio_2 = QRadioButton('2000')
radio_3 = QRadioButton('1998')
radio_4 = QRadioButton('1991')

# DISEÑO
main_layout = QVBoxLayout() # Layout principal (orientacion vertical)
row_1 = QHBoxLayout() # Fila de botones 1
# Incorporando los elementos al layout
row_1.addWidget(radio_1, alignment=Qt.AlignCenter) 
row_1.addWidget(radio_2, alignment=Qt.AlignCenter)
row_2 = QHBoxLayout() # Fila de botones 2
row_2.addWidget(radio_3, alignment=Qt.AlignCenter)
row_2.addWidget(radio_4, alignment=Qt.AlignCenter)

# Establecer el layout principal
main_layout.addWidget(pregunta, alignment=Qt.AlignCenter)
main_layout.addLayout(row_1)
main_layout.addLayout(row_2)
window.setLayout(main_layout)

# FUNCIONALIDAD
radio_1.clicked.connect(show_correct)
radio_2.clicked.connect(show_wrong)
radio_3.clicked.connect(show_wrong)
radio_4.clicked.connect(show_wrong)

window.show()
app.exec_()

