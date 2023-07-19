#!/bin/python3

import math
import os
import random
import re
import sys



n = int(input())
print ("Not Weird" if not n%2 and (n in range(2,6) or n>20) else "Weird")
