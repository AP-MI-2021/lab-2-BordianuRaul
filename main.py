'''

Determina daca un numar este antipalindrom

'''

def is_antipalindrome(n):

    clona_n=n
    invers_n=0
    nr_cifre=0

    while clona_n:

        invers_n=invers_n*10+clona_n%10
        clona_n//=10
        nr_cifre+=1

    if nr_cifre % 2 == 1:
        ok=0
    else: ok=1

    while invers_n:
        if invers_n%10 == n%10:
            ok=ok+1
        if ok==2:
            return False
        invers_n//=10
        n//=10
    return True

def test_is_antipalindrome():

    assert is_antipalindrome(12345) == True
    assert is_antipalindrome(92349) == False
    assert is_antipalindrome(1542341) == False
    assert is_antipalindrome(1234) == True
    assert is_antipalindrome(53912) == True
    assert is_antipalindrome(129329) == False




'''

Transforma un numar din baza 10 in baza 2

'''

def get_base_2(n):

    baza_2 = []
    n=int(n)
    while n:
        baza_2.insert(0, n % 2)
        n//=2
    return baza_2

def test_get_base_2():

    assert get_base_2(12) == [1,1,0,0]
    assert get_base_2 (23) == [1,0,1,1,1]
    assert get_base_2(103) == [1, 1, 0, 0, 1, 1, 1]
    assert get_base_2(2021) == [1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1]
    assert get_base_2(2) == [1, 0]

"""
 Transforma un numa dat in baza 2 in baza 16
"""
def get_base_16_from_2(n):


    n=int(n)
    exponent=0
    base_10_n=0
    base_16_n=""
    while n:
        base_10_n += (n % 10 * 2**exponent)
        exponent += 1
        n //= 10


    while base_10_n:

        rest_base_10_n = base_10_n % 16
        if rest_base_10_n == 10:
            base_16_n ='A'+ base_16_n
        elif rest_base_10_n == 11:
            base_16_n ='B' + base_16_n
        elif rest_base_10_n ==12:
            base_16_n ='C' + base_16_n
        elif rest_base_10_n == 13:
            base_16_n ='D' + base_16_n
        elif rest_base_10_n ==14:
            base_16_n ='E' + base_16_n
        elif rest_base_10_n == 15:
            base_16_n ='F' + base_16_n
        else: base_16_n =str(rest_base_10_n) + base_16_n

        base_10_n //= 16

    return base_16_n



def test_get_base_16_from_2():

    assert get_base_16_from_2(10) == '2'
    assert get_base_16_from_2(1001) == '9'
    assert get_base_16_from_2(10011101) == '9D'
    assert get_base_16_from_2(11111) == '1F'
    assert get_base_16_from_2(10011) == '13'


def main():

    while True:
        print("1. Determina daca un numar este antipalndrom")
        print("2. Transforma un numar din baza 10 in baza 2")
        print("3. Transforma un numar din baza 2 in baza 16")
        print("x. Iesire din program")

        optiune=input("Alege optiune: ")

        if optiune == '1':
            numar=int(input("Introduce-ti numarul: "))
            print(is_antipalindrome(numar))

        elif optiune == '2':
            numar=input("Introduce-ti numarul: ")
            print(f"Numarul {numar} in baza 2 este {get_base_2(numar)}")

        elif optiune == '3':
            numar=input("Introduce-ti numarul in baza 2: ")
            print(get_base_16_from_2(numar))

        elif optiune == 'x':
            break

        else: print("Optiune invalida!")

test_is_antipalindrome()
test_get_base_2()
test_get_base_16_from_2()
main()