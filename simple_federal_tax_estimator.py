# https://www.irs.gov/filing/federal-income-tax-rates-and-brackets

SINGLE_TAXPAYER_RATES_2023 = [
    (0, .10), (11000, 0.12), (44725, 0.22), (95375, 0.24), (182100, 0.332), (231250, 0.35), (578125, 0.37)]


def calculate(taxable_income):
    running_total_tax = 0
    remaining_taxable_income = taxable_income
    for bracket, rate in SINGLE_TAXPAYER_RATES_2023[::-1]:
        if remaining_taxable_income > bracket:
            portion = (remaining_taxable_income - bracket)
            running_total_tax = running_total_tax + (portion * rate)
            remaining_taxable_income = remaining_taxable_income - portion

    return running_total_tax


if __name__ == '__main__':
    from math import ceil, floor

    while True:
        try:
            usr_input = float(input("Estimate federal income tax for: "))
            if usr_input % 1 >= 5:
                usr_input = ceil(usr_input)
            else:
                usr_input = floor(usr_input)
        except Exception as e:
            print(e)
            continue

        print(calculate(usr_input))
