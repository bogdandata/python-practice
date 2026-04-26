def main():
    while True:
        try:
            fraction = input("Fraction: ")
            x, y = fraction.split("/")
            x = int(x)
            y = int(y)
            if y == 0:
                continue
            if x > y:
                continue

            break
        except (ValueError, ZeroDivisionError):
            pass
        except NameError:
            pass
    percentage = x / y * 100
    if percentage < 2:
        print("E")
    elif percentage > 99:
        print("F")
    else:
        print(f"{round(percentage)}%")

main()