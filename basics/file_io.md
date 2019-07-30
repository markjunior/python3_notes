Python reads files by using a cursor

```
file = open('io_learning_file.txt')
file.read() # read from the cursor to the end
file.seek(0) # let the cursor go into the index of characters
file.readline()
file.readlines() # return as a list
file.closed # check if it is closed or not
file.close()
```
