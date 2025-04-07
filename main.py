def linea(num: int, qty: int = 5):
    for i in range(qty):
        code = num + i
        print(f"{code}".rjust(3), end="")
        print(": ", end="")
        if code not in [9, 10, 13]:
            print(chr(code), end="")
        else:
            print("*", end="")
        print(" " * 3, end="")
    print()


def solucion_carlos(init: int = 32) -> None:
    qty = 9
    c = init
    while c <= 250:
        linea(c, qty)
        c += qty


def solucion_mariya():
    for i in range(256):
        if 32 <= i <= 255:
            print(f"{i}: {chr(i)}")
        else:
            print(f"caracter no imprmible")


if __name__ == "__main__":
    if True:
        solucion_mariya()
    else:
        solucion_carlos(32)
