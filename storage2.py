import colorama

products = [
    {
        "name": "Audi",
        "price": 50
    },
    {
        "name": "Audi fake",
        "price": 50
    },
    {
        "price": 30,
        "name": "BMW",
    },
    {
        "price": 30,
        "name": "BMW2",
    },
]


def print_products(specified_products=products,highlight_product=None):
    for product in specified_products:
        if product == highlight_product:
            print(f"{colorama.Back.LIGHTYELLOW_EX}{colorama.Fore.RED}ZMENENY PRODUKT{colorama.Fore.RESET} Název produktu: {colorama.Fore.RED}{product['name']}{colorama.Fore.RESET}, cena: {colorama.Fore.RED}{product['price']}${colorama.Style.RESET_ALL}")
        else:
            print(f"Název produktu: {colorama.Fore.YELLOW}{product['name']}{colorama.Fore.RESET}, cena: {colorama.Fore.YELLOW}{product['price']}${colorama.Fore.RESET}")


def add_product():
    products.append({
        'name': input("Název produktu:"),
        'price': int(input("Zadej cenu:"))
    })





def menu():
    print("Vítej ve skladu")
    print("###############\n")
    print("1. Výpis polože")
    print("2. Přidání položky")
    print("3. Vyhledani položek")
    print("4. Suma cen položek")
    print("5. Nejlevnejsi ceny položek")
    print("6. Nejdrazsi ceny položek")
    print("7. Prumer cen položek")
    print("8. Zmena položky\n")

    choice = int(input("Volba: "))

    if choice == 1:
        print("Položky na skladě jsou:")
        print_products()
        print("")
        menu()

    elif choice == 2:
        print("Přidání položky:")
        add_product()
        print("")
        menu()
    else:
        print("Zadal jsi špatně!\n")
        menu()


menu()
