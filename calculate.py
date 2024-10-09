import tkinter as tk
from tkinter import messagebox
import math

class CalculadoraGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")

        # Entrada para os números
        self.entry = tk.Entry(root, width=30, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=4)

        # Botões da calculadora
        buttons = [
            '7', '8', '9', '/', 
            '4', '5', '6', '*', 
            '1', '2', '3', '-', 
            '0', 'C', '=', '+', 
            '√', 'x^y'
        ]

        row = 1
        col = 0
        for button in buttons:
            tk.Button(root, text=button, padx=20, pady=20, command=lambda b=button: self.button_click(b)).grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1

        # Armazena os operandos e o operador
        self.first_number = None
        self.operation = None

    def button_click(self, button):
        if button in '0123456789':
            current = self.entry.get()
            self.entry.delete(0, tk.END)
            self.entry.insert(0, current + button)
        elif button == 'C':
            self.entry.delete(0, tk.END)
        elif button == '=':
            second_number = self.entry.get()
            self.entry.delete(0, tk.END)
            if self.operation == '+':
                self.entry.insert(0, self.first_number + float(second_number))
            elif self.operation == '-':
                self.entry.insert(0, self.first_number - float(second_number))
            elif self.operation == '*':
                self.entry.insert(0, self.first_number * float(second_number))
            elif self.operation == '/':
                if float(second_number) == 0:
                    messagebox.showerror("Erro", "Divisão por zero!")
                else:
                    self.entry.insert(0, self.first_number / float(second_number))
            elif self.operation == 'x^y':
                self.entry.insert(0, self.first_number ** float(second_number))
        elif button == '√':
            number = self.entry.get()
            self.entry.delete(0, tk.END)
            if float(number) < 0:
                messagebox.showerror("Erro", "Não é possível calcular a raiz quadrada de número negativo!")
            else:
                self.entry.insert(0, math.sqrt(float(number)))
        else:
            self.first_number = float(self.entry.get())
            self.operation = button
            self.entry.delete(0, tk.END)

# Testes automatizados
def teste_calculadora():
    calc = CalculadoraGUI(None)

    # Teste de soma
    assert calc.somar(5, 5) == 10, "Erro no teste de soma!"
    
    # Teste de subtração
    assert calc.subtrair(10, 5) == 5, "Erro no teste de subtração!"
    
    # Teste de multiplicação
    assert calc.multiplicar(4, 2) == 8, "Erro no teste de multiplicação!"
    
    # Teste de divisão
    assert calc.dividir(10, 2) == 5, "Erro no teste de divisão!"
    assert calc.dividir(10, 0) == "Erro: Divisão por zero!", "Erro no teste de divisão por zero!"
    
    # Teste de potência
    assert calc.potencia(2, 3) == 8, "Erro no teste de potência!"
    
    # Teste de raiz quadrada
    assert calc.raiz_quadrada(9) == 3, "Erro no teste de raiz quadrada!"
    assert calc.raiz_quadrada(-4) == "Erro: Não existe raiz quadrada de número negativo!", "Erro no teste de raiz quadrada com número negativo!"

    print("Todos os testes passaram com sucesso!")

# Função principal para iniciar a calculadora
if __name__ == "__main__":
    root = tk.Tk()
    calc_gui = CalculadoraGUI(root)
    root.mainloop()
    
    # Após fechar a calculadora, executar os testes
    teste_calculadora()
