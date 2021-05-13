import matplotlib
import numpy as np

def rozwiniecie(x, n):
    
    #Utworzenie potęg licznika
    potegi = np.linspace(1,2*n+1,num=n+1)
    #Obliczenia licznika
    licznik = np.ones((1))
    licz = np.linspace(1,2*n-1,num=n)
    licz = np.cumprod(licz)
    licznik = np.append(licznik, licz)

    #wyznaczenie mianownika
    mianownik = np.ones((1))
    mian1 = np.linspace(2,2*n,num=n)
    mian1 = np.cumprod(mian1)
    mianownik = np.append(mianownik,mian1)
    mianownik = mianownik * potegi

    #Podniesienie x do potegi
    x_power = np.power(x,potegi)
    #Policzenie finalnego licznika
    final_licznik = x_power * licznik
    #Podzielenie licznik przez mianownik
    final = final_licznik/mianownik
    
    return np.sum(final, axis = None)
    
    
if __name__ == "__main__":
    
    x = 0.5
    file = open("tabela.txt", 'w')
    val = np.arcsin(x)
    file.write(f'Wartość arcsin \t Funkcja rozwinięcie \t Błąd względny \t Błąd bezwzględny \n')
    print(f'Wartość arcsin \t Funkcja rozwinięcie \t Błąd względny \t Błąd bezwzględny \n')
    for i in range(10):
        sum = rozwiniecie(x,i)
        print(f'{val} \t {round(sum,6)} \t {round(val - sum, 6)} \t {100 * (val-sum)/val}% \n')
        file.write(f'{val} \t {round(sum,6)} \t {round(val - sum, 6)} \t {100 * (val-sum)/val}% \n')
    

