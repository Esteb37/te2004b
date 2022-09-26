# =================================================================
##
# File: exercise03.py
# Author(s): Esteban Padilla Cerdio - A01703068
# 			 Hilda Olivia Beltrán Acosta - A01251916
# Description: This file contains the code that implements the
# enumeration sort algorithm. The time this implementation
# takes ill be used as the basis to calculate the
# improvement obtained with parallel technologies.
##
# Copyright (c) 2022 by Tecnologico de Monterrey.
# All Rights Reserved. May be reproduced for any non-commercial
# purpose.
##
# =================================================================

import utils
import time

SIZE = 100000  # 1e5

# Place your code here

if __name__ == "__main__":
    array = [0] * SIZE

    utils.randomArray(array)
    utils.displayArray("before", array)

    print("Starting...")
    startTime = endTime = ms = 0
    result = [0] * SIZE

    for i in range(utils.N):
        startTime = time.time() * 1000

        for j, item_j in enumerate(array):
            # Asume it is the biggest
            count = SIZE - 1

            # Subtract how many elements are bigger than it
            for k, item_k in enumerate(array):
                if item_j < item_k or (item_j == item_k and j < k):
                    count -= 1

                # Place it in the position according to the count
            result[count] = item_j

        endTime = time.time() * 1000

        ms = ms + (endTime - startTime)

        # Check that the array is sorted
    isSorted = True
    for i in range(SIZE-1):
        if result[i] > result[i + 1]:
            isSorted = False
            break
    if isSorted:
        print("Array is sorted")
    else:
        print("Array is not sorted")

    utils.displayArray("after", result)
    print("avg time = ", (ms / utils.N), " ms")
