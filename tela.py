import PySimpleGUI as sg
from cifra_de_cesar import cifra_de_cesar

class Tela:
    def __init__ (self):
        sg.change_look_and_feel("Topanga")
        # *Layout
        layout = [
            [sg.Text("Bem vindo ao codificador / decodificador de Cifra de César")],
            [sg.Text("Sua mensagem:", size=(15,0)), sg.Input(size=(28,0), key="mensagem")],
            [sg.Text("Ação:", size=(15,0)), sg.Radio("Codificar", "acao", size=(9,0), key="codificar"), sg.Radio("Decodificar", "acao", size=(9,0), key="decodificar")],
            [sg.Text("Deslocamento:", size=(15,0)), sg.Input(size=(28,0), key="deslocamento")],
            [sg.Button("Confirmar")],
            [sg.Text("Mensagem Codificada:")],
            [sg.Output(size=(46,10))],
            [sg.Image(filename=("img\julio_cesar.png"))]
        ]
        # *Janela
        self.janela = sg.Window("Cifra de César", size=(500,750), element_justification='center').layout(layout)
        # *Extrair dados da tela

    def define_acao (self):
        if self.values["codificar"] == True:
            return 'c'
        elif self.values["decodificar"] == True:
            return 'd'

    def Iniciar (self):
        while True:
            self.button, self.values = self.janela.Read()
            self.values["acao"] = self.define_acao()
            self.values.pop("decodificar")
            self.values.pop("codificar")
            palavra_codificada = cifra_de_cesar(self.values["mensagem"], int(self.values["deslocamento"]), self.values["acao"])
            print(palavra_codificada)


def main():
    tela = Tela()
    tela.Iniciar()


if __name__ == '__main__':
    main()
