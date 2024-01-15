#Assignment 9.4
'''Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
 The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
 The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
 After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.'''
 
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

#creating a dictionary to store the values of interest
sender = {}
#picks lines beginning with 'From:', then strips the output. Formats the output and selects the email from the line. Then adds the emails and their count to the dictionary
for line in handle:
    if line.startswith('From: '):
        line = line.rstrip().split()
        word = line[1]
        sender[word] = sender.get(word, 0) + 1

#Creating the variables to hold the word with the largest count
bigword = None
bigcount = None

#assigns the sender.items to the items in the sender dictionary. If bigcount is None or less than the current iteration variable, the new word is stored and the count is updated in bigword and bigcount respectively. 
for word, count in sender.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count 
print(bigword, bigcount)