import redis
import json

def tot_primes(n):
    """ Returns the total number of primes less than or equal to `n`."""
    primes = [2]
    if n < 2:
        return 0
    for i in range(2, n+1):
        for j in range(2, i):
            if (i % j == 0):
                break
            if j == i-1:
                primes.append(i)
    return len(primes)

def store_tot_primes_redis(max_num=100):
	for N in range(max_num):
		rd.set(N,tot_primes(N))

	return(rd)

def tot_primes_cache(n):
	if rd.get(n) is not None:
		return int(rd.get(n))
	else:
		rd.set(n,tot_primes(n))
		return int(rd.get(n))

def store_dictionary(uid, d):
	rd.set(uid,json.dumps(d))


rd = redis.StrictRedis(host='172.17.0.1', port=6379, db=0)