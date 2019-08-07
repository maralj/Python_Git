import csv

### Reading the text file

myFile = '/Users/maraljamali/Desktop/red-headed-league.txt' 
with open(myFile, 'r') as rd:
	for items in rd.readlines():
		word = list(items.split(' '))
		char = list(items.strip())
	print(list(char))

### Removing punctuation 

def removePunctuation(char) :
	clean_str_list = []
	for item in char:
		if (item.isalpha()) or (item == ' '):
			clean_str_list.append(item)
		else:
			char.pop()
	return(clean_str_list)

char_list = removePunctuation(char)
clean_text = ''.join(char_list)

### Counting Word Frequency 

def findcount(clean_text):
	word_freq_dict = {}
	words = list(clean_text.split(' '))
	for word in words:
		if word not in word_freq_dict:
			word_freq_dict[word] = 1
		else:
			word_freq_dict[word] = word_freq_dict[word] + 1
	return(word_freq_dict)

word_freq = findcount(clean_text)
csv_file = '/Users/maraljamali/Desktop/word_freq.csv'

### Writing word count o a csv file

def writecountfile(csv_file,word_freq):
	dict_output = csv.writer(open(csv_file, 'w+'))
	for key, value in word_freq.items():
		c = (key, value)
		dict_output.writerow(c)

writecountfile(csv_file,word_freq)