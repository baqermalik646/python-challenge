import os
import csv
import statistics

path = "/Users/muhammadbaqermalik/Desktop"
budget_csv = os.path.join(path, 'DataScienceBootcamp', 'Homework', '03-Python', 'python-challenge','python-challenge', 'PyBank', 'Resources', 'budget_data.csv')

with open(budget_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)

    netTotalAmountOfProfit_losses = []
    monthToMonthChange = []
    total_months = []

    for row in csvreader:
        netTotalAmountOfProfit_losses.append(int(row[1]))
        total_months.append(row[0])


numberOfTotalMonths = len(total_months)
netTotalAmount = sum(netTotalAmountOfProfit_losses)
print("Financial Analysis")
print("------------------------------------")
print(f"Total Months: {numberOfTotalMonths}")
print(f"Total: ${sum(netTotalAmountOfProfit_losses)}")


for i in range(len(netTotalAmountOfProfit_losses)-1):
    monthlyChange = netTotalAmountOfProfit_losses[i + 1] - netTotalAmountOfProfit_losses[i]
    monthToMonthChange.append(monthlyChange)


maxIncreaseValue = max(monthToMonthChange)
minDecreaseValue = min(monthToMonthChange)


greatestIncreaseMonth = monthToMonthChange.index(max(monthToMonthChange)) + 1
greatestDecreaseMonth = monthToMonthChange.index(min(monthToMonthChange)) + 1

average = round(statistics.mean(monthToMonthChange), 2)
print(f"Average Change: ${average}")


print(f"Greatest Increase in Profits: {total_months[greatestIncreaseMonth]} (${maxIncreaseValue})")
print(f"Greatest Decrease in Profits: {total_months[greatestDecreaseMonth]} (${minDecreaseValue})")

path = "/Users/muhammadbaqermalik/Desktop"
output_file = os.path.join(path, 'DataScienceBootcamp', 'Homework', '03-Python', 'python-challenge','python-challenge', 'PyBank', 'analysis', 'Financial_Analysis_Summart.txt')


with open(output_file, "w") as file:

    file.write("Financial Analysis")
    file.write("\n")
    file.write("-------------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(total_months)}")
    file.write("\n")
    file.write(f"Total: ${sum(netTotalAmountOfProfit_losses)}")
    file.write("\n")
    file.write(f"Average Change: ${average}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[greatestIncreaseMonth]} (${maxIncreaseValue})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[greatestDecreaseMonth]} (${minDecreaseValue})")


