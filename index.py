# import csv
# avg_sales_by_country = {}
# with open('product_data.csv', newline='') as csvfile:
#    reader = csv.DictReader(csvfile)
#    for row in reader:
#        if row['Year'] == '2022':
#            country = row['Country']
#            gross_sales = int(row['Gross Sales'])
#            if country not in avg_sales_by_country:
#                avg_sales_by_country[country] = {'Q1': [], 'Q2': [], 'Q3': [], 'Q4': []}
#            avg_sales_by_country[country][row['Quarter']].append(gross_sales)


# avg_sales_pivot = {}
# for country, quarters in avg_sales_by_country.items():
#    avg_sales_pivot[country] = {}
#    for quarter, sales in quarters.items():
#        avg_sales_pivot[country][quarter] = sum(sales) / len(sales)


# print("Country\tQ1\tQ2\tQ3\tQ4\tTotal")
# for country, quarters in avg_sales_pivot.items():
#    total_sales = sum(quarters.values())
#    print(f"{country}\t{quarters['Q1']}\t{quarters['Q2']}\t{quarters['Q3']}\t{quarters['Q4']}\t{total_sales}")

# import csv

# # Function to calculate average sales by country and quarter
# def calculate_avg_sales(file_path):
#     avg_sales_by_country = {}
#     with open(file_path, newline='') as csvfile:
#         reader = csv.DictReader(csvfile)
#         for row in reader:
#             if row['Year'] == '2022':
#                 country = row['Country']
#                 gross_sales = int(row['Gross Sales'])
#                 if country not in avg_sales_by_country:
#                     avg_sales_by_country[country] = {'Q1': [], 'Q2': [], 'Q3': [], 'Q4': []}
#                 avg_sales_by_country[country][row['Quarter']].append(gross_sales)

#     avg_sales_pivot = {}
#     for country, quarters in avg_sales_by_country.items():
#         avg_sales_pivot[country] = {}
#         for quarter, sales in quarters.items():
#             avg_sales_pivot[country][quarter] = sum(sales) / len(sales)
#     return avg_sales_pivot

# # Function to print profit table and summary insights
# def print_profit_table_and_summary(avg_sales_pivot):
#     print("Country\tQ1\tQ2\tQ3\tQ4\tTotal")
#     for country, quarters in avg_sales_pivot.items():
#         total_sales = sum(quarters.values())
#         print(f"{country}\t{quarters['Q1']}\t{quarters['Q2']}\t{quarters['Q3']}\t{quarters['Q4']}\t{total_sales}")

#     # Analyze data for insights
#     max_country = max(avg_sales_pivot, key=lambda x: sum(avg_sales_pivot[x].values()))
#     min_country = min(avg_sales_pivot, key=lambda x: sum(avg_sales_pivot[x].values()))

#     max_sales = sum(avg_sales_pivot[max_country].values())
#     min_sales = sum(avg_sales_pivot[min_country].values())

#     print("\nSummary Insights:")
#     print(f"- {max_country} had the highest total sales in 2022 with a total of {max_sales}.")
#     print(f"- {min_country} had the lowest total sales in 2022 with a total of {min_sales}.")
#     print("- Quarter-wise analysis:")
#     for quarter in ['Q1', 'Q2', 'Q3', 'Q4']:
#         quarter_sales = sum(avg_sales_pivot[country][quarter] for country in avg_sales_pivot)
#         print(f"  - Total sales in {quarter}: {quarter_sales}")

# # Main function
# def main():
#     file_path = 'product_data.csv'
#     avg_sales_pivot = calculate_avg_sales(file_path)
#     print_profit_table_and_summary(avg_sales_pivot)

# if __name__ == "__main__":
#     main()

# import csv

