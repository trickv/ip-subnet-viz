#!/usr/bin/env python

from util import *

from PIL import Image
from netaddr import IPNetwork

import hashlib
import sys

supernet = IPNetwork(sys.argv[1])
allocations = []
for allocation in sys.argv[2].split(','):
    allocations.append(IPNetwork(allocation))
output_file = sys.argv[3]

width = 256
height = supernet.size / width
image = Image.new("RGB", (width, height), "#eeeeee")

red = (255, 0, 0)
green = (0, 255, 0)

for allocation in allocations:
    for ip in allocation:
        digest = hashlib.md5(str(allocation)).hexdigest()
        color = (
            int(digest[0:2], 16),
            int(digest[2:4], 16),
            int(digest[4:6], 16))
        image.putpixel(ip_coordinates(supernet, ip, width), color)

image.save(output_file)
