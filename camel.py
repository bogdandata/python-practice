def main():
    camel_word = input("CamelCase: ")
    for c in camel_word:
        if c.isupper():
            print("_" + c.lower(), end="")
        else:
            print(c, end="")

    print()

main()
