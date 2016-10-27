domainLists = ''
abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in abc:
	for j in abc:
		for k in abc:
			for l in abc:
				domain = i + j + k + l + '\n'
				domainLists += domain

with open('domainLists.txt', 'wb') as f:
	f.write(domainLists)
	f.close()