with open('Ссылки1.txt', 'r') as a:
    link_first = a.read().split("\n")

with open('Ссылки2.txt', 'r') as b:
    link_second = b.read().split("\n")

same_links = []
unsame_links = []
for link in link_first:
    if link in link_second and link not in same_links:
        same_links.append(link)
    else:
        unsame_links.append(link)

for link_ in link_second:
    link_ = link_.replace('!', '')
    if link_ not in same_links and link_ in link_first:
        same_links.append(link_)
    else:
        unsame_links.append(link_)

for link in unsame_links:
    if link in same_links:
        unsame_links.remove(link)

with open('Совпадающие ссылки.txt', 'w', encoding='utf-8') as sem_links:
    for g in same_links:
        sem_links.write(g + '\n')
with open('Несовпадающие ссылки.txt', 'w', encoding='utf-8') as not_links:
    for e in unsame_links:
        not_links.write(e + '\n')

print(link_first)
print(link_second)
print(same_links)