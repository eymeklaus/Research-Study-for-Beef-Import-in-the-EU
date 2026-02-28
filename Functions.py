def top_ten(total_expenditure):
    return total_expenditure.nlargest(5, "Total Expenditure")