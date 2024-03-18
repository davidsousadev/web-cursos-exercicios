import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

class SimpleApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        # Define a geometria da janela
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle('Aplicativo Simples em PyQt')
        
        # Cria um botão
        self.button = QPushButton('Clique Aqui', self)
        
        # Conecta o sinal "clicked" do botão ao método "buttonClicked"
        self.button.clicked.connect(self.buttonClicked)
        
        # Cria um layout vertical e adiciona o botão a ele
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        
        # Define o layout da janela
        self.setLayout(layout)
        
    def buttonClicked(self):
        # Define o que acontece quando o botão é clicado
        print('Botão clicado!')
        
if __name__ == '__main__':
    # Cria a aplicação
    app = QApplication(sys.argv)
    
    # Cria a instância do aplicativo
    ex = SimpleApp()
    
    # Exibe a janela
    ex.show()
    
    # Executa a aplicação
    sys.exit(app.exec_())
