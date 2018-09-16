
a = open('src.txt', 'r').read().splitlines()

o = open('dwnominate_112.csv', 'r', encoding='utf-8').read().splitlines()
d = open('dwnoms.txt', 'w', encoding='utf-8')
xcz=""
#print(a)
for x in a:
	for y in o:
		if x in y:
			#print(y)
			d.write(f"{y}\n")
#o.close()