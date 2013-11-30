#!/usr/bin/env python

from PIL import Image
from netaddr import IPNetwork

import sys

network = IPNetwork(sys.argv[1])
allocations = []
for allocation in sys.argv[2].split(','):
    allocations.append(IPNetwork(allocation))
output_file = sys.argv[3]

"""network = IPNetwork('192.168.0.0/16')
allocations = (
    IPNetwork('192.168.1.0/24'),
    IPNetwork('192.168.4.0/24'),
    IPNetwork('192.168.16.0/23'),
    IPNetwork('192.168.174.0/24'),
    IPNetwork('192.168.199.0/26'),
    IPNetwork('192.168.144.128/28'),
    )

network = IPNetwork('172.22.0.0/16') #  APAC Satellite offices allocation
allocations = (
    IPNetwork('172.22.0.0/20'), # KL
    IPNetwork('172.16.16.0/20'), # SG
    IPNetwork('172.16.32.0/20'), # BOM
    IPNetwork('172.16.48.0/20'), # SYD
    )
"""

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


#for i in range(100):
#    image.putpixel((i, i), red)



image.save(output_file)
