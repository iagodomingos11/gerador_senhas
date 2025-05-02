import tkinter as tk
from gerador import gerar_senha  # Certifique-se de ter a função correta

# Cores do tema Matrix
COR_FUNDO = "#000000"         # Preto
COR_TEXTO = "#00FF00"         # Verde neon
COR_BOTAO = "#003300"         # Verde escuro
COR_BOTAO_TEXTO = "#00FF00"   # Verde neon
COR_ENTRADA = "#001a00"       # Verde quase preto
COR_ENTRADA_TEXTO = "#00FF00"

# Criação da janela principal
janela = tk.Tk()
janela.title("Gerador de Senhas do iago")
janela.geometry("400x300")
janela.configure(bg=COR_FUNDO)

# Título
titulo = tk.Label(janela, text="Gerador de Senhas do iago", bg=COR_FUNDO, fg=COR_TEXTO, font=("Courier", 16, "bold"))
titulo.pack(pady=10)

# Campo para inserir o tamanho da senha
entry_tamanho = tk.Entry(janela, bg=COR_ENTRADA, fg=COR_ENTRADA_TEXTO, insertbackground=COR_ENTRADA_TEXTO, font=("Courier", 12))
entry_tamanho.pack(pady=5)

# Campo para mostrar a senha gerada
entry_resultado = tk.Entry(janela, bg=COR_ENTRADA, fg=COR_ENTRADA_TEXTO, insertbackground=COR_ENTRADA_TEXTO, font=("Courier", 12), justify="center")
entry_resultado.pack(pady=10)

# Função do botão
def gerar_e_mostrar():
    try:
        tamanho = int(entry_tamanho.get())
        senha = gerar_senha(tamanho)
        entry_resultado.delete(0, tk.END)
        entry_resultado.insert(0, senha)
    except ValueError:
        entry_resultado.delete(0, tk.END)
        entry_resultado.insert(0, "Número inválido")

# Botão
botao_gerar = tk.Button(janela, text="Gerar Senha", command=gerar_e_mostrar,
                        bg=COR_BOTAO, fg=COR_BOTAO_TEXTO, font=("Courier", 12, "bold"), activebackground=COR_ENTRADA)
botao_gerar.pack(pady=10)

janela.mainloop()
