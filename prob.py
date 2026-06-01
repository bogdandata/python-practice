import argparse

parser = argparse.ArgumentParser(description="yo, bruh")
parser.add_argument("-n", default=1, help="number of times to print", type=int)
args = parser.parse_args()  

for _ in range(int(args.n)):
    print("yo, bruh")