# # Function to calculate average sales by country and quarter
# def calculate_avg_sales(file_path):
#     avg_sales_by_country = {}
#     with open(file_path, newline='') as csvfile:
#         reader = csv.DictReader(csvfile)
#         for row in reader:
#             if row['Year'] == '2022':
#                 country = row['Country']
#                 gross_sales = int(row['Gross Sales'])
#                 if country not in avg_sales_by_country:
#                     avg_sales_by_country[country] = {'Q1': [], 'Q2': [], 'Q3': [], 'Q4': []}
#                 avg_sales_by_country[country][row['Quarter']].append(gross_sales)

#     avg_sales_pivot = {}
#     for country, quarters in avg_sales_by_country.items():
#         avg_sales_pivot[country] = {}
#         for quarter, sales in quarters.items():
#             avg_sales_pivot[country][quarter] = sum(sales) / len(sales)
#     return avg_sales_pivot

# # Function to print profit table and summary insights
# def print_profit_table_and_summary(avg_sales_pivot):
#     # Print table header
#     print("______________________________________________________")
#     print("| Country | Quarter 1 | Quarter 2 | Quarter 3 | Quarter 4 | Total |")
#     print("|---------|-----------|-----------|-----------|-----------|-------|")

#     # Iterate through each country and print sales data
#     for country, quarters in avg_sales_pivot.items():
#         total_sales = sum(quarters.values())
#         print(f"| {country:<7} | {quarters['Q1']:<9.2f} | {quarters['Q2']:<9.2f} | {quarters['Q3']:<9.2f} | {quarters['Q4']:<9.2f} | {total_sales:<5.2f} |")

#     # Print table footer
#     print("|_________|___________|___________|___________|___________|_______|")

#     # Additional analysis and insights can be printed here if needed

# # Main function
# def main():
#     file_path = 'product_data.csv'
#     avg_sales_pivot = calculate_avg_sales(file_path)
#     print_profit_table_and_summary(avg_sales_pivot)

# if __name__ == "__main__":
#     main()


# import csv

# # Function to calculate average sales by country and quarter
# def calculate_avg_sales(file_path):
#     avg_sales_by_country = {}
#     with open(file_path, newline='') as csvfile:
#         reader = csv.DictReader(csvfile)
#         for row in reader:
#             if row['Year'] == '2022':
#                 country = row['Country']
#                 gross_sales = int(row['Gross Sales'])
#                 if country not in avg_sales_by_country:
#                     avg_sales_by_country[country] = {'Q1': [], 'Q2': [], 'Q3': [], 'Q4': []}
#                 avg_sales_by_country[country][row['Quarter']].append(gross_sales)

#     avg_sales_pivot = {}
#     for country, quarters in avg_sales_by_country.items():
#         avg_sales_pivot[country] = {}
#         for quarter, sales in quarters.items():
#             avg_sales_pivot[country][quarter] = sum(sales) / len(sales)
#     return avg_sales_pivot

# # Function to print profit table and summary insights
# def print_profit_table_and_summary(avg_sales_pivot):
#     # Print table header
#     print("______________________________________________________")
#     print("| Country | Quarter 1 | Quarter 2 | Quarter 3 | Quarter 4 | Total |")
#     print("|---------|-----------|-----------|-----------|-----------|-------|")

#     # Iterate through each country and print sales data
#     for country, quarters in avg_sales_pivot.items():
#         total_sales = sum(quarters.values())
#         print(f"| {country:<7} | {quarters['Q1']:<9.2f} | {quarters['Q2']:<9.2f} | {quarters['Q3']:<9.2f} | {quarters['Q4']:<9.2f} | {total_sales:<5.2f} |")

#     # Print table footer
#     print("|_________|___________|___________|___________|___________|_______|")

#     # Additional analysis and insights
#     max_country = max(avg_sales_pivot, key=lambda x: sum(avg_sales_pivot[x].values()))
#     min_country = min(avg_sales_pivot, key=lambda x: sum(avg_sales_pivot[x].values()))

#     max_sales = sum(avg_sales_pivot[max_country].values())
#     min_sales = sum(avg_sales_pivot[min_country].values())

#     print("\nSummary Insights:")
#     print(f"- {max_country} had the highest total sales in 2022 with a total of {max_sales:.2f}.")
#     print(f"- {min_country} had the lowest total sales in 2022 with a total of {min_sales:.2f}.")

