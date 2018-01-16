old = open('day','r')
new = open('new_day','w')
old_replace = input('please replace content:')
new_replace = input('please new replace content:')

for i in old:
	if old_replace in i:
		i = i.replace(old_replace,new_replace)
	new.write(i)

old.close()
new.close()