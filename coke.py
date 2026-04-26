def main():
    amount_due = 50
    while True:
        coin = int(input("Insert coin: "))
        if coin in [25, 10, 5]:
            amount_due -= coin
            if amount_due > 0:
                print("due: ", amount_due)
            else:
                print("owed: ", -amount_due)
                break
        else:
            print("due: ", amount_due)

main()
        