# Import Dependencies
import os
import csv

# Create file path
csv_path = os.path.join("Resources", "budget_data.csv")

# Open file as cvs file and skip headers
with open(csv_path, newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    next(csv_reader)
    # Create counter for total number of months, net profits/losses, etc.
    count_months = 0
    total_net = 0
    store_profit = []
    change = []
    max_increase = 0
    max_decrease = 0
    # Loop through each row of data
    for row in csv_reader:
        # Convert monthly profit to integer and append to list "store_profit"
        month_prof = int(row[1])
        store_profit.append(month_prof)
        # Start calculating change between months starting at 2nd row a
        if count_months > 0:
            change.append(store_profit[count_months] - store_profit[count_months - 1])
        # Increase month counter by one and add monthly profit/loss to total
        count_months += 1
        total_net += month_prof
        # Use if statement to determing whether new monthly profit is greater/less than previous month
        if month_prof > max_increase:
            max_increase = month_prof
            max_imonth = row[0]
        elif month_prof < max_decrease:
            max_decrease = month_prof
            max_dmonth = row[0]
    # Calculate average of "change" list to get average change over months
    average_change = round((sum(change)/len(change)), 2)
    # Print to terminal
    print('Financial Analysis')
    print('-------------------------------')
    print(f'Total Months: {count_months}')
    print(f'Total: ${total_net}')
    print(f'Average change: ${average_change}')
    print(f'Greatest Increase in Profits: {max_imonth} (${max_increase})')
    print(f'Greatest Decrease in Profits: {max_dmonth} (${max_decrease})')
    # Print to .txt file
    with open("PybankResults.txt", "w") as text_file:
        print('Financial Analysis', file=text_file)
        print('-------------------------------', file=text_file)
        print(f'Total Months: {count_months}', file=text_file)
        print(f'Total: ${total_net}', file=text_file)
        print(f'Average change: ${average_change}', file=text_file)
        print(f'Greatest Increase in Profits: {max_imonth} (${max_increase})', file=text_file)
        print(f'Greatest Decrease in Profits: {max_dmonth} (${max_decrease})', file=text_file)
