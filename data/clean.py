o = open('ideologies_trimmed.txt','w', encoding="utf8")
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