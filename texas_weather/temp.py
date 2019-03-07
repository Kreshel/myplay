from operator import itemgetter
import matplotlib.pyplot as plt

def std_dev_fail():
	with open('data.csv','r') as f:
		headers = f.readline()
		data =[]

		for line in f:
			line = line.strip().split(',')
			data.append(line)


	intvl = len(data)/6
	print(intvl)
	sorted_data = sorted(data, key = itemgetter(3))
	print(sorted_data[0:3])

def avg_temp_fail():
	with open('avgtemp.csv','r') as f:
		headers = f.readline().strip().split(',')
		data = []

		for line in f:
			line = line.strip().split(',')
			data.append(line)

	loc = set()
	date = set()
	for item in data:
		loc.add(item[0])
		date.add(item[1])

	print(len(loc))
	print(len(date))

def plot_avg_temps():
	plt.plot(san_diego)
	plt.plot(austin)
	plt.plot(miami)
	plt.plot(lincoln)
	plt.plot(new_york)
	plt.title('Average Temperature of Airports')
	plt.xlabel('Day of Year')
	plt.ylabel('Temperature (F)')
	plt.legend(['San Diego', 'Austin', 'Miami', 'Lincoln', 'New York'])
	plt.show()

def plot_clunky_errors():
	plt.errorbar(x=dates,y=austin,yerr=austin_std)
	plt.errorbar(x=dates,y=new_york,yerr=new_york_std)
	plt.show()







with open('useful.csv','r') as f:
	headers = f.readline().strip().split(',')
	# cleans up unnecessary headers
	for idx in [4,3,2,0]:
		del headers[idx]
	data = []

	for line in f:
		line = line.strip().split(',')
		for idx in [4,3,2,0]:
			del line[idx]
		data.append(line)

san_diego = []
austin = []
austin_std = []
miami = []
lincoln = []
new_york = []
new_york_std = []
for ele in data:
	if 'SAN DIEGO INTERNATIONAL AIRPORT CA US' in ele:
		san_diego.append(float(ele[2]))
	elif 'AUSTIN BERGSTROM INTERNATIONAL AIRPORT TX US' in ele:
		austin.append(float(ele[2]))
		austin_std.append(float(ele[3]))
	elif 'MIAMI KENDALL TAMIAMI EXEC AIRPORT FL US' in ele:
		miami.append(float(ele[2]))
	elif 'LINCOLN AIRPORT NE US' in ele:
		lincoln.append(float(ele[2]))
	elif 'JFK INTERNATIONAL AIRPORT NY US' in ele:
		new_york.append(float(ele[2]))
		new_york_std.append(float(ele[3]))

dates = list(range(1,366))

#plot_avg_temps()
#plot_clunky_errors()
plt.plot(austin_std)
plt.plot(new_york_std)
plt.show()



