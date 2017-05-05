import sys

a = 0
b  = 0

clean = input()
viral = input()

shortest = min(len(clean),len(viral))

aDone = False
bDone = False
a = b = 0

while not (aDone and bDone):
    if a + b == shortest:
        break

    if clean[a] == viral[a]:
        a += 1
    else:
        aDone = True

    if a + b == shortest:
        break

    if clean[-1-b] == viral[-1-b]:
        b += 1
    else:
        bDone = True

# a    is index where it starts to change
# -1-b is where the end of virus difference is
# viral[a:-1-b] is the viral insertion
# to avoid indexing error make -1-b positive

b = len(viral) - b

print(len(viral[a:b]))



