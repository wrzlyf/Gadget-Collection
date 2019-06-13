import requests
import time
import random


filename_original_no = 2539766052
url_prefix="https://img3.doubanio.com/view/photo/l/public/"

i=1
j=0
while i<=2000000000:
    filename_original_no = filename_original_no - 1
    filename_original="p"+ str(filename_original_no)+".jpg"
    url_photo= url_prefix + filename_original
    resp=requests.get(url_photo)    # 连接 photo的url
    
    if resp.status_code==200:
        with open(filename_original,"wb") as f:
            f.write(resp.content)
    else:
        pass

    #sleeptime = random.randint(1,5)     # 随机等待时间
    #time.sleep(sleeptime)
    resp.close
    status_connect = resp.status_code
    downloadtime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    print(str(filename_original) + " " + str(status_connect) + " " + str(downloadtime))
    i=i+1
    j=j+1
    
    #if j==50:
    #    j=0
    #    time.sleep(random.randint(11,20))   # 每50票 大休息 11~20s


print("done")

