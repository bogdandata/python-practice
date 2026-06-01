import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: lines.py <file>")
        sys.exit(1)
    if not sys.argv[1].endswith(".py"):
        print("Invalid filename")
        sys.exit(1)

    try:
        with open(sys.argv[1], "r") as file:
            print(f"{sum(1 for line in file if line.strip() and not line.strip().startswith('#'))}")
    except FileNotFoundError:
        print("File not found")
        sys.exit(1)

if __name__ == "__main__":
    main()