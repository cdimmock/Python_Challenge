# Dimport dependencies
import csv
import os

# get files
budget_data = os.path.join("Resources", "budget_data.csv")
budget_analysis = os.path.join("analysis", "budget_analysis.txt")

# track these components
total_months = 0
month_of_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
total_net = 0

# Read csv and turn it into a list of dictionaries
with open(budget_data) as financial_data:
    reader = csv.reader(financial_data)

    # Read the header 
    header = next(reader)

    # Extract first row so it doesn't go to net change list
    first_row = next(reader)
    total_months = total_months + 1
    total_net = total_net + int(first_row[1])
    prev_net = int(first_row[1])

    for row in reader:

        # find total
        total_months = total_months + 1
        total_net = total_net + int(row[1])

        # find net change
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list = net_change_list + [net_change]
        month_of_change = month_of_change + [row[0]]

        #  greatest increase
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change

        #  greatest decrease
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

# Average Net Change
net_monthly_avg = sum(net_change_list) / len(net_change_list)

# show data
output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average  Change: ${net_monthly_avg:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# Print output 
print(output)

# Export results as a text file
with open(budget_analysis, "w") as txt_file:
    txt_file.write(output)