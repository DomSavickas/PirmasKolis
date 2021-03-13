# Pirma užduotis
class first:  # Sukūriama klasė first
    def summing_function(self, n, a, b):  # Sukūriama funkcija summing_function, kuriai perduodami trys parametrai n, a, b
        try:
            given_text=list(n)  # given_text yra n kintamojo listas
            positive_symbols=list(a)  # positive_symbols yra a kintamojo listas
            negative_symbols=list(b)  # negative_symbols yra b kintamojo listas
            temp_negative=0  # Priskiriama 0 reikšmė kintamiesiems, kuriuos naudosiu cikle
            temp_positive=0
            try:
                for symbol in given_text:  # Pradedu for ciklą
                    for negative in negative_symbols:  # Pradedu antrą ciklą neigiamų simbolių radimui
                        if (symbol==negative):  # Jeigu yra rastas neigiamas simbolis, tai prie temp_negative yra pridedamas 1
                            temp_negative+=1
                    for positive in positive_symbols:  # Pradedu trečią ciklą teigiamų simbolių radimui
                        if (symbol==positive):  # Jeigu yra rastas teigiamas simbolis, tai prie temp_positive yra pridedamas 1
                            temp_positive+=1
            except:
                print("Problema su ciklu!")
            result=temp_positive-temp_negative  # Sukurtas result kintamasis, kuriame yra atimama negative suma iš positive
            print("Jūsų rezultatas: "+str(result))
        except:
            print("Bandykite iš naujo!")

fi=first()  # Priskiriamas kintamasis klasei
fi.summing_function("vienas du trys", "vn ", "ayds")  # Iškviečiama summing_function funkcija, kai programa yra paleidžiama
fi.summing_function("keturiolika", "ktur", "ila")
