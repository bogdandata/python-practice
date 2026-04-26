from pyfiglet import Figlet
import random
import sys

def main():
    f = Figlet() 
    if len(sys.argv) == 1:
        font = random.choice(f.getFonts())
    elif len(sys.argv) == 3 and sys.argv[1] in ("-f", "--font"):#check if the user 
                                                                #provided a font and if it's valid
        font = sys.argv[2]
        if font not in f.getFonts():
            print("Invalid font")
            sys.exit(1)
    else:
        print("Usage: figlet.py [-f font]")
        sys.exit(1)
    f.setFont(font=font)
    text = input("Input: ")
    print(f.renderText(text))


if __name__ == "__main__":
    main()
