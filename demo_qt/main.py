from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, 
                            QLabel, QPushButton, QVBoxLayout) # (Horizontal)

app = QApplication([])
screen = QWidget()
screen.setWindowTitle('Identificador del ganador!')
screen.resize(640, 480)

# widgets
texto = QLabel('Soy un etiqueta de texto!')
ganador = QLabel('?')
boton = QPushButton('Generar')

# layout (Diseño)
main_layout = QVBoxLayout()
main_layout.addWidget(texto, alignment=Qt.AlignCenter)
main_layout.addWidget(ganador, alignment=Qt.AlignCenter)
main_layout.addWidget(boton, alignment=Qt.AlignCenter)

# ESTABLECER EL LAYOUT EN LA VENTANA
screen.setLayout(main_layout)

screen.show() # muestra el widget
app.exec_()