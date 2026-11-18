class Title():
    #constructor
    def __init__(self, texto, cor_x, cor_y):
        self.texto = texto
        self.cor_x =cor_x
        self.cor_y =cor_y
        self.visibility = True
    #metodos
    def print_info(self):
        print('Boton:', self.texto)
        print('Ubicacion:', (self.cor_x, self.cor_y))
        print('Visibilidad:', self.visibility)

    def hide(self):
        self.visibility = False
    def show(self):
        self.visibility = True

#crear 2 etiquetas (objetos)
boton_1 = Title('Descubre al ganador ahora mismo', 150, 150)
boton_2 = Title('Solo puede haber un ganador!', 150, -100)
boton_1.print_info()
#ocultar 2da etiqueta
boton_2.hide()
boton_2.print_info()