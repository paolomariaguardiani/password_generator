from pathlib import Path

import generator
import set_time

generate_password = generator.Generator()

class WriteFile():
    def __init__(self):
        # self.data_odierna = st.data_odierna
        # self.data_per_titolo = st.data_per_titolo
        # self.st = set_time.SetTime()
        pass

    def write_one_password(self, nome_file):
        # devo mettere st qui per avere la data aggiornata al momento esatto in cui premo il pulsante
        st = set_time.SetTime() 
        path = Path(f"{st.data_per_titolo} - {nome_file}") # verrà salvato nella stessa directory del programma.exe
        content = f"Passwords generate in data: {st.data_odierna}\n\n"
        password = generate_password.generate_simple_password()
        content += f"Password semplice ..................... {password}\n\n"
        password = generate_password.shuffle_string(password)
        content += f"Password difficile .................... {password} "

        path.write_text(content)

    def write_simple_list(self, nome_file, lista):
        st = set_time.SetTime()
        path = Path(f"{st.data_per_titolo} - {nome_file}") # verrà salvato nella stessa directory del programma.exe
        content = ""
        content = f"Passwords generate in data: {st.data_odierna}\n\n"
        for element in lista:
            password = generate_password.generate_simple_password()
            numero_puntini = 35 - len(element)
            content += f"{element} {numero_puntini * '.'} {password}\n\n"

        path.write_text(content) # write the file and close it!!!


    def write_difficult_list(self, nome_file, lista):
        st = set_time.SetTime()
        path = Path(f"{st.data_per_titolo} - {nome_file}") # verrà salvato nella stessa directory del programma.exe
        
        content = ""
        content = f"Passwords generate in data: {st.data_odierna}\n\n"
        for element in lista:
            password = generate_password.generate_simple_password()
            password = generate_password.shuffle_string(password)
            numero_puntini = 35 - len(element)
            content += f"{element} {numero_puntini * '.'} {password}\n\n"

        path.write_text(content) # write the file and close it!!!