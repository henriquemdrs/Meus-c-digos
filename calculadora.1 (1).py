import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora.1")
        self.root.geometry("300x200")
        
        self.entry1_value = tk.StringVar()
        self.entry2_value = tk.StringVar()
        
        self.create_widgets()
    
    def create_widgets(self):
        self.create_input("a:", self.entry1_value)
        self.create_input("b:", self.entry2_value)
        
        operations = [("+", self.add), ("-", self.subtract), ("*", self.multiply), ("/", self.divide)]
        for operation, function in operations:
            tk.Button(self.root, text=operation, command=function).pack(side=tk.LEFT, padx=5)
        
        self.result_label = tk.Label(self.root, text="Resultado:")
        self.result_label.pack(anchor=tk.W, pady=(10,0))
        
        self.result = tk.Label(self.root, text="", anchor=tk.W)
        self.result.pack(anchor=tk.W, pady=(0,10))
        
        tk.Button(self.root, text="Limpar", command=self.clear).pack(side=tk.LEFT, padx=5)
        tk.Button(self.root, text="Sair", command=self.root.quit).pack(side=tk.LEFT, padx=5)
        
    def create_input(self, label_text, text_variable):
        tk.Label(self.root, text=f"Valor de {label_text}").pack(anchor=tk.W, pady=(5,0))
        entry = tk.Entry(self.root, textvariable=text_variable)
        entry.pack(anchor=tk.W, pady=(0,5))
        return entry
    
    def get_values(self):
        try:
            value1 = float(self.entry1_value.get())
            value2 = float(self.entry2_value.get())
            return value1, value2
        except ValueError:
            return None
    
    def update_result(self, result):
        self.result.config(text=f"Resultado: {result}")
    
    def add(self):
        values = self.get_values()
        if values is not None:
            result = sum(values)
            self.update_result(result)
        else:
            self.update_result("Valor inválido")
    
    def subtract(self):
        values = self.get_values()
        if values is not None:
            result = values[0] - values[1]
            self.update_result(result)
        else:
            self.update_result("Valor inválido")
    
    def multiply(self):
        values = self.get_values()
        if values is not None:
            result = values[0] * values[1]
            self.update_result(result)
        else:
            self.update_result("Valor inválido")
    
    def divide(self):
        values = self.get_values()
        if values is not None:
            if values[1] != 0:
                result = values[0] / values[1]
                self.update_result(result)
            else:
                self.update_result("Divisão por zero")
        else:
            self.update_result("Valor inválido")
    
    def clear(self):
        self.entry1_value.set("")
        self.entry2_value.set("")
        self.update_result("")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
