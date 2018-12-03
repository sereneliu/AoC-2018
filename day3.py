# --- Day 3: No Matter How You Slice It ---
# The Elves managed to locate the chimney-squeeze prototype fabric for Santa's suit (thanks to someone who helpfully wrote its box IDs on the wall of the warehouse in the middle of the night). Unfortunately, anomalies are still affecting them - nobody can even agree on how to cut the fabric.

# The whole piece of fabric they're working on is a very large square - at least 1000 inches on each side.

# Each Elf has made a claim about which area of fabric would be ideal for Santa's suit. All claims have an ID and consist of a single rectangle with edges parallel to the edges of the fabric. Each claim's rectangle is defined as follows:

# The number of inches between the left edge of the fabric and the left edge of the rectangle.
# The number of inches between the top edge of the fabric and the top edge of the rectangle.
# The width of the rectangle in inches.
# The height of the rectangle in inches.
# A claim like #123 @ 3,2: 5x4 means that claim ID 123 specifies a rectangle 3 inches from the left edge, 2 inches from the top edge, 5 inches wide, and 4 inches tall. Visually, it claims the square inches of fabric represented by # (and ignores the square inches of fabric represented by .) in the diagram below:

# ...........
# ...........
# ...#####...
# ...#####...
# ...#####...
# ...#####...
# ...........
# ...........
# ...........
# The problem is that many of the claims overlap, causing two or more claims to cover part of the same areas. For example, consider the following claims:

# #1 @ 1,3: 4x4
# #2 @ 3,1: 4x4
# #3 @ 5,5: 2x2
# Visually, these claim the following areas:

# ........
# ...2222.
# ...2222.
# .11XX22.
# .11XX22.
# .111133.
# .111133.
# ........
# The four square inches marked with X are claimed by both 1 and 2. (Claim 3, while adjacent to the others, does not overlap either of them.)

# If the Elves all proceed with their own plans, none of them will have enough fabric. How many square inches of fabric are within two or more claims?

puzzle_input = open('day3.txt', 'r')
puzzle_input = puzzle_input.read()
puzzle_input = puzzle_input.split('\n')

def create_fabric(inches):
    fabric = []
    for _ in range(inches):
        width = []
        for _ in range(inches):
            width.append('.')
        fabric.append(width)
    return fabric

fabric = create_fabric(1000)

def mark_claims(elf_plans):
    for plan in elf_plans:
        elf = plan[1:plan.index(' ')]
        from_left_edge = int(plan[plan.index('@') + 2:plan.index(',')])
        from_top_edge = int(plan[plan.index(',') + 1:plan.index(':')])
        width = int(plan[plan.index(':') + 2:plan.index('x')])
        height = int(plan[plan.index('x') + 1:])
        
        for i in range(height):
            for j in range(width):
                if fabric[from_top_edge + i][from_left_edge + j] == '.':
                    fabric[from_top_edge + i][from_left_edge + j] = elf
                else:
                    fabric[from_top_edge + i][from_left_edge + j] = 'x'
    
    mult_claims = 0
    for h in range(len(fabric)):
        for w in range(len(fabric)):
            if fabric[h][w] == 'x':
                mult_claims += 1
    return fabric, mult_claims

marked_fabric, mult_claims = mark_claims(puzzle_input)
print mult_claims # Your puzzle answer was 107663.

# --- Part Two ---
# Amidst the chaos, you notice that exactly one claim doesn't overlap by even a single square inch of fabric with any other claim. If you can somehow draw attention to it, maybe the Elves will be able to make Santa's suit after all!

# For example, in the claims above, only claim 3 is intact after all claims are made.

# What is the ID of the only claim that doesn't overlap?

def find_claim_with_no_overlap(fabric, elf_plans):
    for plan in elf_plans:
        no_overlap = True
        elf = plan[1:plan.index(' ')]
        from_left_edge = int(plan[plan.index('@') + 2:plan.index(',')])
        from_top_edge = int(plan[plan.index(',') + 1:plan.index(':')])
        width = int(plan[plan.index(':') + 2:plan.index('x')])
        height = int(plan[plan.index('x') + 1:])
        
        for i in range(height):
            for j in range(width):
                if fabric[from_top_edge + i][from_left_edge + j] == 'x':
                    no_overlap = False
                    break
            if no_overlap == False:
                break
        
        if no_overlap == True:
            return elf

print find_claim_with_no_overlap(marked_fabric, puzzle_input) # Your puzzle answer was 1166.
