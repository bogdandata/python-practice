def main():
    word = input("Input: ")
    print("Output: ", end="")
    for c in word:
        if c in "AEIOUaeiou":
            print( "", end="")
        else:
            print(c, end="")

    print()

main()