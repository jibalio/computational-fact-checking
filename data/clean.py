"""o = open('ideologies_trimmed.txt','w', encoding="utf8")
with open('ideologies', 'r', encoding="utf8") as f:
	for x in f.readlines():
		cnt = -1
		a = x.split("; ")
		for i in a:
			cnt+=1
			if cnt%2==0:
				o.write(i)
				o.write(";")
o.close()
"""

# TWO LINE SPLITTER
x = open ("t3_x_countries.txt","w")
y = open ("t3_y_capitals.txt", "w")
with open('unsep', 'r', encoding="utf-8") as f:
	cnt = -1
	for i in f:
		if not i.startswith("--"):
			cnt += 1
			if (cnt%2==0):
				x.write(i)
			else:
				y.write(i)
		else:
			x.write(i)
			y.write(i)
x.close()
y.close()


