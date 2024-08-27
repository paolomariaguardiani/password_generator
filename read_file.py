from pathlib import Path


class ReadFile():
    def __init__(self):
        self.lista_dati = self.read_file_txt("dati/dati_importanti.txt")
        self.modello_password = self.lista_dati[0]
        
        self.lista_pc_classi = self.read_file_txt("dati/lista_pc_classi.txt")
        self.lista_maestri = self.read_file_txt("dati/lista_maestri.txt")


    def read_file_txt(self, percorso):
        path = Path(percorso)
        contents = path.read_text() # read the file and close it!
        lista = contents.splitlines()
        return lista