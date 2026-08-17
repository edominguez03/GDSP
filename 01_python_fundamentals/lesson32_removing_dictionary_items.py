computer = {'brand': 'apple',
            'processor': 'M4',
            'memory': 16,
            'year': 2026
            }


del computer['year']

del_mem = computer.pop('memory')
print(del_mem)

graph_card = computer.pop('graphics', "Not Specified")
print(graph_card)

print(computer)



