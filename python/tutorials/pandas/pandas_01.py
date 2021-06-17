import pandas as pd
from termcolor import colored

'''
The primary two components of pandas are the Series and DataFrame.
A Series is essentially a column, and  a DataFrame is a multi-dimensional table made up of a collection of Series.
'''


data = {
    'apples': [3, 2, 0, 1],
    'oranges': [0, 3, 7, 2]
}

purchases = pd.DataFrame(data)
print(colored('Example of auto-indexed DataFrame:\n', 'magenta'), purchases)
print(colored('The Index of this DataFrame was given to us on creation as the numbers 0-3  but we could also create our own when we initialize the  DataFrame.', 'blue'))

purchases = pd.DataFrame(data, index=['A', 'B', 'C', 'D'])

print(colored('Example of modiifed index in DataFrame: \n', 'magenta'),purchases, colored(' \n To do so, we have used the index attribute in DataFrame', 'magenta'))

print(purchases.keys())