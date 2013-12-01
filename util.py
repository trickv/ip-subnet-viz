# Each IP address in the supernet has a corresponding coordinate.
# Write a function to figure that out, and then this gets easier!
def ip_coordinates(supernet, ip, width):
    offset = int(ip) - int(supernet.network)
    row = int(offset / width)
    column = offset % width
    return (column, row)
