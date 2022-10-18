from Tela_login import Ui_Tela_login
from Tela_inicio import Ui_Tela_inicio
from Tela_cadastro import Ui_Cadastro
from Tela_editar import Ui_Editar
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import *
import sys


class Classe_Inicio(QMainWindow):
    from Func_telas import tela_pacientes
    from Func_telas import tela_inicio
    from Func_Inicio import abrir_cadastro
    from Func_Inicio import sair_inicio
    from Func_Inicio import expaandir_left_menu
    def __init__(self):
        super().__init__()
        self.janela_inicio = Ui_Tela_inicio()
        self.janela_inicio.setupUi(self)
        self.cadastro = Classe_cadastro()
        
    
        ################## - BOTÕES - INÍCIO - ##################
        self.janela_inicio.Bt_cadastro.clicked.connect(self.abrir_cadastro)
        self.janela_inicio.Bt_sair.clicked.connect(self.sair_inicio)
        self.janela_inicio.Bt_Expandir.clicked.connect(self.expaandir_left_menu)
        self.janela_inicio.Bt_Inicio.clicked.connect(
        lambda: self.janela_inicio.stackedWidget.setCurrentWidget(self.tela_inicio()))
        self.tela_inicio()
        self.janela_inicio.Bt_Cadastro.clicked.connect(
        lambda: self.janela_inicio.stackedWidget.setCurrentWidget(self.tela_pacientes()))
        self.tela_pacientes()


class Classe_login(QMainWindow):
    from Func_banco import conectar
    from Func_banco import desconectar
    from Func_banco import inserir_dados
    from Func_telas import tela_banco
    from Func_telas import tela_login
    from Func_entrar import entrar
    from Func_entrar import start
    def __init__(self):
        super().__init__()
        self.janela_login = Ui_Tela_login()
        self.janela_login.setupUi(self)
        self.inicio = Classe_Inicio()
          
        
        ################## - BOTÕES - LOGIN - ##################
        self.janela_login.Bt_Login.clicked.connect(self.entrar)
        self.janela_login.config_banco.clicked.connect(
        lambda: self.janela_login.stackedWidget.setCurrentWidget(self.tela_banco()))
        self.tela_banco()
        self.janela_login.Bt_Tela_Login.clicked.connect(
        lambda: self.janela_login.stackedWidget.setCurrentWidget(self.tela_login()))
        self.tela_login()
        self.janela_login.Bt_Conectar.clicked.connect(self.inserir_dados)
        self.janela_login.Bt_Desconectar.clicked.connect(self.desconectar)
         

class Classe_editar (QMainWindow):
    def __init__(self):
        super().__init__()
        self.janela_editar = Ui_Editar()
        self.janela_editar.setupUi(self)
        

class Classe_cadastro (QMainWindow):
    from Func_cadastro import inserir_cadastro
    from Func_cadastro import alerta
    def __init__(self):
        super().__init__()
        self.janela_cadastro = Ui_Cadastro()
        self.janela_cadastro.setupUi(self)   
        self.janela_cadastro.bt_Salvar.clicked.connect(self.inserir_cadastro)
        


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Classe_Inicio()
    window.show()
    sys.exit(app.exec())