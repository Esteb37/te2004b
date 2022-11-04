# =================================================================
##
# File: exercise03.py
# Author(s): Esteban Padilla Cerdio - A01703068
# 			 Hilda Olivia Beltrán Acosta - A01251916
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

SIZE = 100000  # 1e5


def enumSort(array, start, end, queue):

    positions = []
    for j in range(start, end):
        count = 0
        for i in range(0, SIZE):
            if (array[j] > array[i]):
                count += 1
        positions.append((count, array[j]))

    queue.put(positions)


if __name__ == "__main__":

    array = [0] * SIZE

    utils.randomArray(array)
    utils.displayArray("array", array)

    CORES = 10
    blockSize = SIZE // CORES

    print("Starting...")
    startTime = endTime = ms = 0

    for i in range(utils.N):

        utils.randomArray(array)

        startTime = time.time() * 1000

        processes = list()
        queue = mp.SimpleQueue()

        for i in range(CORES):
            start = i * blockSize
            if i != (CORES - 1):
                end = (i + 1) * blockSize
            else:
                end = SIZE

            process = mp.Process(target=enumSort,
                                 args=(array, start, end, queue))

            processes.append(process)
            process.start()

        for i in range(CORES):
            positions = queue.get()
            for pos in positions:
                array[pos[0]] = pos[1]

        endTime = time.time() * 1000
        ms += (endTime - startTime)

    utils.displayArray("array", array)
    print("avg time = ", (ms / utils.N), " ms")
