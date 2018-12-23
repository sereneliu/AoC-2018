# --- Day 23: Experimental Emergency Teleportation ---
# Using your torch to search the darkness of the rocky cavern, you finally locate the man's friend: a small reindeer.

# You're not sure how it got so far in this cave. It looks sick - too sick to walk - and too heavy for you to carry all the way back. Sleighs won't be invented for another 1500 years, of course.

# The only option is experimental emergency teleportation.

# You hit the "experimental emergency teleportation" button on the device and push I accept the risk on no fewer than 18 different warning messages. Immediately, the device deploys hundreds of tiny nanobots which fly around the cavern, apparently assembling themselves into a very specific formation. The device lists the X,Y,Z position (pos) for each nanobot as well as its signal radius (r) on its tiny screen (your puzzle input).

# Each nanobot can transmit signals to any integer coordinate which is a distance away from it less than or equal to its signal radius (as measured by Manhattan distance). Coordinates a distance away of less than or equal to a nanobot's signal radius are said to be in range of that nanobot.

# Before you start the teleportation process, you should determine which nanobot is the strongest (that is, which has the largest signal radius) and then, for that nanobot, the total number of nanobots that are in range of it, including itself.

# For example, given the following nanobots:

# pos=<0,0,0>, r=4
# pos=<1,0,0>, r=1
# pos=<4,0,0>, r=3
# pos=<0,2,0>, r=1
# pos=<0,5,0>, r=3
# pos=<0,0,3>, r=1
# pos=<1,1,1>, r=1
# pos=<1,1,2>, r=1
# pos=<1,3,1>, r=1
# The strongest nanobot is the first one (position 0,0,0) because its signal radius, 4 is the largest. Using that nanobot's location and signal radius, the following nanobots are in or out of range:

# The nanobot at 0,0,0 is distance 0 away, and so it is in range.
# The nanobot at 1,0,0 is distance 1 away, and so it is in range.
# The nanobot at 4,0,0 is distance 4 away, and so it is in range.
# The nanobot at 0,2,0 is distance 2 away, and so it is in range.
# The nanobot at 0,5,0 is distance 5 away, and so it is not in range.
# The nanobot at 0,0,3 is distance 3 away, and so it is in range.
# The nanobot at 1,1,1 is distance 3 away, and so it is in range.
# The nanobot at 1,1,2 is distance 4 away, and so it is in range.
# The nanobot at 1,3,1 is distance 5 away, and so it is not in range.
# In this example, in total, 7 nanobots are in range of the nanobot with the largest signal radius.

# Find the nanobot with the largest signal radius. How many nanobots are in range of its signals?

from operator import attrgetter

puzzle_input = open('day23.txt', 'r')
puzzle_input = puzzle_input.read()
puzzle_input = puzzle_input.split('\n')

class Nanobot:
    def __init__(self, location, radius):
        self.location = location
        self.radius = radius

def create_nanobots(xyzr):
    nanobots = []
    for nanobot in xyzr:
        pos = nanobot[nanobot.index('<') + 1:nanobot.index('>')]
        coordinates = [int(coordinate) for coordinate in pos.split(',')]
        radius = int(nanobot[nanobot.index('r') + 2:])
        nanobots.append(Nanobot(coordinates, radius))
    return nanobots

def find_largest_radius(list_of_nanobots):
    return max(list_of_nanobots, key=attrgetter('radius'))

nanobots = create_nanobots(puzzle_input)
nanobot_largest_r = find_largest_radius(nanobots)

def man_dist(bot1, bot2):
    (a, b, c) = bot1
    (d, e, f) = bot2
    return abs(a - d) + abs(b - e) + abs(c - f)

def find_nanobots_in_range(nanobot, nanobots):
    nanobots.remove(nanobot)
    nanobots_in_range = 0
    for nb in nanobots:
        nb_range = man_dist(nanobot.location, nb.location)
        if nb_range <= nanobot.radius:
            nanobots_in_range += 1
    return nanobots_in_range

print find_nanobots_in_range(nanobot_largest_r, nanobots)
