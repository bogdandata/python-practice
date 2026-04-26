def main():
    d = {}
    while True:
        try:
            item = input()
        except EOFError:
            break
        item = item.lower()
        d[item] = d.get(item, 0) + 1

    for item in sorted(d):
        print(d[item], item.upper())

if __name__ == "__main__":
    main()
