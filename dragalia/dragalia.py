import requests
import json
from operator import itemgetter

with open('dragalia.csv', 'r') as f:
	header = f.readline().strip().split(',')
	data = []

	for line in f:
		current = line.strip().split(',')
		test = {}
		test[header[0]] = current[0]
		test[header[1]] = current[1]
		test[header[2]] = current[2]
		test[header[3]] = current[3]
		data.append(test)

# to test output
# print (json.dumps(data, sort_keys=True, indent=4, separators=(',', ':')) )

total_list = []
str_list = []
HP_list = []

for ele in data:
	total = int(ele['Max STR']) + int(ele['Max HP'])
	ele['Total'] = total

	total_list.append( (ele['Character'], ele['Total'], ele['Rarity']) )
	str_list.append( (ele['Character'], ele['Max STR'], ele['Rarity']) )
	HP_list.append( (ele['Character'], ele['Max HP'], ele['Rarity']) )


sorted_total_list = sorted(total_list, reverse=True, key=lambda tup: tup[1])
with open('total.txt', 'w') as f:
	f.write('Dragalia Lost Totals\n\n')
	for i in range(0,len(sorted_total_list)-1):
		f.write(sorted_total_list[i][0]+'('+sorted_total_list[i][2]+') : '+str(sorted_total_list[i][1])+'\n')

sorted_str_list = sorted(str_list, reverse=True, key=lambda tup: tup[1])
with open('Max_STR.txt', 'w') as f:
	f.write('Dragalia Lost Max STR\n\n')
	for i in range(0,len(sorted_str_list)-1):
		f.write(sorted_str_list[i][0]+'('+sorted_str_list[i][2]+') : '+str(sorted_str_list[i][1])+'\n')

sorted_HP_list = sorted(HP_list, reverse=True, key=lambda tup: tup[1])
with open('Max_HP.txt', 'w') as f:
	f.write('Dragalia Lost Max HP\n\n')
	for i in range(0,len(sorted_HP_list)-1):
		f.write(sorted_HP_list[i][0]+'('+sorted_HP_list[i][2]+') : '+str(sorted_HP_list[i][1])+'\n')



