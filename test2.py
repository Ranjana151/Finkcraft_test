#Implement a Python function that takes a list of integers and a target number as input, 
# and returns a tuple of two integers that add up to the target number
 
lt = list(input("Enter the integers seperated by space").split())
target_num = int(input())
lt = list(map(int,lt))

lt1 = []
for i in range(0,len(lt)):
	if lt[i-1] + lt[i] == target_num:
		lt1.append(lt[i-1])
		lt1.append(lt[i])
	else:
		continue
tupl_int = tuple(lt1)
print(tupl_int)
	