#     # Quarter-wise analysis
#     for quarter in ['Q1', 'Q2', 'Q3', 'Q4']:
#         quarter_sales = sum(avg_sales_pivot[country][quarter] for country in avg_sales_pivot)
#         print(f"  - Total sales in {quarter}: {quarter_sales:.2f}")

# # Main function
# def main():
#     file_path = 'product_data.csv'
#     avg_sales_pivot = calculate_avg_sales(file_path)
#     print_profit_table_and_summary(avg_sales_pivot)

# if __name__ == "__main__":
#     main()


import csv

# Function to calculate average sales by country and quarter
def calculate_avg_sales(file_path):
    avg_sales_by_country = {}
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Year'] == '2022':
                country = row['Country']
                gross_sales = int(row['Gross Sales'])
                if country not in avg_sales_by_country:
                    avg_sales_by_country[country] = {'Q1': [], 'Q2': [], 'Q3': [], 'Q4': []}
                avg_sales_by_country[country][row['Quarter']].append(gross_sales)

    avg_sales_pivot = {}
    for country, quarters in avg_sales_by_country.items():
        avg_sales_pivot[country] = {}
        for quarter, sales in quarters.items():
            avg_sales_pivot[country][quarter] = sum(sales) / len(sales)
    return avg_sales_pivot

# Function to calculate quarter-over-quarter growth rates
def calculate_growth_rates(avg_sales_pivot):
    growth_rates = {}
    for country, quarters in avg_sales_pivot.items():
        growth_rates[country] = {}
        for i in range(1, 4):
            current_sales = avg_sales_pivot[country][f'Q{i}']
            next_sales = avg_sales_pivot[country][f'Q{i+1}']
            growth_rate = ((next_sales - current_sales) / current_sales) * 100
            growth_rates[country][f'Q{i} to Q{i+1}'] = growth_rate
    return growth_rates

# Function to print profit table and summary insights
def print_profit_table_and_summary(avg_sales_pivot):
    # Print profit table
    print("______________________________________________________")
    print("| Country | Quarter 1 | Quarter 2 | Quarter 3 | Quarter 4 | Total |")
    print("|---------|-----------|-----------|-----------|-----------|-------|")
    for country, quarters in avg_sales_pivot.items():
        total_sales = sum(quarters.values())
        print(f"| {country:<7} | {quarters['Q1']:<9.2f} | {quarters['Q2']:<9.2f} | {quarters['Q3']:<9.2f} | {quarters['Q4']:<9.2f} | {total_sales:<5.2f} |")
    print("|_________|___________|___________|___________|___________|_______|")

    # Additional analysis and insights can be printed here if needed

    # Summary insights
    total_sales_by_country = {country: sum(quarters.values()) for country, quarters in avg_sales_pivot.items()}
    max_country = max(total_sales_by_country, key=total_sales_by_country.get)
    min_country = min(total_sales_by_country, key=total_sales_by_country.get)
    max_sales = total_sales_by_country[max_country]
    min_sales = total_sales_by_country[min_country]

    print("\nSummary Insights:")
    print(f"- {max_country} had the highest total sales in 2022 with a total of {max_sales:.2f}.")
    print(f"- {min_country} had the lowest total sales in 2022 with a total of {min_sales:.2f}.")

# Function to print growth rates
def print_growth_rates(growth_rates):
    print("\nQuarterly Growth Rates:")
    for country, growths in growth_rates.items():
        print(f"- {country}:")
        for quarter, growth_rate in growths.items():
            print(f"  - {quarter}: {growth_rate:.2f}%")

# Main function
def main():
    file_path = 'product_data.csv'
    avg_sales_pivot = calculate_avg_sales(file_path)
    print_profit_table_and_summary(avg_sales_pivot)
    growth_rates = calculate_growth_rates(avg_sales_pivot)
    print_growth_rates(growth_rates)

if __name__ == "__main__":
    main()
