"""
Question answers


"""

"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    amount_of_months = int(input("How many months? "))

    for month in range(1, amount_of_months + 1):
        income = float(input("Enter income for month " + str(month) + ": "))
        incomes.append(income)
    def print_the_report():
        print("\nIncome Report\n-------------")
        total = 0
        for month in range(1, amount_of_months + 1):
            income = incomes[month - 1]
            total += income
            print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))
    print_the_report()

main()
