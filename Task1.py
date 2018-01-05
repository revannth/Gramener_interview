#Task1.py

#Using python 2.7.14


#Case 1,with duplicate values and without using inbuilt set functions for optimal solution


list1 = list(raw_input())

list2 = list(raw_input())



def binsearch(key,lis_t):
	low = 0
	high = len(lis_t)
	
	while low <= high :

		mid = low + (high - low)/2

		
		if key > lis_t[mid]:
			low = mid + 1

		elif key < lis_t[mid]:
			high = mid - 1
		else :
			return True 

	return False

#To make sure duplicates are handled

if len(list2) >= len(list1):

	list2.sort()


	union =[]
	unique = []

	[ union.append(val) if binsearch(val,list2) else unique.append(val) for val in list1 ]

	#Common elements

	print union

	#Unique elements
	print unique

else :
	list1.sort()


	union =[]
	unique = []

	[ union.append(val) if binsearch(val,list1) else unique.append(val) for val in list2 ]

	for val in list2:
		if binsearch(val,list1):
			union.append(val)
		else :
			unique.append(val)

	#Common elements

	print union

	#Unique elements
	print unique



#Time complexity : O( len(list2)*log(list2) + len(list1)*log(list2) )
						#sorting                 #searching         






#Case 2, without duplicate values using inbuilt set functions for optimal solution




set1 = set(list1)

set2 = set(list2)

 #Common Elements

commonele = set1 & set2
#Time complexity : O( len(set1) * len(set2) )

print commonele 

#Elements in L1 and not in L2

print set1 - commonele
#Time complexity : O( len(set1) )












