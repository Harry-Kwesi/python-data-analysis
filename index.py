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
                month_name = row[' Month Name '].strip()  # Corrected key access
                quarter = get_quarter(month_name)
                if quarter is not None:
                    if country not in avg_sales_by_country:
                        avg_sales_by_country[country] = {'Q1': [], 'Q2': [], 'Q3': [], 'Q4': []}
                    avg_sales_by_country[country][quarter].append(gross_sales)

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

# Function to get quarter from month name
def get_quarter(month_name):
    if month_name in ('January', 'February', 'March'):
        return 'Q1'
    elif month_name in ('April', 'May', 'June'):
        return 'Q2'
    elif month_name in ('July', 'August', 'September'):
        return 'Q3'
    elif month_name in ('October', 'November', 'December'):
        return 'Q4'
    else:
        return None

# Function to print profit table and summary insights
def print_profit_table_and_summary(avg_sales_pivot):
    # 1. Print profit table
    print("____________________________________________________________________________________________________")
    print("| Country                        | Quarter 1 | Quarter 2 | Quarter 3 | Quarter 4 | Total           |")
    print("|--------------------------------|-----------|-----------|-----------|-----------|-----------------|")
    total_sales_by_country = {country: sum(quarters.values()) for country, quarters in avg_sales_pivot.items()}
    for country, quarters in avg_sales_pivot.items():
        total_sales = sum(quarters.values())
        q1_sales = quarters['Q1'] if 'Q1' in quarters else 0
        q2_sales = quarters['Q2'] if 'Q2' in quarters else 0
        q3_sales = quarters['Q3'] if 'Q3' in quarters else 0
        q4_sales = quarters['Q4'] if 'Q4' in quarters else 0
        print(f"| {country:<30} | {q1_sales:<9.2f} | {q2_sales:<9.2f} | {q3_sales:<9.2f} | {q4_sales:<9.2f} | {total_sales:<15.2f} |")
    print("|________________________________|___________|___________|___________|___________|_________________|")

    # 2. Summary insights
    max_country = None
    min_country = None
    max_sales = float('-inf')
    min_sales = float('inf')

    for country, sales in total_sales_by_country.items():
        if sales > max_sales:
            max_sales = sales
            max_country = country
        if sales < min_sales:
            min_sales = sales
            min_country = country

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

#3b explain how such analysis adds value to the analysis.
# Quarterly growth rates allow you to identify trends in sales performance. Positive growth rates indicate increasing sales, while negative growth rates suggest declining sales. By examining these trends, you can understand how sales are evolving over time and whether there are any notable fluctuations or patterns.
#Assessing Performance: Comparing growth rates across different quarters provides insights into the relative performance of each period. For example, if sales growth accelerates in a particular quarter compared to the previous one, it may indicate successful marketing campaigns or seasonal factors driving increased demand.
#Forecasting: Analyzing historical growth rates enables you to make informed predictions about future sales performance. By knowing the trends from past growth rates, you can estimate future sales levels and adjust business strategies accordingly.

# Main function
def main():
    file_path = 'product_data.csv'
    avg_sales_pivot = calculate_avg_sales(file_path)
    print_profit_table_and_summary(avg_sales_pivot)
    growth_rates = calculate_growth_rates(avg_sales_pivot)
    print_growth_rates(growth_rates)

if __name__ == "__main__":
    main()





#DELETE THIS PART. THIS IS JUST FOR YOUR KNOWLEDGE
#If you use .keys(), it will return a view object that displays a list of all the keys in the dictionary. This means you would be printing the keys themselves, not the corresponding values (sales).
#If you use .values(), it will return a view object that displays a list of all the values in the dictionary. However, it would not allow you to handle the case where a quarter is missing for a particular country.

# So to solve the problem of not using .get() I used conditional statements to check if the key exists in the dictionary and then access its value if it does.
