o = open("a:\log")
#print (o.read())

import re
import csv
ip_dict = {}
invalid_arr = []

inv_f = open("./invalid_users.csv", 'w')
freq_f = open("./freq_writer.csv",'w')
invalid_writer = csv.writer(inv_f)
invalid_writer.writerow(["Date", "Time", "Username", "Ip Address"])
ip_freq_writer = csv.writer(freq_f)
ip_freq_writer.writerow(["Ip Address", "Frequency"])

for i in o.readlines():
    log_text = i.split(":")[len(i.split(":"))-1].lower()
    res =re.search(r'src=(\d+).(\d+).(\d+).(\d+)' , log_text)
    if(res != None):
        #print(log_text[res.span()[0]+4:res.span()[1]])
        if log_text[res.span()[0]+4:res.span()[1]] in ip_dict:
            ip_dict[log_text[res.span()[0]+4:res.span()[1]]] = ip_dict[log_text[res.span()[0]+4:res.span()[1]]] + 1
        else :
            ip_dict[log_text[res.span()[0]+4:res.span()[1]]] = 1
    invalid_res = re.search(r'invalid',log_text)
    if(invalid_res != None):
        csvline = ",".join([" ".join(i.split(" ")[0:2]) , i.split(" ")[2], log_text.split(" ")[3],
                            log_text.split(" ")[len(log_text.split(" "))-1]])
        inv_f.write(csvline)

for ip_data in ip_dict.items():
    ip_freq_writer.writerow(ip_data)

