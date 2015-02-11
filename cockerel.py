import os.path
import random

if not os.path.isfile('./.cockerel'):
    with open('./.cockerel', 'w') as g:
        pass

with open('./.cockerel', 'r') as k:
    cache = [x.strip() for x in k.read().strip().split('\n')]


with open('./cockerel.txt', 'r') as f:
    l = f.read().strip().split('\n')[2:]
    l2 = [x[2:].strip() for x in l if x[2:].strip() not in cache]
    cockerel = random.choice(l2)

with open('./.cockerel', 'a') as c:
    c.write(cockerel + '\n')

if cockerel.endswith(')'):
    print(cockerel[:-4])
else:
    print(cockerel)
