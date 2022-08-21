#2022-08-21
#1
def getPi(pat, pi):
	leng = 0
	i = 1
	while i < len(pat):
		if pat[i] == pat[leng]:	#when they match
			leng += 1
			pi[i] += leng
			i += 1
		else:	# when they don't match
			if leng != 0:	#when they matched earlier
				leng = pi[leng-1]
			else:	#when they didn't match earlier
				pi[i] = 0
				i += 1

def KMPSearch(pat, txt):
	m = len(pat)
	n = len(txt)
	pi = [0] * m
	getPi(pat, pi)
	i = 0	# txt index
	j = 0	# pat index
	while i < n:
		if txt[i] == pat[j]:	# if they match
			i += 1
			j += 1
		else:	# if they don't match
			if j != 0:	# if they matched earlier
				j = pi[j-1]
			else:	# if they don't match from the start
				i += 1
		if j == m:	# when the pattern is found
			print("Pattern found in index " + str(i - j))
			j = pi[j-1]
KMPSearch("ABXAB", "ABXABABXAB")