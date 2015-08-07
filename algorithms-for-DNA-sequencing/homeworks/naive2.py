def naive2(p, t):
	occurances = []
	for i in range(len(t) - len(p) + 1):
		match = True
		mismatches = 0
		for j in range(len(p)):
			if t[i+j] != p[j]:
				if mismatches > 2:
					match = False
					break
				else:
					mismatches += 1
		if match:
			occurances.append(i)
	return occurances

print naive2('ACTTTA', 'ACTTACTTGATAAAGT')