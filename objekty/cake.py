class Menu:
    def __init__(self, dni, smaki, nazwy) -> None:
        print(dni)
        print(smaki)
        print(nazwy)

dzien_powszedni = Menu(
    ["poniedziałek", "wtorek", "sroda"],
    ["truskawka", "malina", "porzeczka"],
    ["owocowka", "lesna", "polana"]
    )
weekend = Menu(
    ["piątek", "sobota", "nd"],
    ["beza", "tort1", "tort2"],
    ["bomba", "petarda", "OSOM"]
)


