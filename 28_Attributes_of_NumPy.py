'''
ndim: एरेको आयामहरूको संख्या ।
shape: एरेको प्रत्येक आयामको आकार ।
size: एरेमा कतिवटा तत्वहरू छन् ।
dtype: एरेमा प्रयोग गरिएको डेटा प्रकार ।
itemsize: एरे कति byte साईजको छ ।
'''

import numpy as nd
listone = [10, 20, 30, 40, 50, 60],
listtwo = [10, 20, 30, 40, 50, 60], [1, 2, 3, 4, 5, 6]
listthree = [[10, 20, 30, 40, 50, 60]], [[1, 2, 3, 4, 5, 6]], [[2, 4, 6, 8, 10, 12]]

arrayone = nd.array(listone)
arraytwo = nd.array(listtwo)
arraythree = nd.array(listthree)

print(arrayone.ndim)
print(arraytwo.ndim)
print(arraythree.ndim)