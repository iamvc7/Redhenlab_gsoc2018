import json

with open('Cooking_Activity.txt','r') as f:
	lines = [line.rstrip('\n') for line in f]

new_dict = {}
for i in range(65):
	new_dict[i+1] = lines[i]

with open('labels_map.json', 'w', encoding='utf-8') as fp:
	json.dump(new_dict, fp)

