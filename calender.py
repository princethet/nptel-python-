from datetime import datetime as dt 
dt.now()
#dt.day()
print(dt.now())

import calendar
# print(calender.weekday)

# import pytz  #need to install pytz 
# tz = pytz.timezone('Singapore')
# print(tz)

#PYTHON SUPPORTS AUTOMATIC GARBAGE COLLECTION

def check_valid_date(d,m,y,l):
    if l:
        if m==2:
            if d<30:
                return True
            else:
                return False
    
        else:
            if m<8:
                if m%2==1:
                    if d<32:
                        return True
                    else:
                        return False

                else:
                    if d<31:
                        return True
                    else:
                        return False 
            
            else:
                if m%2==0:
                    if d<32:
                        return True
                    else:
                        return False

                else:
                    if d<31:
                        return True
                    else:
                        return False 
    else:
        if m==2:
            if d<30:
                return True
            else:
                return False
    
        else:
            if m<8:
                if m%2==1:
                    if d<32:
                        return True
                    else:
                        return False

                else:
                    if d<31:
                        return True
                    else:
                        return False 
            
            else:
                if m%2==0:
                    if d<32:
                        return True
                    else:
                        return False

                else:
                    if d<31:
                        return True
                    else:
                        return False





def check_leap(y):
    if y%100==0:
        if y%4==0:
            return True
        else:
            return False 

    else:
        if y%4==0:
            return True
        else:
            return False


def get_day(day_index):
    list_of_days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    return list_of_days[day_index]

while(1):
    year = int(input("enter year(1970-20xx): "))
    if year<1970:
        print("enter a year in the range 1970 onwards ")
    else:
        break


while(1):
    month = int(input("enter month(1-12) "))
    if month<=12 and month>0:
        #print("enter a month in the range 1-12: ")
        break
    else:
        print("enter the valid month in the range(1-12)? ")

leap = check_leap(year)

while(1):
    date = int(input("enter date: "))
    if date>0 and check_valid_date(date,month,year,leap):
        break
    else:
        print("enter a valid date: ")

day_index = calendar.weekday(year,month,date)
day = get_day(day_index)

print(date,"/",month,"/",year,"falls on ",day)
        