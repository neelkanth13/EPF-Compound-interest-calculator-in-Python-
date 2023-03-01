############################################################################################
# x = 10000  (Initial Amount)
# years = 20 (Time period)
# rate = 8%  
# Every year investment = replace 165000 with the amount that you would invest every year
#
# The below code will give the final amount accumulated at the end of the time period 
# also plot the graph that would should the exponential power of compound interest. 
############################################################################################

import matplotlib.pyplot as plt
import locale

def compound_interest(x, years):
    # initial principal amount
    principal = x
   
    # fixed interest rate
    rate = 0.08
   
    # create list to store principal amounts for each year
    principal_list = [principal]
   
    print(f'Current principle amount: {int(principal)}')
    # calculate compound interest for specified number of years
    for i in range(years):
        # increase principal amount by x+165000
        principal = principal + 165000
        # calculate interest on new principal amount
        interest = principal * rate
        print(f'Year: {i}  principle amount: {int(principal)} interest: {int(interest)}')
        # add interest to principal amount
        principal += interest
        # add new principal amount to list
        principal_list.append(principal)
   
    # plot the principal amounts over the years
    locale.setlocale(locale.LC_ALL, 'en_IN')
    plt.plot(range(years+1), principal_list)
    plt.title("Compound Interest over {} Years".format(years))
    plt.xlabel("Year")
    plt.ylabel("Principal Amount (₹)")
    plt.ticklabel_format(style='plain', axis='y')
    plt.gca().yaxis.set_major_formatter(locale.currency)
    plt.grid(True)
    plt.show()
   
    # return final principal amount
    return principal


x = 10000
years = 20

final_amount = compound_interest(x, years)
locale.setlocale(locale.LC_ALL, 'en_IN')
print("Final amount after {} years: {}".format(years, locale.currency(final_amount, grouping=True)))
