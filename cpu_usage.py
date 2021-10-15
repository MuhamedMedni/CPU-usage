#!/usr/bin/python3
import psutil, os ,sys

pstotal = 0.0
for proc in psutil.process_iter():
    ps_name = proc.name()
    ps_memory = proc.memory_info().rss
    #/ 2**20
    ps_pids = proc.pid

    pstotal += float(ps_memory)
print('Memory:', pstotal)

Input_memory = (sys.argv[1])
Input_minute = (sys.argv[2])

memory_number = Input_memory[:-1]
memory_unit = Input_memory[-1]

if memory_unit == 'M' or memory_unit == 'm':
    changed_memory_m = (float(pstotal) / 2**20)
    print(changed_memory_m)

if memory_unit == 'G' or memory_unit == 'g':
    changed_memory_g = (float(pstotal) / 2**30)
    print(changed_memory_g)
 
#=====================have to start from this part. 14/10 seongeun 

    if int(changed_memory_m) > int(memory_number):
        print("Stop")


#====================I think I can use it for .txt to show the list. so I just left it.

#def memory_usage(message: str = 'debug'):
#    p = psutil.Process()
#    rss = p.memory_info().rss / 2 ** 20 
#    print(f"[{message}] memory usage: {rss: 10.5f} MB")
#memory_usage('#1')
