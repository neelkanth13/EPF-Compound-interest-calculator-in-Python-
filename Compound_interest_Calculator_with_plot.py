import tkinter as tk
import matplotlib.pyplot as plt
import locale
import multiprocessing
import matplotlib.pyplot as plt

result_label=None


def calculate(entry_principal, entry_yearly_investment, entry_rate_of_interest, entry_years, q):
    global result_label

    principal = float(entry_principal.get())
    interest = float(entry_yearly_investment.get())
    yearly_contribution = float(entry_yearly_investment.get())
    rate = float(entry_rate_of_interest.get())/100
    years = int(entry_years.get())

    yearly_principle_amt_list = []
    principle_list = []
    for i in range(years):
        # increase principal amount by yearly_contribution
        principle_list.append(int(principal))
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

    q.put(('generate_plot', principle_list)) 

def ui_application(q):
    global result_label
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

    calculate_button = tk.Button(root, text="Calculate", command=lambda: calculate(entry_principal,\
                                                                                   entry_yearly_investment,\
                                                                                   entry_rate_of_interest,\
                                                                                   entry_years,
                                                                                   q))
    calculate_button.grid(row=4, column=0, columnspan=2)

    result_label = tk.Label(root, text="")
    result_label.grid(row=5, column=0, columnspan=2)

    root.mainloop()


# every time calculate button is pressed, plot a new graph and close the previous graph

def generate_plot(principle_list):
    years = len(principle_list)

    print(principle_list)
    print(years)

    # Generate the year values for the x-axis
    x_values = list(range(1, years+1))

    # Plot the graph
    plt.plot(x_values, principle_list)

    # Set the format of the y-axis tick labels to not use scientific notation
    plt.ticklabel_format(style='plain', axis='y')

    # Add labels and title to the graph
    plt.xlabel('Year')
    plt.ylabel('Principle Amount')
    plt.title('Principle Amount vs. Year')

    # Display the graph
    plt.show()

def plotting_application(q):

    while (1):
        message, principle_list = q.get()
        print("Received message: ", message)
        print(principle_list)
        if (message == 'generate_plot'): 
            generate_plot(principle_list)    

if __name__ == '__main__':
    # Create a queue object
    q = multiprocessing.Queue()

    # create two new processes
    p1 = multiprocessing.Process( target=ui_application, args=(q,) )
    p2 = multiprocessing.Process( target=plotting_application, args=(q,) )
    # start the processes
    p1.start()
    p2.start()
    # wait for the processes to complete
    p1.join()
    p2.join()

