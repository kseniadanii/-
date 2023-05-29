from collections import OrderedDict
from functools import reduce

lines = []
with open('news.txt', 'r') as file:
    for line in file:
        pos, text = line.split(' ', maxsplit=1)
        pos = int(pos)
        text = text.strip()
        lines.append((pos, text))


def process(d, i):
    if len(d) == 0 or i[0] > list(d.keys())[-1]:
        d[i[0]] = i[1]
    return d


news = reduce(
    process,
    lines,
    OrderedDict()
)

print('\n'.join(news.values()))
