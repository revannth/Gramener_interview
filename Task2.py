#Task2.py



#Case 1 : Assuming we are aware of the fact that the Gregorian Calendar starts with a Monday, that is 01/01/90 is a Monday


# Enter any two years you want to or just hit enter to get the answer for the number of thursdays between 1990 and 2000

begin_year =int(raw_input() or 1990)



end_year =int(raw_input() or 2000)
end_year-=1

def isleap(yea_r):
	if yea_r % 400==0 or (yea_r % 4==0 and yea_r % 100 != 0) :
		return True
	else :
		return False

def start_mon(begin_year):

	start_month=0

	if begin_year<1990 :

		count = 0

		while begin_year<=1990:
			if isleap(begin_year):
				count+=2
				
			else :
				count+=1

			begin_year+=1

		start_month = 7 - count%7

	elif begin_year>1990:

		count = 0

		temp = 1990

		while temp<=begin_year:
			if isleap(temp):
				count+=2
			else :
				count+=1

			temp+=1
		start_month = 7-count%7

	

	return start_month	

start_month = start_mon(begin_year)


no_thur= 52*(end_year-begin_year+1)

while begin_year<=end_year:

	if isleap(begin_year):
		start_month = (start_month + 2)%7
		if start_month == 4:
			no_thur+=1
	else:
		start_month = (start_month + 1)%7
		if start_month == 4:
			no_thur+=1

	begin_year+=1

print no_thur








