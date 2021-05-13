from matplotlib import pyplot as plt
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
    
    '''
    Wyrysowanie wykresów do porównania dokładności algorytmu
    '''
    x = 0.5
    points = np.linspace(0,1,50)
    #arcus sinus
    arc_val = np.arcsin(points)
    #tablice wartości różnych precyzji
    wykr2 = []
    wykr3 = []
    wykr4 = []

    for i in points:
        
        val2 = rozwiniecie(i,3)
        wykr2.append(val2)
        val3 = rozwiniecie(i,6)
        wykr3.append(val3)
        val4 = rozwiniecie(i,10)
        wykr4.append(val4)
    
    plt.plot(points,arc_val)
    plt.plot(points,wykr2)
    plt.plot(points,wykr3)
    plt.plot(points,wykr4)
    plt.legend(('Arcsin', 'Rozwinięcie n=3', 'Rozwinięcie n=6', 'Rozwinięcie n=10'))
    plt.xlabel('x')
    plt.ylabel('arcsin(x)')
    plt.show()