import os
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.utils import platform
from controle import funcao_transferencia, malha_aberta_degrau, parametros_sistema
import matplotlib.pyplot as plt

class TransferFunctionApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        
        self.label_num = Label(text='Numerador (separado por vírgulas)')
        self.layout.add_widget(self.label_num)
        
        self.input_num = TextInput(multiline=False)
        self.layout.add_widget(self.input_num)
        
        self.label_den = Label(text='Denominador (separado por vírgulas)')
        self.layout.add_widget(self.label_den)
        
        self.input_den = TextInput(multiline=False)
        self.layout.add_widget(self.input_den)
        
        self.button = Button(text='Criar Função de Transferência')
        self.button.bind(on_press=self.create_transfer_function)
        self.layout.add_widget(self.button)
        
        self.image = Image()
        self.layout.add_widget(self.image)

        self.image = Image(size_hint=(1, None), height=500)  # Ajuste o tamanho conforme necessário
        self.layout.add_widget(self.image)
        
        return self.layout

    def create_transfer_function(self, instance):
        num_str = self.input_num.text
        den_str = self.input_den.text
        
        try:
            num = [float(n) for n in num_str.split(',')]
            den = [float(d) for d in den_str.split(',')]
            
            # Criação da função de transferência
            tf = funcao_transferencia(num, den)
            
            # Define o caminho relativo para salvar a imagem baseado na plataforma
            if platform == 'android':
                # Usar caminho específico para Android
                storage_dir = storagepath.get_app_storage_dir() or '/sdcard/Download'
                filepath = os.path.join(storage_dir, 'step_response_android.png')
            elif platform == 'ios':
                # Usar caminho específico para iOS
                from os.path import expanduser
                home = expanduser('~')
                filepath = os.path.join(home, 'Documents', 'step_response_ios.png')
            else:
                # Para desenvolvimento no PC
                current_dir = os.path.dirname(os.path.abspath(__file__))
                filepath = os.path.join(current_dir, 'step_response_desktop.png')
            
            # Chamar a função da sua biblioteca para gerar a imagem
            malha_aberta_degrau(tf)

            # Salvar a imagem no caminho especificado
            plt.savefig(filepath)
            plt.close()

            # Print de depuração para verificar o caminho do arquivo
            print(f"Imagem salva em: {filepath}")
            
            # Carregar a imagem no widget de imagem
            self.image.source = filepath
            self.image.reload()

            # Print de depuração para verificar se a imagem foi carregada
            print(f"Imagem carregada no widget: {self.image.source}")
        except ValueError:
            self.show_error('Erro: Por favor, insira números válidos.')

    def show_error(self, message):
        self.layout.add_widget(Label(text=message))

if __name__ == '__main__':
    TransferFunctionApp().run()
