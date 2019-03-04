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

with open('dates.txt', 'r') as myfile:
    dates=myfile.read().split(',')

def main():
	# lines = f.read().split("--")
	# count = 0;
	# dates = lines[1::2]

	# Regex to match all non letters or spaces
	alpha = re.compile(r"[^a-zA-Z\s]+")
	# Regex for a date, and two names
	one = r"^[1-9][0-9]?\/[0-9][0-9]?\/[18|19]"
	two = " - " + name1 + ": "
	three = " - " + name2 + ": "

	# Make exported text from whatsapp into a more parseable format
	with open("../Sensitive/ChatRaw.txt", "r") as f:
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

		if not set(dic.keys()) == set(dic2.keys()):
			print("NO")

					


main()
