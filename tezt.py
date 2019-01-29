import re
import csv
import operator

open("errbody.csv", "w").close()
open("james.csv", "w").close()
open("jessika.csv", "w").close()
open("../Sensitive/new.txt", "w").close()
open("text.csv", "w").close()
file = open("../Sensitive/new.txt", "a")

name1 = "James"
name2 = "Jessika"

dates = ["8/27/18", "8/28/18", "8/29/18", "8/30/18", "8/31/18", "9/1/18", 
"9/2/18", "9/3/18", "9/4/18", "9/5/18", "9/6/18", "9/7/18", "9/8/18", "9/9/18", 
"9/10/18", "9/11/18", "9/12/18", "9/13/18", "9/14/18", "9/15/18", "9/16/18", 
"9/17/18", "9/18/18", "9/19/18", "9/20/18", "9/21/18", "9/22/18", "9/23/18", 
"9/24/18", "9/25/18", "9/26/18", "9/27/18", "9/28/18", "9/29/18", "9/30/18", 
"10/1/18", "10/2/18", "10/3/18", "10/4/18", "10/5/18", "10/6/18", "10/7/18", 
"10/8/18", "10/9/18", "10/10/18", "10/11/18", "10/12/18", "10/13/18", "10/14/18", 
"10/15/18", "10/16/18", "10/17/18", "10/18/18", "10/19/18", "10/20/18", "10/21/18", 
"10/22/18", "10/23/18", "10/24/18", "10/25/18", "10/26/18", "10/27/18", "10/28/18", 
"10/29/18", "10/30/18", "10/31/18", "11/1/18", "11/2/18", "11/3/18", "11/4/18", 
"11/5/18", "11/6/18", "11/7/18", "11/8/18", "11/9/18", "11/10/18", "11/11/18", 
"11/12/18", "11/13/18", "11/14/18", "11/15/18", "11/16/18", "11/17/18", "11/18/18", 
"11/19/18", "11/20/18", "11/21/18", "11/22/18", "11/23/18", "11/24/18", "11/25/18", 
"11/26/18", "11/27/18", "11/28/18", "11/29/18", "11/30/18", "12/1/18", "12/2/18", 
"12/3/18", "12/4/18", "12/5/18", "12/6/18", "12/7/18", "12/8/18", "12/9/18", 
"12/10/18", "12/11/18", "12/12/18", "12/13/18", "12/14/18", "12/15/18", "12/16/18", 
"12/17/18", "12/18/18", "12/19/18", "12/20/18", "12/21/18", "12/22/18"]

def main():
	# lines = f.read().split("--")
	# count = 0;
	# dates = lines[1::2]

	# Regex to match all non letters or spaces
	alpha = re.compile(r"[^a-zA-Z\s]+")
	# Regex for a date, and two names
	one = r"^[1-9][0-9]?\/[0-9][0-9]?\/18"
	two = " - " + name1 + ": "
	three = " - " + name2 + ": "

	# Make exported text from whatsapp into a more parseable format
	with open("../Sensitive/fresh.txt", "r") as f:
		for line in f:
			newLine = line

			# Add '--' as delimeter before the date
			if not re.search(one, line) is None:
				newLine = "--" + line
			# Add comma between time and name and add a delimiter after name for both names
			if not re.search(two, line) is None:
				newLine = newLine.replace(" - " + name1 + ": ", ", " + name1 + "--")
			if not re.search(three, line) is None:
				newLine = newLine.replace(" - " + name2 + ": ", ", " + name2 + "--")
			file.write(newLine)

	# Parse and split all newly written data from new.txt
	with open("../Sensitive/new.txt", "r") as s:
		i = 0
		cupl = []
		word = []
		# Dictonary for each occurance of each date per person
		dic = dict((el, 0) for el in dates)
		dic2 = dict((el, 0) for el in dates)
		textCounts = dict()

		# Split on '--'
		allLines = s.read().split("--")

		# Set lines equal to every other element to get the dates and names
		lines = allLines[1::2]
		# Set texts equal to all the text
		texts = allLines[0::2]

		wordz = ["hi", "hi", "HEllo", "Hello", "Hi hello", "hey", "Hey Hi HeLLo3.22", "hey"]

		for x in texts:
			x = x.replace("'", "")
			x = x.replace("\n", " ")
			x = alpha.sub(" ", x)
			x = x.lower()
			part = x.split(" ")
			word.append(part)

		for x in word:
			for y in x:
				if y == "m":
					print(x)
				textCounts[y] = textCounts.get(y, 0) + 1

		sortedCounts = sorted(textCounts.items(), key=operator.itemgetter(1))


		# Remove white space, split on commas, delete the 2nd element (time)
		for x in lines:
			x = x.replace(" ", "")
			part = x.split(",")
			part.pop(1)
			cupl.append(part)

		# For each date-name pair increment the dictionary value with the date
		# as the key for the corresponding persons dictionary
		for x in cupl:
			if x[1] == "James":
				dic[x[0]] = dic.get(x[0], 0) + 1
			else:
				dic2[x[0]] = dic2.get(x[0], 0) + 1

		# Write the computed values into csvs for each person and as a whole
		with open('text.csv', 'a') as f:
			for key, value in sortedCounts:
				f.write(key + "," + str(value) + "\n")

		with open('james.csv', 'a') as f:
			for key, value in dic.items():
				f.write(key + "," + str(value) + "\n")

		with open('jessika.csv', 'a') as f: 
			for key, value in dic2.items():
				f.write(key + "," + str(value) + "\n")
	
		with open('errbody.csv', 'a') as f: 
			for key, value in dic.items():
				f.write(key + "," + str(value) + "," + str(dic2.get(key)) + "\n")

		if not set(dick.keys()) == set(vag.keys()):
			print("NO")

					


main()
