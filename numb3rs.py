import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    if re.search(r"^\d+\.\d+\.\d+\.\d+$", ip):
       groups = re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip).groups()
       for group in groups:
            if int(group) < 0 or int(group) > 255:
                return False
       return True
    else:
        return False

 

if __name__ == "__main__":
    main()