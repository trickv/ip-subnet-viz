#!/usr/bin/env python

from util import *

from PIL import Image
from netaddr import IPNetwork

import sys

supernet = IPNetwork(sys.argv[1])
allocations = []
for allocation in sys.argv[2].split(','):
    allocations.append(IPNetwork(allocation))
output_file = sys.argv[3]

width = 256
height = supernet.size / width
image = Image.new("RGB", (width, height), "#00ff00")

red = (255, 0, 0)
green = (0, 255, 0)

for allocation in allocations:
    for ip in allocation:
        image.putpixel(ip_coordinates(supernet, ip, width), red)

image.save(output_file)
