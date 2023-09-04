# Etapas: 1°: Fazer mudanças de diretórios pela biblioteca os
# 2°: Criar interface para a pessoa escolher em qual ela pretende executar o Script
# 3°: Funções para Organizar files por suas extensões e armazenar em pastas separadas

from Os import Os
from Tkinter import Interface

class Main():
   def __init__(self):
      self.os = Os()
      self.inter = Interface()

   def main(self):
      self.inter.interface()

if __name__ == '__main__':
   main = Main()
   main.main()




    