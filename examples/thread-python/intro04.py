## =================================================================
##
## File: intro04.cpp
## Author: Pedro Perez
## Description: This file contains an example of processes in Python. 
##
## Copyright (c) 2022 by Tecnologico de Monterrey.
## All Rights Reserved. May be reproduced for any non-commercial
## purpose.
##
## =================================================================

import multiprocessing as mp
import threading as th

# CORES = mp.cpu_count() 
CORES = 4

def task(id, limit):
    for i in range(0, limit):
        print("Process id = ", id, " i = " , i)

if __name__ == "__main__":
	threads = list()
	for index in range(CORES):
		t = th.Thread(target=task, args=(index, ((index + 1) * 2), ))
		threads.append(t)
		t.start()

	for index, thread in enumerate(threads):
		print("Main    : before joining process ", index, ".")
		thread.join()
		print("Main    : process ", index, " done.")