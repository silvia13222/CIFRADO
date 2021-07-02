#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.loader import Loader
from kivy.uix.image import Image
from kivy.properties import StringProperty, BoundedNumericProperty
from kivy.lang import Builder




class WidgetExample(GridLayout):

    button_text = StringProperty("Cifra/descifra")
    input_text = StringProperty('Iholflgdghv, qrydwr, ho ghfrglilfdgru gh VKLHOG ixqflrqd')
    label_text = StringProperty('Aquí queda descifrado tu codigo')
    clave = BoundedNumericProperty(0, min=-26, max=26)

    def show_slider(self, widget): #metodo
        self.clave = widget.value
        print(widget.value)


    def Cifra(self, input_text, clave=-3):
        buff = []
        for c in input_text:
            num = ord(c)
            if 65 <= num < 91:
                new_num = ((num - 65 + clave) % 26) + 65
                buff.append(str(chr(new_num)))
            elif 97 <= num < 123:
                new_num = ((num - 97 + clave) % 26) + 97
                buff.append(str(chr(new_num)))
            else:
                buff.append(c)
        return ''.join(buff)


    def do_descifrar(self):
        inputtext = self.input_text  #texto a descifrar
        clave = self.clave  #clave de cifrado
        
        outputtext = self.Cifra(inputtext, clave)
        self.label_text = outputtext  #texto descifrado


class app_cifraApp(App):
    pass


def main():
    
    app = app_cifraApp()
    app.run()


if __name__ == '__main__':
    main()