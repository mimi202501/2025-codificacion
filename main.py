if __name__ == "__main__":
    print(chr(98))
    print("=======")
    print(ord('c'))
    print("codigos ascii")
    for i in range(256):
        if 32 <= i <= 255:
            print(f"{i}: {chr(i)}")
        else:
            print(f"caracter no imprmible")
