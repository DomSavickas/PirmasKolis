# Antra užduotis
class second:  # Sukūriama klasė second
    def list_filtration(self, a):  # Sukūriama funkcija list_filtration, kuri skirta filtravimui
        print(a)
        print("Originalus listas")
        try:
            empty_array=[] # Naujas masyvas
            result = list(filter(lambda x: x>=10 and x<=100, a))  # List filtravimas
            print(result)
            print("Išfiltruotas listas")
            maximum=max(result)  # List max
            minimum=min(result)  # List min
            sum_of_all=sum(result)  # List suma
            average =sum(result)/len(result)  # List vidurkis
            empty_array.append(average)  # Atsakymai yra suvedami į masyvą
            empty_array.append(minimum)
            empty_array.append(maximum)
            empty_array.append(sum_of_all)
            return empty_array
        except:
            print("Bandykite iš naujo!")

    def call_list_filtration_on_new_list (self, b):
        for x in b:  # Kiekvienam listui listų sąraše yra kviečiama pirma funkcija
            print("="*30)
            print(self.list_filtration(x))
            print("Listo skaičiavimai")


s=second()  # Priskiriamas kintamasis klasei
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
s.list_filtration(one_dimensional_list)
s.call_list_filtration_on_new_list(data_list1)
s.call_list_filtration_on_new_list(data_list2)