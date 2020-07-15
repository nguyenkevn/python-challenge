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
print(f"Total: {totalnet}")

#Calculate the average of the changes in "Profit/Losses" over the entire period
average=round(totalnet/len(profitloss))
print(f"Average Change: {average}")

#Calculate the greatest increase in profits (date and amount) over the entire period
maxprofit=max(profitloss)
maxindexprofit=profitloss.index(maxprofit)
maxprofitdate=months[maxindexprofit]
print(f"Greatest Increase in Profits: {maxprofitdate} ({maxprofit})")

#Calculate the greatest decrease in losses (date and amount) over the entire period
maxloss=min(profitloss)
maxindexloss=profitloss.index(maxloss)
maxlossdate=months[maxindexloss]
print(f"Greatest Decrease in Profits: {maxlossdate} ({maxloss})")

#Final script should print the analysis to the terminal AND export a text file with the results
    