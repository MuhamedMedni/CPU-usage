#!/usr/bin/python3

import psutil, os, sys
import time, schedule

changed_memory_m = 0.0
changed_memory_g = 0.0

Input_memory = (sys.argv[1])
Input_minute = (sys.argv[2])

memory_number = Input_memory[:-1]
memory_unit = Input_memory[-1]


def job():
    f = open("/tmp/cpu_usage_rapport.txt", "a")
    for proc in psutil.process_iter():
        ps_name = proc.name()
        ps_memory = proc.memory_info().rss
        ps_pids = proc.pid

        if memory_unit == 'M' or memory_unit == 'm':
            changed_memory_m = (float(ps_memory) / 2**20)
            if float(changed_memory_m) > (float(memory_number)):
                 f = open("/tmp/cpu_usage_rapport.txt", "a")
                 f.write("WARNING : You're using CPU memory more than " + str(Input_memory) +" ")
                 f.write(str(ps_pids)+" ")
                 f.write(str(ps_name)+" ")
                 f.write(str(ps_memory/2**20))
                 f.write("\n")

        if memory_unit == 'G' or memory_unit == 'g':
            changed_memory_g = (float(ps_memory) / 2**30)
            if float(changed_memory_g) > (float(memory_number)):
                f = open("/tmp/cpu_usage_rapport.txt", "a")
                f.write("WARNING : You're using CPU memory more than " + str(Input_memory) +" ")
                f.write(str(ps_pids)+" ")
                f.write(str(ps_name)+" ")
                f.write(str(ps_memory/2**30))
                f.write("\n")
tt = 0
asd = True
starttime = time.time()
while asd:
    job()
    time.sleep(float(Input_minute) - ((time.time() - starttime) % float(Input_minute)))

    #Seongeun Park, Muhamed Medni 

