# =================================================================
##
## File: exercise01.py
# Author(s): Esteban Padilla Cerdio - A01703068
# 			 Hilda Olivia Beltrán Acosta - A01251916
# Description: This file contains the code to count the number of
# even numbers within an array. The time this implementation
# takes will be used as the basis to calculate the
# improvement obtained with parallel technologies.
##
# Copyright (c) 2022 by Tecnologico de Monterrey.
# All Rights Reserved. May be reproduced for any non-commercial
# purpose.
##
# =================================================================

import utils
import time

SIZE = 100000000  # 1e8

# Place your code here

if __name__ == "__main__":
    array = [0] * SIZE

    utils.fillArray(array)
    utils.displayArray("array", array)

    print("Starting...")
    startTime = endTime = ms = 0
    result = 0
    for i in range(utils.N):
        startTime = time.time() * 1000

        for num in array:

            # The result of module is either 0 when even or 1 when odd, we can add 1 to the result when it's even and 0 when it's odd
            result += 1 - num % 2

        endTime = time.time() * 1000

        ms = ms + (endTime - startTime)

    print("sum = ", result)
    print("avg time = ", (ms / utils.N), " ms")
