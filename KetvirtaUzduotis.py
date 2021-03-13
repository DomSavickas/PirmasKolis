# ketvirta užduotis pridėjau naujų print eilučių, kad rezultatai būtų aiškesni
class fourth:  # Sukūriama klasė fourth

            def list_filtration(self, a):  # Sukūriama funkcija list_filtration, kuri skirta filtravimui
                print(a)
                print("Originalus listas")
                try:
                    empty_array = []  # Naujas masyvas
                    result = list(filter(lambda x: x >= 10 and x <= 100, a))  # List filtravimas
                    maximum = max(result)  # List max
                    minimum = min(result)  # List min
                    sum_of_all = sum(result)  # List suma
                    average = sum(result) / len(result)  # List vidurkis
                    empty_array.append(average)  # Atsakymai yra suvedami į masyvą
                    empty_array.append(minimum)
                    empty_array.append(maximum)
                    empty_array.append(sum_of_all)
                    print(empty_array)
                    print("Originalus skaičiavimo listas")
                    return empty_array
                except:
                    print("Bandykite iš naujo!")

            def call_list_filtration_on_new_list(self, b):
                try:
                    temp_list=list()
                    for x in b:  # Kiekvienam listui listų sąraše yra kviečiama pirma funkcija
                        temp_list.append(self.list_filtration(x))
                    return temp_list
                except:
                    print("Bandykite iš naujo!")

            def decorator_for_normal_list(self, func):  # Dekoratorius
                try:
                    def wrapped_func_one(x):  # Apsirašoma vidinė funkcija
                        t_list=list()  # Sūkuriamas listas reikšmėms
                        for number in func(one_dimensional_list):  # Pradedamas for ciklas pridedantis įrašus iš func į listą
                            t_list.append(number-x)
                        return t_list  # Grąžinamas listas
                    return wrapped_func_one  # Grąžinamas rezultatas
                except:
                    print("Bandykite iš naujo!")

            def decoratot_for_multiple_lists(self, func):  # Dekoratorius
                try:
                    def wrapped_func_two(x):  # Apsirašoma vidinė funkcija
                        t_list=list()  # Sūkuriamas listas reikšmėms
                        m_list=list()  # Sūkuriamas listas reikšmėms
                        for number in func(data_list1):  # Pradedamas for ciklas pridedantis įrašus iš func į listą
                            for i in number:  # Pradedamas for ciklas kiekvienam numeriui liste
                                t_list.append(i-x)  # Prie listo pridedame reikšmes su numeriais iš, kurių buvo atimta 10
                        m_list.append(t_list)  # Prie rezultatų listo pridedame t_list reikšmes
                        return m_list  # Grąžinamas listas
                    return wrapped_func_two  # Grąžinamas rezultatas
                except:
                    print("Bandykite iš naujo!")

            def results(self):
                try:
                    x = 10
                    result = self.decorator_for_normal_list(self.list_filtration)  # Ši eilutė ir žemiau pateiktos panaudoja dekoratorius pirmai ir antrai funkcijoms
                    print(result(x))
                    print("Listas po dekoratoriaus")
                    multilines = self.decoratot_for_multiple_lists(self.call_list_filtration_on_new_list)
                    print(multilines(x))
                    print("Listai po dekoratoriaus")
                except:
                    print("Bandykite iš naujo!")

fo=fourth()  # Priskiriamas kintamasis klasei
one_dimensional_list=[0,10,25,32,19,100,101]
data_list1=[
    [1, 10, 34, 110, 400, 30, 20],
    [-5, -10, 55, 120, 30],
    [2, 67, 23, 78, 200],
]
data_list2= [
    [-1, 45, 23, 32, 999],
    [67, 99, 23],
    [23],
]
fo.results()