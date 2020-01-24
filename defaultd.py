from collections import defaultdict
city_list = [('AP','Amaravati'), ('AP','Vizag'), ('KA','Bengalore'), ('KA', 'Mysore'), ('KA', 'Kolar'), ('MH', 'Mumbai'),
             ('AP', 'Tirupati'), ('MH','Pune'), ('WB', 'Kolkata'), ('TS', 'Hyderabad')]
cities_by_state = defaultdict(list)
for state, city in city_list:
    cities_by_state[state].append(city)

for state, cities in cities_by_state.items():
    print (state,':' ,', '.join(cities))



lst = [('Geeks', 1), ('For', 2), ('Geeks', 3)]
orDict = defaultdict(list)
# iterating over list of tuples
for key, val in lst:
    orDict[key].append(val)

print(orDict)