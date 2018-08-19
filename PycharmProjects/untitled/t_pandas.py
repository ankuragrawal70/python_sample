import numpy as np
import pandas as pd

x1 = np.array([4, 3, 4, 4, 8, 4])

products = pd.DataFrame({'category': ['Cleaning', 'Cleaning', 'Entertainment', 'Entertainment', 'Tech', 'Tech'],
                        'store': ['Walmart', 'Dia', 'Walmart', 'Fnac', 'Dia','Walmart'],
                        'price':[11.42, 23.50, 19.99, 15.95, 55.75, 111.55],
                        'testscore': [4, 3, 5, 7, 5, 8]})
#
# s = pd.Series([1, 4, 5])
# print(s[0:2])


def test(x):
    print(np.array(x.as_matrix()).flat)
    # print (type(x.as_matrix()))

print(test(products['price']))
print(type(products['price']))


