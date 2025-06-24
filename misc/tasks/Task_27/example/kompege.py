clustersA = [[],[]]

for s in open('27_A_17916.txt'):
    x, y = [float(c) for c in s.split()]
    if y > 8:
        clustersA[0].append([x,y])
    else:
        clustersA[1].append([x,y])

print([len(kl) for kl in clustersA])

clustersB = [[],[],[],[],[]]

for s in open('27_B_17916.txt'):
    x, y = [float(c) for c in s.split()]
    if y > 14:
        clustersB[0].append([x,y])
    if 10 < y < 14:
        clustersB[1].append([x,y])
    if 6 < y < 10:
        clustersB[2].append([x,y])
    if x < 8 and y < 4:
        clustersB[3].append([x,y])
    if x > 8 and y < 2:
        clustersB[4].append([x,y])

print([len(kl) for kl in clustersB])

def dist(p1, p2):
    x1,y1,x2,y2 = *p1, *p2
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

def center(kl):
    m = []
    for p in kl:
        sm = sum(dist(p,p1)for p1 in kl)
        m.append([sm, p])
    return min(m)[1]

centerA = [center(kl) for kl in clustersA]
centerB = [center(kl) for kl in clustersB]

# print(centerA)
# print(centerB)

pxA = sum(x for x,y in centerA)/2 * 10000
pyA = sum(y for x,y in centerA)/2 * 10000

print(int(pxA),int(pyA))

pxB = sum(x for x,y in centerB)/5 * 10000
pyB = sum(y for x,y in centerB)/5 * 10000

print(int(pxB),int(pyB))
