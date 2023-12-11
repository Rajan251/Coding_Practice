import numpy as np
MyList = input()
my_dict = {i:MyList.count(i) for i in MyList}
my_array = np.array(my_dict)
print (my_array)

