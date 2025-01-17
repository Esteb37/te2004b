# =================================================================
##
## File: exercise02.py
# Author(s): Esteban Padilla Cerdio - A01703068
# 			 Hilda Olivia Beltrán Acosta - A01251916
# Description: This file contains the code that performs the sum of
# all prime numbers less than or equal to MAXIMUM. The
# time this implementation takes will be used as the
# basis to calculate the improvement obtained with
# parallel technologies.
##
# Copyright (c) 2022 by Tecnologico de Monterrey.
# All Rights Reserved. May be reproduced for any non-commercial
# purpose.
##
# =================================================================

import utils
import time

MAXIMUM = 1000000  # 1e6

# Place your code here

if __name__ == "__main__":
    print("Starting...")
    startTime = endTime = ms = 0

    for i in range(utils.N):

        result = 0

        startTime = time.time() * 1000

        # Sum of all prime numbers less than or equal to MAXIMUM
        for num in range(2, MAXIMUM+1):
            isPrime = True

            # Check all numbers from 2 to the square root of the current number
            for div in range(2, int(num**(1/2))+1):

                # If num is divisible by div, it is not prime
                if num % div == 0:
                    isPrime = False
                    break

            # If the number is prime, add it to the result
            if isPrime:
                result += num

        endTime = time.time() * 1000

        ms = ms + (endTime - startTime)

    print("sum = ", result)
    print("avg time = ", (ms / utils.N), " ms")
