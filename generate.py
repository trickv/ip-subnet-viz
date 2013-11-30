#!/usr/bin/env python

from PIL import Image
from netaddr import IPNetwork

import sys

network = IPNetwork(sys.argv[1])
allocations = []
for allocation in sys.argv[2].split(','):
    allocations.append(IPNetwork(allocation))
output_file = sys.argv[3]

width = 256
height = network.size / width
image = Image.new("RGB", (width, height), "white")

red = (255, 0, 0)
green = (0, 255, 0)

column = 0
row = 0
for ip in network:
    color = green
    for allocation in allocations:
        if ip >= allocation.network and ip <= allocation.broadcast:
            color = red
    image.putpixel((column, row), color)
    column += 1
    if column >= width:
        row += 1
        column = 0

image.save(output_file)
