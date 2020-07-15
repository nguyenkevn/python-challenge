import os
import csv

#Path of budget_data.csv file
budget_data=r"C:\Users\nguye\Desktop\Homework\Python\python-challenge\PyBank\Resources\budget_data.csv"

#Define function for Financial Analysis
def financial_analysis(row):
    months=row[0]
    profitloss=row[1]
    print("Financial Analysis")
    print("-------------------------------------")

#Calculate the total number of months included in the dataset
    totalmonth=len(months)
    print(f"Total Months: {totalmonth}")

#Calculate the net total amount of "Profit/Losses" over the entire period
    totalnet=sum(profitloss)
    print(f"Total: {totalnet}")

#Calculate the average of the changes in "Profit/Losses" over the entire period

    average=totalnet/len(profitloss)
    print(f"Average Change: {average}")

#Calculate the greatest increase in profits (date and amount) over the entire period

    maxprofit=max(profitloss)
    print(f"Greatest Increase in Profits: {maxprofit}")

#Calculate the greatest decrease in losses (date and amount) over the entire period

    maxloss=min(profitloss)
    print(f"Greatest Decrease in Profits: {maxloss}")

#Final script should print the analysis to the terminal AND export a text file with the results

with open(budget_data, 'r') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')

    yes_no = input("Would you like the financial analysis?(Yes or No)")

    for row in csvreader:

        if (yes_no=="Yes"):
            financial_analysis(row)
        else:
            print("No financial analysis requested")

    