import os
import csv

#Path of election_data.csv file
election_data=r"C:\Users\nguye\Desktop\Homework\Python\python-challenge\PyPoll\Resources\election_data.csv"

#Creating lists
votecount=[]
candidates=[]


with open(election_data, 'r') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    header=next(csvreader)

#Defining list
    for row in csvreader:
        votecount.append(row[0])
        candidates.append(row[2])

#Printing headers
print("Election Results")
print("---------------------------")

#Calculate the total number of votes cast
totalvote=len(votecount)
print(f"Total Votes: {totalvote} ")

print("---------------------------")

#A complete list of candidates who received votes
uniquecandidate=[]
for unique in candidates:
    if unique not in uniquecandidate:
        uniquecandidate.append(unique)

#The percentage of votes each candidates won and the total number of votes each candidate won

    #Count of each candidate
candidate1=candidates.count(uniquecandidate[0])
candidate2=candidates.count(uniquecandidate[1])
candidate3=candidates.count(uniquecandidate[2])
candidate4=candidates.count(uniquecandidate[3])

    #Percentage of each candidate
perc_candidate1=round(((candidate1/len(candidates))*100),3)
perc_candidate2=round(((candidate2/len(candidates))*100),3)
perc_candidate3=round(((candidate3/len(candidates))*100),3)
perc_candidate4=round(((candidate4/len(candidates))*100),3)

print(f"{uniquecandidate[0]}: {perc_candidate1}% ({candidate1})")
print(f"{uniquecandidate[1]}: {perc_candidate2}% ({candidate2})")
print(f"{uniquecandidate[2]}: {perc_candidate3}% ({candidate3})")
print(f"{uniquecandidate[3]}: {perc_candidate4}% ({candidate4})")

print("--------------------------")

#The winner of the election based on popular vote
    #Candidate dictionary with vote
candidatedict={uniquecandidate[0]:candidate1, uniquecandidate[1]:candidate2, uniquecandidate[2]:candidate3, uniquecandidate[3]:candidate4}
    #Max in dictionary credit: https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
winner=max(candidatedict, key=candidatedict.get)
print(f"Winner: {winner}")
print("--------------------------")

#Final script should print the analysis to the terminal AND export a text file with the results
with open("C:\\Users\\nguye\\Desktop\\Homework\\Python\\python-challenge\\PyPoll\\Analysis\\electionresults.txt", "w") as pyfile:
    pyfile.write("Election Results\n")
    pyfile.write("-------------------------------------\n")
    pyfile.write(f"Total Votes: {totalvote}\n")
    pyfile.write("-------------------------------------\n")
    pyfile.write(f"{uniquecandidate[0]}: {perc_candidate1}% ({candidate1})\n")
    pyfile.write(f"{uniquecandidate[1]}: {perc_candidate2}% ({candidate2})\n")
    pyfile.write(f"{uniquecandidate[2]}: {perc_candidate3}% ({candidate3})\n")
    pyfile.write(f"{uniquecandidate[3]}: {perc_candidate4}% ({candidate4})\n")
    pyfile.write("-------------------------------------\n")
    pyfile.write(f"Winner: {winner}\n")
    pyfile.write("-------------------------------------\n")
