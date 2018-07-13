import numpy as np

##------------Array initialization------------------------------
print(np.arange(1,10,2)) #start,end,stepsize
np.zeros(5,5) #rows,columns
np.ones(5,5) #rows,columns
np.linspace(1,5,10) #rows,columns,number of pints needed
np.eye(4) #Identity Matrix (square in size and diagonal is 1)
np.random.rand(5,5) #rows,columns
np.random.randn(2) #returns numbers distributed normally around 0
np.random.randint(1,100,10) #low, high, how many numbers required


##-----------Aray operation------------------
arr = np.arange(25)
arr.reshape(5,5) #reshape an existing array, will throw error if number of elemnet in the existing array are not equal to number of elements required to reshape in passed dimensions.

ranr = np.random.randint(0,50,10)
ranr.max() #max number in array
ranr.min() #min number in array
ranr.argmax() #index of max number in array
ranr.argmin() #index of min number in array

arr.shape #gives number of rows and column as a tuple.
arr.dtype #returns datatype of elements in array.

##-------------Array Copying------------------
##numpy arrays are not copied when we assign a slice of one array to another varialble.
##So when you change the newly created array the original one will alos gets changed.
##to overcome this we need to specifically used copy method.
arr = np.arange(25)
arr_copy = arr.copy()

##---------------2D Array indexing-------------------
arr[0,1]
arr[0][1]

##----------Array Conditional selection------------
arr = np.arange(1,10)
bool_arr = arr > 5 #This will generate a boolean array(TRUE/FALSE) or we can say replace all the array elements with values TRUE or FALSE depending upon which one of them satisfies the condition > 5. All elements > 5 will be replaced by TRUE and rest all will be FALSE.
arr[bool_arr] #When you specify a boolean array as an index of an array, only elements with a correspoding value as TRUE will be returned.
arr[arr>5] #Short hand notation of above 2 steps can be combined in a single statemmnet like this.

##-------------Array with Array operations-------------
arr = np.arange(0,11)
print(arr)
print(arr + arr) ## This will work as add operation would be done element by element.

arr1 = np.arange(0,6)
print(arr1)
print(arr + arr1) ## This will throw error bacause Array to array operations cannot be performed with different sized arrays.

##--------------Array with Scaler Operations-------------
## In array to array perations both array's should be of same lenght but we can also perform these operations with scalar value.
arr = arr + 5 ## This will broadcast 5 to each element in the arr and will add 5 to each elemnt of the arr. 

## For both array to array and array to scalar operations, numpy will not throw exceptions in situations like divide by zero.
## Instead it will show a warning and the problamatic value will be either set ti nan or infinity, but operation will still occur for all other elements of array and an array will be returned.

##--------------Universal Array Functions-------------------
##numpy has provided a lot of inbuilt functions to perform common operations on numpy arrays.
np.max(arr) #This will find the max element in the numpy array passed as parameter.
## You can find all these universal functions in numpy documentation.



