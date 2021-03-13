# Penkta užduotis
class fifth:  # Sukūriama klasė fifth
    def compress_text(self, text):  # Sukūriama funkcija compress_text, kuri skirta teksto suspaudimui
        try:
            temp_value = None  # Laikinas kintamasis
            i = 1  # Skaičius ciklui
            result = ""  # Rezultatui
            for value in text + "]":  # Ciklas skirtas raidžių skaičiavimui
                if temp_value == value:  # Tikrinama ar temp_value bus lygu value
                    i = i + 1  # Jei taip tai prie i pridedame i
                else:
                    if temp_value != None:  # Raidžių skaičiaus tikrinimas
                        if value != "]":  # Jeigu value bus nelygu ]
                            result += str(i)  # Prie rezultato pridėsime i ir value
                            result += value
                            i = 1  # i reikšmė 1
                            temp_value = value  # temp_value priskirsime value reikšmę
                        else:
                            result += str(i)  # Prie rezultato pridėsime i
                    else:
                        result += value # Prie rezultato pridėsime value
                        temp_value = value  # temp_value priskirsime value reikšmę
            return result

        except:
            print("Bandykite iš naujo!")

fif=fifth()  # Priskiriamas kintamasis klasei
print(fif.compress_text("aaavvvfdff")) # Paleidus programą bus iškviestos šios funkcijos
print(fif.compress_text("avtvvvff"))