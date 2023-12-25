import streamlit as st
import math
import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns

#####################################################
def collatz_sequence(n):
    if not isinstance(n, int) or n < 2 or n > 1e15:
        print("Invalid input, please provide an integer greater than 1 or less than 1e15!")
    else: 
        s = [n]
        while(n > 1):
            if (n%2) ==0:
                n = int(n/2) 
            else:
                n = int(3*n + 1)
            s.append(n)
        return s

#####################################################

def collatz_sequence_plot(n):
    plt.figure(figsize=(15,8))
    sns.set_style('darkgrid')
    plt.plot(collatz_sequence(n),color='red', marker='s', linestyle='dashed',linewidth=2, markersize=3, label= 'n = %i' %n);
    plt.legend(loc="upper right");
    plt.xlabel("Collatz Sequence Length");
    plt.ylabel("Collatz Sequence Value");


#####################################################
# Streamlit app
st.set_option('deprecation.showPyplotGlobalUse', False)
st.title('Collatz Sequence')
st.caption('Developed by : Al Yazdani')
st.caption('**The Collatz Conjecture (1937):** Start with any positive integer n, divide by two if n is even, or multiply by three and add one if n is odd, repeat.\
           The conjecture states that this sequence will eventually reach 1.\
            Almost a century later, the conjecture is still unsolved: no mathematical proof and no counter-example! \
            Studying it nevertheless has lead into several directions intersecting number theory, combinatorics, mathematical analysis, probability and statistics, fractal geometry, and computational complexity.\
            Paul Erdos famously said "Mathematics may not be ready for such problems".\
            Below is a simple python script to calcualte and visualize the Collatz sequence.\
            Do you see a common pattern there?! Read more about the conjecture here (https://en.wikipedia.org/wiki/Collatz_conjecture).')

# Input field for the user to enter an integer value
user_input = st.number_input('Enter an integer value:', step=10, value = 500)

# Calculate the value of the function 'f' based on user input
function_result = collatz_sequence(user_input)

# Display the result
st.write(f'The Collatz sequence for input {user_input} is:n {function_result}')
st.pyplot(collatz_sequence_plot(user_input))

