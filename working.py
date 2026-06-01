import re
import sys


def main():
    print(convert(input("Hours: ")))




def convert(s):
    time_pattern = r"^([1-9]|1[0-2]):?([0-5][0-9])?\s*(AM|PM)\s*to\s*([1-9]|1[0-2]):?([0-5][0-9])?\s*(AM|PM)$"
    if match := re.search(time_pattern, s):
        hours = int(match.group(1))
        minutes = match.group(2) or "00"
        start_am_pm = match.group(3).upper()
        end_hours = int(match.group(4))
        end_minutes = match.group(5) or "00"
        end_am_pm =     match.group(6).upper()
        if start_am_pm == "PM" and hours != 12:
            hours += 12
        elif start_am_pm == "AM" and hours == 12:
            hours = 0

        if end_am_pm == "PM" and end_hours != 12:
            end_hours += 12
        elif end_am_pm == "AM" and end_hours == 12:
            end_hours = 0

        return f"{hours:02}:{minutes} to {end_hours:02}:{end_minutes}"
    else:
        raise ValueError("Invalid time format")

if __name__ == "__main__":
    main()