from random import randint
from copy import deepcopy
import smtplib
from getpass import getpass


# participants' emails/name read in from csv
with open('santas.csv','r') as f:
	headers = f.readline().strip().split(',')

	people = []
	emails = []
	for line in f:
		line_data = line.strip().split(',')
		people.append(line_data[0])
		emails.append(line_data[1])

# connects email:person with a dictionary
data = {}
for i in range(len(people)):
	data[emails[i]] = people[i]

# assigns pairs (repeats if any gifter=giftee)
isSame = True
while isSame:
	isSame = False
	pairs = {}
	temp_people = deepcopy(people)

	# randomizes gifter/giftee
	for person in emails:
		idx = randint(0,len(temp_people)-1)
		pairs[person] = temp_people.pop(idx)

	# checks for giftee=gifter
	for person in emails:
		if data[person] == pairs[person]:
			isSame = True

# setting up smtp server
email = 'temp.kreshel@gmail.com'
password = getpass(prompt='Enter your password for temp.kreshel@gmail.com (hint: boo): ')
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(email,password)


# sends emails to givers of their givee
for key in emails:
	print('{}: {}\t{}: {}'.format(key,pairs[key],key,data[key])) #run to check the pairs
	recipient = key
	msg = pairs[key]
	#server.sendmail(email, recipient, msg)


server.quit()