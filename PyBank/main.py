import os
import csv

#Path of budget_data.csv file
budget_data=r"C:\Users\nguye\Desktop\Homework\Python\python-challenge\PyBank\Resources\budget_data.csv"

#Creating lists
months=[]
profitloss=[]


with open(budget_data, 'r') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    header=next(csvreader)
    for row in csvreader:

#Defining list
        months.append(row[0])
        profitloss.append(int(row[1]))

#Printing header
print("Financial Analysis")
print("-------------------------------------")

#Calculate the total number of months included in the dataset
totalmonth=len(months)
print(f"Total Months: {totalmonth}")

#Calculate the net total amount of "Profit/Losses" over the entire period
totalnet=sum(profitloss)
print(f"Total: ${totalnet}")

#Calculate the difference between each month
difference=[]
change=0
previousrow=0
for row in profitloss:
    #Not equal credit: https://www.edureka.co/community/33869/how-to-use-not-equal-operator-in-python#:~:text=You%20can%20use%20%22!%3D,are%20not%20equal%2C%20otherwise%20false%20.
    if len(difference) != 0:
        change= row-previousrow
    previousrow=row
    difference.append(change)

#Calculate the average of the changes in "Profit/Losses" over the entire period
#Rounding credit: https://www.programiz.com/python-programming/methods/buil
average=round((sum(difference)/((len(difference))-1)),2)
print(f"Average Change: ${average}")

#Calculate the greatest increase in profits (date and amount) over the entire period
maxprofit=max(difference)
maxindexprofit=difference.index(maxprofit)
maxprofitdate=months[maxindexprofit]
print(f"Greatest Increase in Profits: {maxprofitdate} (${maxprofit})")

#Calculate the greatest decrease in losses (date and amount) over the entire period
maxloss=min(difference)
maxindexloss=difference.index(maxloss)
maxlossdate=months[maxindexloss]
print(f"Greatest Decrease in Profits: {maxlossdate} (${maxloss})")

#Final script should print the analysis to the terminal AND export a text file with the results
with open("C:\\Users\\nguye\\Desktop\\Homework\\Python\\python-challenge\\PyBank\\Analysis\\financialanalysis.txt", "w") as pyfile:
    pyfile.write("Financial Analysis\n")
    pyfile.write("-------------------------------------\n")
    pyfile.write(f"Total Months: {totalmonth}\n")
    pyfile.write(f"Total: ${totalnet}\n")
    pyfile.write(f"Average Change: ${average}\n")
    pyfile.write(f"Greatest Increase in Profits: {maxprofitdate} (${maxprofit})\n")
    pyfile.write(f"Greatest Decrease in Profits: {maxlossdate} (${maxloss})\n")