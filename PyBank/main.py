import os
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join ('Resources', 'budget_data.csv')

months = []
profit = []

# Read the CSV file
with open(budget_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    #loop through each row of the file to get the month and the profits/loss
    for row in csvreader:
        months.append(row[0])
        profit.append(int(row[1])) #convert str with profit into integer so we can calculate things later

    # Total number of months
    total_months = len(months)
    print(f'Total months: {total_months}')
    
    # The net total amount of "Profit/Losses" over the entire period
    total_profit = sum(profit)
    print(f'Total profit: ${total_profit}')

    # The changes in "Profit/Losses" over the entire period, and then the average of those changes
    change = []
    month_change = []
    i = 1

    # Loop through profits and calculate changes subtracting previous months from current month
    for i in range(i,len(profit)):
        change.append(profit[i] - profit[i-1])
        # Store the months that changes are being computed for
        month_change.append(months[i])
    
    # Calculate average of changes
    av_change = sum(change)/len(change)
    print(f'Average Change: ${round(av_change,2)}')

    # The greatest increase in profits (date and amount) over the entire period
    max_value = max(change)
    max_month = month_change[change.index(max_value)]
    print(f'Greatest Increase in Profits: {max_month} (${max_value})')
    
    # The greatest decrease in profits (date and amount) over the entire period
    min_value = min(change)
    min_month = month_change[change.index(min_value)]
    print(f'Greatest Decrease in Profits: {min_month} (${min_value})')

    # Write the text file
    output_path = os.path.join ('analysis', 'pybank.txt')

    with open(output_path, 'w') as text:
        text.write ('Financial analysis \n'
                    '---------------------------------- \n'
                    f'Total months: {total_months} \n'
                    f'Total profit: ${total_profit} \n'
                    f'Average Change: ${round(av_change,2)} \n'
                    f'Greatest Increase in Profits: {max_month} (${max_value}) \n'
                    f'Greatest Decrease in Profits: {min_month} (${min_value})')