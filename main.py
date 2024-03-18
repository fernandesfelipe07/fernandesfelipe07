import tkinter as tk
from tkinter import messagebox

class AcademiaApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Sistema de Academia")
        self.master.configure(bg="#f0f0f0")  # Cor de fundo da janela principal

        # Frames
        self.frame_adicionar = tk.Frame(self.master, bg="#f0f0f0")  # Cor de fundo do frame
        self.frame_adicionar.pack(pady=10)

        self.frame_lista = tk.Frame(self.master, bg="#f0f0f0")  # Cor de fundo do frame
        self.frame_lista.pack(padx=10, pady=5)

        # Labels e Entries para adicionar membros
        self.label_nome = tk.Label(self.frame_adicionar, text="Nome:", bg="#f0f0f0")  # Cor de fundo do label
        self.label_nome.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_nome = tk.Entry(self.frame_adicionar, width=30)
        self.entry_nome.grid(row=0, column=1, padx=5, pady=5)

        self.label_plano = tk.Label(self.frame_adicionar, text="Plano:", bg="#f0f0f0")  # Cor de fundo do label
        self.label_plano.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_plano = tk.Entry(self.frame_adicionar, width=30)
        self.entry_plano.grid(row=1, column=1, padx=5, pady=5)

        self.label_valor = tk.Label(self.frame_adicionar, text="Valor:", bg="#f0f0f0")  # Cor de fundo do label
        self.label_valor.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.entry_valor = tk.Entry(self.frame_adicionar, width=30)
        self.entry_valor.grid(row=2, column=1, padx=5, pady=5)

        # Botão para adicionar membro
        self.botao_adicionar = tk.Button(self.frame_adicionar, text="Adicionar Membro", command=self.adicionar_membro, cursor="hand2", bg="#008080", fg="white")  # Cor de fundo e texto do botão
        self.botao_adicionar.grid(row=3, columnspan=2, pady=10)

        # Lista de membros
        self.lista_membros = tk.Listbox(self.frame_lista, width=50)
        self.lista_membros.grid(row=0, column=0, rowspan=4)

        # Botões para editar, excluir e registrar pagamento
        self.botao_editar = tk.Button(self.frame_lista, text="Editar Membro", command=self.editar_membro, cursor="hand2", bg="#008080", fg="white")  # Cor de fundo e texto do botão
        self.botao_editar.grid(row=0, column=1, pady=5, padx=5, sticky='ew')

        self.botao_excluir = tk.Button(self.frame_lista, text="Excluir Membro", command=self.excluir_membro, cursor="hand2", bg="#008080", fg="white")  # Cor de fundo e texto do botão
        self.botao_excluir.grid(row=1, column=1, pady=5, padx=5, sticky='ew')

        self.botao_pagamento = tk.Button(self.frame_lista, text="Registrar Pagamento", command=self.registrar_pagamento, cursor="hand2", bg="#008080", fg="white")  # Cor de fundo e texto do botão
        self.botao_pagamento.grid(row=2, column=1, pady=5, padx=5, sticky='ew')

        # Botão para gerar relatório
        self.botao_relatorio = tk.Button(self.frame_lista, text="Gerar Relatório", command=self.gerar_relatorio, cursor="hand2", bg="#008080", fg="white")  # Cor de fundo e texto do botão
        self.botao_relatorio.grid(row=3, column=1, pady=5, padx=5, sticky='ew')

    def adicionar_membro(self):
        nome = self.entry_nome.get()
        plano = self.entry_plano.get()
        valor = self.entry_valor.get()

        if nome and plano and valor:
            self.lista_membros.insert(tk.END, f"{nome} - Plano: {plano} - Valor: R${valor}")
            self.entry_nome.delete(0, tk.END)
            self.entry_plano.delete(0, tk.END)
            self.entry_valor.delete(0, tk.END)
        else:
            messagebox.showwarning("Atenção", "Por favor, preencha todos os campos.")

    def registrar_pagamento(self):
        try:
            indice = self.lista_membros.curselection()[0]
            membro_selecionado = self.lista_membros.get(indice)
            self.lista_membros.delete(indice)
            messagebox.showinfo("Pagamento Registrado", f"Pagamento registrado para:\n{membro_selecionado}")
        except IndexError:
            messagebox.showwarning("Atenção", "Por favor, selecione um membro para registrar o pagamento.")

    def editar_membro(self):
        try:
            indice = self.lista_membros.curselection()[0]
            membro_selecionado = self.lista_membros.get(indice)
            nome, plano, valor = membro_selecionado.split(" - Plano: ")[0], membro_selecionado.split(" - Plano: ")[1].split(" - Valor: ")[0], membro_selecionado.split(" - Valor: ")[1]
            self.entry_nome.delete(0, tk.END)
            self.entry_plano.delete(0, tk.END)
            self.entry_valor.delete(0, tk.END)
            self.entry_nome.insert(0, nome)
            self.entry_plano.insert(0, plano)
            self.entry_valor.insert(0, valor)
            self.lista_membros.delete(indice)
        except IndexError:
            messagebox.showwarning("Atenção", "Por favor, selecione um membro para editar.")

    def excluir_membro(self):
        try:
            indice = self.lista_membros.curselection()[0]
            self.lista_membros.delete(indice)
        except IndexError:
            messagebox.showwarning("Atenção", "Por favor, selecione um membro para excluir.")

    def gerar_relatorio(self):
        membros = self.lista_membros.get(0, tk.END)
        messagebox.showinfo("Relatório de Membros", f"Total de membros: {len(membros)}\n\nLista de Membros:\n\n{chr(10).join(membros)}")

def main():
    root = tk.Tk()
    app = AcademiaApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()