# Trecia uzduotis
class third:  # Sukūriama klasė third
    def check_input(self):  # Sukuriama funkcija list_filtration, kuri skirta filtravimui
        try:
            x = input("Įveskite simbolius:")  # Paprašoma įvesti simbolių seką
            y = int(input("Įveskite skaičių:"))  # Paprašoma įvesti skaičių
            if (0 > y and len(x) % y != 0):  # Patikra ar yra įmanoma
                print("Jūsų duotas skaičius gali būti neteisingas arba neįmanoma padalinti!")
            else:
                x_list = list(x)  # Naujas listas su x reiksme
                temp_number = 0  # Laikinas skaičius
                temp_list = list()  # Laikinas listas
                temp = y  # Skirtas laikinam priskyrimui
                while (y <= len(x)):  # Pradedama while ciklas, kuris suskis tol kol bus y mažiau arba lygu x
                    for i in range(temp_number, y):  # Pradedamas for ciklas, kuris kiekvienam i range tarp temp number ir y atliks žemesnes kodo eiliutes
                        temp_list.append(x_list[i])  # Prie temp_list pridedamas x_list[i] elementas
                    temp_list = list(dict.fromkeys(temp_list))
                    result = ''.join(temp_list)  # Sujungiami listai
                    print(result)
                    temp_number += temp # temp_number yra padidinamas pridedant temp
                    y += temp  # y yra padidinamas pridedant temp
                    temp_list.clear()  # Išvalomas laikinas listas

        except:
            print("Bandykite iš naujo!")


t=third()  # Priskiriamas kintamasis klasei
t.check_input()