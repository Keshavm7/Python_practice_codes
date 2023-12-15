# Program for Identifying entered day is Weekday/Working Day or Weekend or Holiday with Match Case Statment
wkd=input("Enter Weekday Name: ")
print("*"*50)
if(wkd.upper() in ["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY","MON","TUE","WED","THU","FRI","SAT","SUN"]):
   match(wkd.upper()[0:3]):
      case "MON"|"TUE"|"WED"|"THU"|"FRI":
         print("{} is Working day".format(wkd.capitalize()))
      case "SAT":
         print("{} is Weekend".format(wkd.capitalize()))
      case "SUN":
         print("{} is HOLIDAY".format(wkd.capitalize()))
else:
   print("The enterd day name is incorrect!!!! Try again")
print("*"*50)