import datetime
import time
halloween2016=datetime.datetime(2025,4,8,16,32,30)
while datetime.datetime.now() < halloween2016:
    time.sleep(1)

oct21st = datetime.datetime(2019, 10, 21, 16, 29, 0)    
print(oct21st.strftime('%Y/%m/%d %H:%M:%S'))
print(oct21st.strftime('%I:%M %p'))
print(oct21st.strftime("%B of '%y"))
print(datetime.datetime.strptime('October 21, 2019', '%B %d, %Y'))
print(datetime.datetime.strptime("October of '19", "%B of '%y"))
print(datetime.datetime.strptime("November of '63", "%B of '%y"))