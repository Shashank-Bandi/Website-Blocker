'''Python Script to block websites during the specified hours. By default the hours have been given as 9 to 6 but can be changed'''


import time
from datetime import datetime as dt



host_path = r"C:\Windows\System32\Drivers\etc\hosts"
direct_to="127.0.0.1"
list_website=['www.youtube.com','www.facebook.com','facebook.com','youtube.com',
              'www.pininterest.com','www.gmail.com','www.cricbuzz.com']

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,9)<dt.now()<dt(dt.now().year,dt.now().month,dt.now().day,18):
        with open(host_path,'r+') as file:
            content = file.read()
            if content not in list_website:
                for x in list_website:
                    file.write(direct_to+"\t"+x+'\n')
        print("Working hours.. Sorry:(")
    else:
        with open(host_path,'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in list_website):
                    file.write(line)
            file.truncate()
        
        print("Happy Browsing:) Logging time:",time.strftime("%H-%M-%S"))
    time.sleep(10)    
