import sys
import inflect
from datetime import date


def main():
    dte = input("Date of Birth YYYY-MM-DD: ")

    try:
        mins = minutes(dte)
        p = inflect.engine()
        print(f"You have lived for {p.number_to_words(mins, andword='')} minutes.")
        
    except ValueError:
        sys.exit("Invalid date")



def minutes(birt_date):
    today = date.today()
    birth_date = date.fromisoformat(birt_date)
    delta = today - birth_date
    return delta.days * 24 * 60




if __name__ == "__main__":
    main()