import numpy as nd
listone = [10, 20, 30, 40, 50, 60], [1, 2, 3, 4, 5, 6], [2, 4, 6, 8, 10, 12]
arrayone = nd.array(listone) # Data Type=float,U32,
print(type(arrayone))
print(arrayone)


import numpy as nd
arrayone = nd.arange(1,13) .reshape(3,4)
print(arrayone)

import numpy as nd
arrayone = nd.zeros(6) .reshape(2,3)
print(arrayone)

import numpy as nd
arrayone = nd.twoice(6) .reshape(2,3)
print(arrayone)
