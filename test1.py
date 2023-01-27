#Write a Python program that finds the longest common substring between two strings.

a = "This is that beautiful"
b = "This is beautiful person"

a = a.split()
b= b.split()
lt = {}
for i in a:
	if i in b:
		lt[i] = len(i)
	else:
		continue
#print(lt)
longest_str = max(lt.values())
for i in lt :
	if lt[i] == longest_str:
		print(i)
		

