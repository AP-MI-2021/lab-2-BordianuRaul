'''

Determina daca un numar este antipalindrom

'''

def is_antipalindrome(n):

    if n%2==1:
        ok=0
    else: ok=1

    clona_n=n
    invers_n=0

    while clona_n:
        invers_n=invers_n*10+clona_n%10
        clona_n//=10

    while invers_n:
        if invers_n%10 == n%10:
            ok=ok+1
        if ok==2:
            return False
        invers_n//=10
        n//=10
    return True

def main():

    while True:
        print("1. Determina daca un numar este antipalndrom")
        print("x. Iesire din program")

        optiune=input("Alege optiune: ")

        if optiune == '1':
            numar=int(input("Introduce-ti numarul: "))
            print(is_antipalindrome(numar))

        elif optiune == 'x':
            break

main()