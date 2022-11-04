# =================================================================
##
## File: exercise03.py
# Author(s):
# Description: This file contains the code that implements the
# enumeration sort algorithm using processes in Python.
##
# Copyright (c) 2022 by Tecnologico de Monterrey.
# All Rights Reserved. May be reproduced for any non-commercial
# purpose.
##
# =================================================================

import utils
import time
import multiprocessing as mp
import threading

SIZE = 1000  # 1e5


def partialSort(start, end, array, queue):

    for i in range(start, end):
        count = 0
        for j in range(0, SIZE):
            if array[j] < array[i]:
                count += 1
            elif array[j] == array[i] and j < i:
                count += 1
        queue.put((count, array[i]))

# Place your code here


if __name__ == "__main__":
    array = [0] * SIZE

    utils.randomArray(array)
    utils.displayArray("before", array)

    print("Starting...")
    startTime = endTime = ms = 0

    CORES = mp.cpu_count() // 2

    result = 0
    for i in range(utils.N):
        startTime = time.time() * 1000

        queue = mp.SimpleQueue()
        processes = list()

        blockSize = SIZE // CORES

        for i in range(CORES):
            start = i * blockSize
            if i != (CORES - 1):
                end = (i + 1) * blockSize
            else:
                end = SIZE
            process = mp.Process(target=partialSort,
                                 args=(start, end, array, queue,))
            processes.append(process)
            process.start()

        for process in processes:
            process.join()

        while not queue.empty():
            result = queue.get()
            array[result[0]] = result[1]

        endTime = time.time() * 1000

        ms = ms + (endTime - startTime)
        print("Execution time: %f ms" % (endTime - startTime))

    utils.displayArray("after", array)
    print("avg time = ", (ms / utils.N), " ms")
