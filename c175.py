import  matplotlib.pyplot as plt
import psutil as p

list_app_name=[]
list_cpu_usage=[]
count=0
for process in p.process_iter():
    count=count+1
    if count<=6:
        name=process.name()
        cpu_usage=p.cpu_percent()
        print("name:",name,"cpu usage:",cpu_usage)
        list_app_name.append(name)
        list_cpu_usage.append(cpu_usage)
plt.figure(figsize=(15,7))
plt.xlabel("Applications")
plt.ylabel("CPU Usage")
plt.bar(list_app_name,list_cpu_usage,width=0.6,color=("red","orange","yellow","green","blue","purple"))
plt.show()