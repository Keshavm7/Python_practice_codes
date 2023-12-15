# Program for Identifying entered day is Weekday/Working Day or Weekend or Holiday with Match Case Statment
wkd=input("Enter any Weekday name: ")
print("*"*50)
match(wkd.upper()):
    case "MONDAY"|"TUESDAY"|"WEDNESDAY"|"THURSDAY"|"FRIDAY":
        print("{} is Working Day".format(wkd.capitalize()))
    case "SATURDAY":
        print("{} is Weekend".format(wkd.capitalize()))
    case "SUNDAY":
        print("{} is Holiday".format(wkd.capitalize()))
print("*"*50)