import os
import csv

election_data=r"C:\Users\nguye\Desktop\Homework\Python\python-challenge\PyPoll\Resources\election_data.csv"



votecount=[]
candidates=[]



with open(election_data, 'r') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    header=next(csvreader)

    for row in csvreader:
        votecount.append(row[0])
        candidates.append(row[2])

print("Election Results")
print("---------------------------")

#Calculate the total number of votes cast

totalvote=len(votecount)
print(f"Total Votes: {totalvote} ")

#A complete list of candidates who received votes

uniquecandidate=[]
for unique in candidates:
    if unique not in uniquecandidate:
        uniquecandidate.append(unique)

print(uniquecandidate)

#The percentage of votes each candidates won and the total number of votes each candidate won

    #Count of each candidate
candidate1=candidates.count(uniquecandidate[0])
candidate2=candidates.count(uniquecandidate[1])
candidate3=candidates.count(uniquecandidate[2])
candidate4=candidates.count(uniquecandidate[3])

    #Percentage of each candidate
perc_candidate1=round((candidate1/len(candidates))*100,3)
perc_candidate2=round((candidate2/len(candidates))*100,3)
perc_candidate3=round((candidate3/len(candidates))*100,3)
perc_candidate4=round((candidate4/len(candidates))*100,3)

print(f"{uniquecandidate[0]}: {perc_candidate1}% ({candidate1})")
print(f"{uniquecandidate[1]}: {perc_candidate2}% ({candidate2})")
print(f"{uniquecandidate[2]}: {perc_candidate2}% ({candidate2})")
print(f"{uniquecandidate[3]}: {perc_candidate3}% ({candidate3})")

print("--------------------------")

#DOES NOT WORK
# candidatelist=[] 
# for i in candidates:
#     #Not equal credit: https://www.edureka.co/community/33869/how-to-use-not-equal-operator-in-python#:~:text=You%20can%20use%20%22!%3D,are%20not%20equal%2C%20otherwise%20false%20.
#     if i != (i+i):
#         candidatename=i
#         candidatelist.append(candidatename)

# print(candidatelist)



#The winnder of the election based on popular vote

print(f"Winner: ")