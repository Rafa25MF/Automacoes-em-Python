import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title="Selecione uma Pasta Para Organizar")

lista_arquivos = os.listdir(caminho)

locais = {
    "Imagens": [".png", ".jpeg", ".gif"],
    "Planilhas": [".xlsx"],
    "Apresentações": [".pptx", ".webp"],
    "Texto": [".docx"],
    "PDFs": [".pdf"],
    "Vídeo": {".mp4"},
    "Música": {".mp3"},
    "Outros": {".exe", ".html", ".rtf", ".avif", ".zip",
               ".py", ".conf", ".ccd", ".bin", ".sub", ".cue", ".7z"}
}

for arquivo in lista_arquivos:
    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
    for pasta in locais:
        if extensao in locais[pasta]:
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.mkdir(f"{caminho}/{pasta}")
            os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")