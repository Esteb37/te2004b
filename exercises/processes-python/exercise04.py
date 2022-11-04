# =================================================================
##
# File: exercise04.py
# Author(s): Esteban Padilla Cerdio - A01703068
# 			 Hilda Olivia Beltrán Acosta - A01251916
# Description: This file implements the PI approximation using the
# series proposed by Euler.
# pi = sqrt ( 6 * sumatoria(i = 1-N) (1 / i^2) )
# using processes in Python.
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

SIZE = 1000000  # 1e6


def partialSum(start, end, queue):
    sum = 0
    for i in range(start, end):
        sum += 1 / (i ** 2)
    queue.put(sum)


if __name__ == "__main__":

    print("Starting...")

    CORES = 10

    startTime = endTime = ms = 0
    blockSize = SIZE // CORES

    for i in range(utils.N):
        startTime = time.time() * 1000

        queue = mp.SimpleQueue()

        processes = list()

        for i in range(CORES):
            start = i * blockSize + 1
            if i != (CORES - 1):
                end = (i + 1) * blockSize
            else:
                end = SIZE

            processes.append(mp.Process(
                target=partialSum, args=(start, end, queue)))
            processes[i].start()

        for i in range(CORES):
            processes[i].join()

        result = 0
        for i in range(CORES):
            result += queue.get()

        result = (6 * result) ** 0.5

        endTime = time.time() * 1000

        ms = ms + (endTime - startTime)

    print("result = ", result)
    print(CORES, "avg time = ", (ms / utils.N), " ms")
