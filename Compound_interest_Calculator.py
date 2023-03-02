import tkinter as tk
import matplotlib.pyplot as plt
import locale

def calculate():
    principal = float(entry_principal.get())
    interest = float(entry_yearly_investment.get())
    yearly_contribution = float(entry_yearly_investment.get())
    rate = float(entry_rate_of_interest.get())/100
    years = int(entry_years.get())

    yearly_principle_amt_list = []
    for i in range(years):
        # increase principal amount by yearly_contribution
        principal = principal + yearly_contribution
        # calculate interest on new principal amount
        interest = principal * rate
        print(f'Year: {i}  Net Principle Amt: {int(principal)} interest: {int(interest)}')
        yearly_principle_amt_list.append(f'Year: {i}  Net Principle Amt: {int(principal)} interest: {int(interest)}')
        # add interest to principal amount
        principal += interest

    list_string = "\n".join([str(x) for x in yearly_principle_amt_list])
    result_label.config(text=\
                        "This is how the Invested Amount will get compounded every year...\n" +
                        str(list_string) + \
                        '\n' + \
                        '#####################################################################\n' + 
                        "Final Amount at the end of year {}: ==>  {} ₹".format(years, int(principal)) +
                        '\n' + \
                        '#####################################################################\n')

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Neelkanth's Compound Interest Calculator")

    label_principal = tk.Label(root, text="Current Principal(can be 0 or whatever is already invested):")
    label_principal.grid(row=0, column=0)

    entry_principal = tk.Entry(root)
    entry_principal.grid(row=0, column=1)

    label_yearly_investment = tk.Label(root, text="Yearly Investment(Starting from Current Year):")
    label_yearly_investment.grid(row=1, column=0)

    entry_yearly_investment = tk.Entry(root)
    entry_yearly_investment.grid(row=1, column=1)

    label_rate_of_interest = tk.Label(root, text="Rate of Interest (%):")
    label_rate_of_interest.grid(row=2, column=0)

    entry_rate_of_interest = tk.Entry(root)
    entry_rate_of_interest.grid(row=2, column=1)

    label_years = tk.Label(root, text="Number of Years(Starting from current year):")
    label_years.grid(row=3, column=0)

    entry_years = tk.Entry(root)
    entry_years.grid(row=3, column=1)

    calculate_button = tk.Button(root, text="Calculate", command=calculate)
    calculate_button.grid(row=4, column=0, columnspan=2)

    result_label = tk.Label(root, text="")
    result_label.grid(row=5, column=0, columnspan=2)

    root.mainloop()
