def main():
    months = ["January",#list of months in order to find the index of the month
            "February", 
            "March", 
            "April",
            "May", 
            "June",
            "July",
            "August",
            "September", 
            "October",
            "November",
             "December"
]
    while True:
        try:
            s = input("Date: ")
            if "/" in s: 
                month, day, year = s.split("/") 
                month = int(month)
                day = int(day) 
                year = int(year)

                if month >= 1 and month <= 12 and day >= 1 and day <= 31: 
                    print(f"{year:04d}-{int(month):02d}-{day:02d}")  
                    break
            elif "," in s:
                s = s.replace(",", "")
                month_name, day, year = s.split() 
                if month_name in months:
                    month_number = months.index(month_name) + 1 
                    day = int(day) 
                    year = int(year)
                    if day >= 1 and day <= 31: 
                        print(f"{year:04d}-{month_number:02d}-{day:02d}")  
                        break
        except ValueError:
            pass


if __name__ == "__main__":
    main()