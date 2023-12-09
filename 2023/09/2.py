# https://adventofcode.com/2023/day/9
# inFile = './testInput.txt'
inFile = './input.txt'

seeds = [[int(x) for x in line.strip().split(' ')] for line in open(inFile, 'r').readlines()]
added=[]
for idx1, seed in enumerate(seeds):
    seed.reverse()
    newseed = []
    found = False
    while not found:
        newseed.append([see - seed[idx-1] for idx, see in enumerate(seed) if idx != 0 ])
        if all(s == 0 for s in newseed[-1]) :

            found = True
            newseed[-1].append(0)
            while len(newseed) > 1:
                newseed[-2].append(newseed[-2][-1]+newseed[-1][-1])
                newseed.pop(-1)
            added.append(seeds[idx1][-1] + newseed[-1][-1])
        seed=newseed[-1]
print(sum(added))


