




with open('jobs.txt', 'r') as f:
	header = f.readline()

	jobs = []
	for line in f:
		job = line.strip().split(', ')
		jobs.append(job)

applied = 0
rejected = 0
response = 0
for job in jobs:
	if job[2] == 'Applied':
		applied += 1
	elif job[2] == 'Rejected':
		rejected += 1
	else:
		response += 1

print('Total:', len(jobs))
print('Applied:', applied)
print('Rejected:', rejected)
print('Response:', response)