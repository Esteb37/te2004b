# =================================================================
##
## File: exercise01.py
# Author(s): Esteban Padilla Cerdio - A01703068
# 			 Hilda Olivia Beltrán Acosta - A01251916
# Description: This file contains the code to count the number of
# even numbers within an array using processes in
# Python.
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

SIZE = 100000000  # 1e8

# Place your code here


def partialCountEven(start, end, array, queue):

    count = 0
    for i in range(start, end):
        if array[i] % 2 == 0:
            count += 1

    queue.put(count)


if __name__ == "__main__":
    array = [0] * SIZE

    utils.fillArray(array)
    utils.displayArray("array", array)

    CORES = 10

    blockSize = SIZE // CORES

    print("Starting...")
    startTime = endTime = ms = 0

    for i in range(utils.N):
        startTime = time.time() * 1000

        queue = mp.SimpleQueue()
        processes = list()

        for i in range(CORES):
            start = i * blockSize
            if i != (CORES - 1):
                end = (i + 1) * blockSize
            else:
                end = SIZE
            process = mp.Process(target=partialCountEven,
                                 args=(start, end, array, queue,))
            processes.append(process)
            process.start()

        result = 0

        for i in range(CORES):
            result += queue.get()

        endTime = time.time() * 1000

        ms = ms + (endTime - startTime)

    print("sum = ", result)
    print("avg time = ", (ms / utils.N), " ms")
