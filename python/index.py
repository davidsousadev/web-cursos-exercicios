# Importando os módulos necessários do Kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

# Definindo a classe principal do aplicativo
class SimpleApp(App):
    
    # Método para construir a interface do usuário
    def build(self):
        # Criando um layout de caixa vertical
        layout = BoxLayout(orientation='vertical')
        
        # Criando um rótulo de texto
        self.label = Label(text="Clique no botão para exibir uma mensagem")
        
        # Criando um botão
        button = Button(text="Clique Aqui!")
        button.bind(on_press=self.on_button_click)  # Vinculando o evento de clique do botão
        
        # Adicionando os widgets ao layout
        layout.add_widget(self.label)
        layout.add_widget(button)
        
        return layout
    
    # Método chamado quando o botão é clicado
    def on_button_click(self, instance):
        self.label.text = "Olá, Mundo!"

# Instanciando e executando o aplicativo
if __name__ == "__main__":
    SimpleApp().run()
