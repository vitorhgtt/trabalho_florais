import tkinter as tk
from tkinter import messagebox, scrolledtext
from sistema_florais import SistemaEspecialistaFloraisCompleto  # Supondo que o seu código está nesse arquivo

class AppFlorais:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema Especialista em Florais de Bach")
        self.root.geometry("600x500")
        self.sistema = SistemaEspecialistaFloraisCompleto()

        self.criar_widgets()

    def criar_widgets(self):
        tk.Label(self.root, text="Descreva seus sintomas emocionais ou físicos:", font=("Helvetica", 12)).pack(pady=10)

        self.entrada = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=60, height=6)
        self.entrada.pack(padx=10, pady=10)

        tk.Button(self.root, text="Obter Recomendações", command=self.obter_recomendacoes, bg="green", fg="white").pack(pady=5)

        self.resultado = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=60, height=15, state='disabled')
        self.resultado.pack(padx=10, pady=10)

    def obter_recomendacoes(self):
        texto = self.entrada.get("1.0", tk.END).strip()
        if not texto:
            messagebox.showwarning("Aviso", "Por favor, digite seus sintomas.")
            return

        recomendacoes = self.sistema._obter_recomendacoes(texto)
        self.resultado.config(state='normal')
        self.resultado.delete("1.0", tk.END)

        if not recomendacoes:
            self.resultado.insert(tk.END, "Recomendação Geral: Rescue Remedy\nIndicação: Situações de crise e emergência emocional")
        else:
            self.resultado.insert(tk.END, "Top Recomendações:\n")
            for i, (floral_id, score) in enumerate(recomendacoes[:3], 1):
                floral = self.sistema.base_florais[floral_id]
                self.resultado.insert(tk.END, f"\n{i}. {floral['nome']} ({score:.1f} pts)\n")
                self.resultado.insert(tk.END, f"   Grupo: {floral['grupo']}\n")
                self.resultado.insert(tk.END, f"   Descrição: {floral['descricao']}\n")
                self.resultado.insert(tk.END, f"   Indicações: {', '.join(floral['indicacoes'])}\n")

        self.resultado.insert(tk.END, "\nDica: Florais podem ser combinados para tratamentos mais específicos.")
        self.resultado.config(state='disabled')


if __name__ == "__main__":
    root = tk.Tk()
    app = AppFlorais(root)
    root.mainloop()
