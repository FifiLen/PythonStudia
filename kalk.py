def kalkulator():
    print("Prosty kalkulator w Pythonie")
    print("Wybierz operację:")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")

    while True:
        wybor = input("Wpisz numer operacji (1/2/3/4): ")

        if wybor in ('1', '2', '3', '4'):
            liczba1 = float(input("Wpisz pierwszą liczbę: "))
            liczba2 = float(input("Wpisz drugą liczbę: "))

            if wybor == '1':
                print(f"{liczba1} + {liczba2} = {liczba1 + liczba2}")

            elif wybor == '2':
                print(f"{liczba1} - {liczba2} = {liczba1 - liczba2}")

            elif wybor == '3':
                print(f"{liczba1} * {liczba2} = {liczba1 * liczba2}")

            elif wybor == '4':
                if liczba2 != 0:
                    print(f"{liczba1} / {liczba2} = {liczba1 / liczba2}")
                else:
                    print("Błąd! Dzielenie przez zero.")

            
            kolejna_operacja = input("Czy chcesz wykonać inną operację? (tak/nie): ")
            if kolejna_operacja.lower() != 'tak':
                break
        else:
            print("Niepoprawny wybór. Spróbuj ponownie.")

kalkulator()
