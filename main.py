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

def main():

    while True:
        print("1. Determina daca un numar este antipalndrom")
        print("2. Transforma un numar din baza 10 in baza 2")
        print("x. Iesire din program")

        optiune=input("Alege optiune: ")

        if optiune == '1':
            numar=int(input("Introduce-ti numarul: "))
            print(is_antipalindrome(numar))

        elif optiune == '2':
            numar=input("Introduce-ti numarul: ")
            print(f"Numarul {numar} in baza 2 este {get_base_2(numar)}")

        elif optiune == 'x':
            break

        else: print("Optiune invalida!")

test_is_antipalindrome()
test_get_base_2()
main()