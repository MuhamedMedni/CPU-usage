#!/usr/bin/python3

import psutil, os, sys
#import time, schedule

changed_memory_m = 0.0
changed_memory_g = 0.0

Input_memory = (sys.argv[1])
Input_minute = (sys.argv[2])

memory_number = Input_memory[:-1]
memory_unit = Input_memory[-1]

for proc in psutil.process_iter():
    ps_name = proc.name()
    ps_memory = proc.memory_info().rss
    ps_pids = proc.pid

    if memory_unit == 'M' or memory_unit == 'm':
        changed_memory_m = (float(ps_memory) / 2**20)
        if float(changed_memory_m) > (float(memory_number)):
            print(ps_name, changed_memory_m)
            f = open("/tmp/cpu_usage_rapport.txt", "a")
#            f.write("WARNING : You're using CPU memory more than )
            f.write(str(ps_pids)+" ")
            f.write(str(ps_name)+" ")
            f.write(str(ps_memory))
            f.write("\n")

    if memory_unit == 'G' or memory_unit == 'g':
        changed_memory_g = (float(ps_memory) / 2**30)
        if float(changed_memory_g) > (float(memory_number)):
            print(ps_name, changed_memory_g)
    
#/tep/sayhello.txt
#schedule.every().minutes.do()
#=====================have to start from this part. 14/10 seongeun 

#    if int(changed_memory_m) > int(memory_number):
#        print("Stop")


#====================I think I can use it for .txt to show the list. so I just left it.

#def memory_usage(message: str = 'debug'):
#    p = psutil.Process()
#    rss = p.memory_info().rss / 2 ** 20 
#    print(f"[{message}] memory usage: {rss: 10.5f} MB")
#memory_usage('#1')
