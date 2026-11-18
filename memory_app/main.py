from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QRadioButton, QGroupBox)

# APP
app = QApplication([])
screen = QWidget()
screen.setWindowTitle('Memory App')
screen.resize(400, 300)

# WIDGETS
texto_pregunta = QLabel('En que año fue lanzado Super Mario 64?')
boton = QPushButton('Responder')

botones_respuesta = QGroupBox('Opciones de Respuesta')
opcion_1 = QRadioButton('1996')
opcion_2 = QRadioButton('1998')
opcion_3 = QRadioButton('1991')
opcion_4 = QRadioButton('2000')

# DISEÑO DE LA CAJA DE BOTONES DE RADIO
layout_respuesta = QHBoxLayout()
col_1 = QVBoxLayout() # Columna para botones 1 y 2
col_1.addWidget(opcion_1)
col_1.addWidget(opcion_2)
col_2 = QVBoxLayout() # Columna para botones 3 y 4
col_2.addWidget(opcion_3)
col_2.addWidget(opcion_4)
# Estableciendo el layout de respuestas
layout_respuesta.addLayout(col_1)
layout_respuesta.addLayout(col_2)
botones_respuesta.setLayout(layout_respuesta)

# DISEÑO PARA LA CAJA DE MUESTRA DE INFORMACION
info_respuesta = QGroupBox('Resultado:')
texto_info = QLabel('Respuesta correcta o incorrecta')
texto_correcta = QLabel('Mostrar la respuesta correcta')

layout_info = QVBoxLayout()
layout_info.addWidget(texto_info, alignment=Qt.AlignLeft)
layout_info.addWidget(texto_correcta, alignment=Qt.AlignCenter)
info_respuesta.setLayout(layout_info)

# DISEÑO
main_layout = QVBoxLayout()
row_1 = QHBoxLayout() # Texto para la pregunta
row_1.addWidget(texto_pregunta, alignment= Qt.AlignCenter)
row_2 = QHBoxLayout() # Opciones de respuesta
row_2.addWidget(botones_respuesta)
row_2.addWidget(info_respuesta)
row_3 = QHBoxLayout() # Boton para validar
row_3.addWidget(boton, alignment= Qt.AlignCenter)

main_layout.addLayout(row_1)
main_layout.addLayout(row_2)
main_layout.addLayout(row_3)

info_respuesta.hide()
# botones_respuesta.hide() # ESCONDIENDO LA CAJA DE BOTONES

screen.setLayout(main_layout)

screen.show()
app.exec_()