# Program for identifying entered day is Weekday/Working Day or Weekend or Holiday with Match Case Statment
wkd=input("Enter any Weekday name: ")
print("*"*50)
match(wkd.upper()):
    case "MONDAY":
        print("{} is Working day".format(wkd.upper()))
    case "TUESDAY":
        print("{} is Working day".format(wkd.upper()))
    case "WEDNESDAY":
        print("{} is Working day".format(wkd.upper()))
    case "THURSDAY":
        print("{} is Working day".format(wkd.upper()))
    case "FRIDAY":
        print("{} is Working day".format(wkd.upper()))
    case "SATURDAY":
        print("{} is Weekend".format(wkd.upper()))
    case "SUNDAY":
        print("{} is Holiday".format(wkd.upper()))
print("*"*50)