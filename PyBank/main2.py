import os
import csv
os.chdir(os.path.dirname(os.path.abspath(__file__)))
budgetcsv = os.path.join("budget_data.csv")
count = 0
total_months = 0
profitsum = 0
profit_loss = []
profit_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]

with open(budgetcsv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    first_row = next(csvreader)
    profitsum += int(first_row[1])
    previous_profit = int(first_row[1])
    total_months = total_months + 1

    for row in csvreader:
        total_months = total_months + 1
        profitsum += int(row[1])
        netchange = int(row[1])-previous_profit
        previous_profit = int(row[1])
        profit_change_list += [netchange]
        
        if netchange > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = netchange

        if netchange < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = netchange

output_path = os.path.join("output", "new.txt")
pl_average_change = sum(profit_change_list) / len(profit_change_list)
months_G_Increase_Change = 4
greatest_decrease_pl = 40

with open(output_path, "w") as txt_file:
    output = (
        f"Financial Analysis\n"
        f"------------------------\n"
        f"Total Months: {total_months}\n"
        f"Total: ${profitsum}\n"
        f"Average Change: ${pl_average_change:.2f}\n"
        f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
        f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")
    print(output)
    txt_file.write(output)
