# =================================================================
##
## File: exercise04.py
# Author(s): Esteban Padilla Cerdio - A01703068
# 			 Hilda Olivia Beltrán Acosta - A01251916
# Description: This file implements the PI approximation using the
# series proposed by Euler.
##				pi = sqrt ( 6 * sumatoria(i = 1-N) (1 / i^2) )
# The time this implementation takes will be used as
# the basis to calculate the improvement obtained with
# parallel technologies.
##
# Copyright (c) 2022 by Tecnologico de Monterrey.
# All Rights Reserved. May be reproduced for any non-commercial
# purpose.
##
# =================================================================

import utils
import time


SIZE = 1000000  # 1e6


# Place your code here

if __name__ == "__main__":

    print("Starting...")
    startTime = endTime = ms = 0
    for i in range(utils.N):
        startTime = time.time() * 1000

        result = 0

        # pi = sqrt(6 * sum(i=1-N)(1 / i ^ 2))
        for j in range(1, LIMIT+1):
            result += 1.0 / (j * j)

        result = (6 * result)**(1/2)

        endTime = time.time() * 1000

        ms = ms + (endTime - startTime)

    print("result = ", result)
    print("avg time = ", (ms / utils.N), " ms")
