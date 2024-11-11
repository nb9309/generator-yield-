# generator-yield-

                                        =================================
			                                     	generator in python
			                                  =================================
=>generator is one of the function
=>The generator function always contains yield keyword
=>If the function contains return statement then it is called Normal Function. Here return 
     statement of function can return More Number of Values if required
=>If the function contains yield keyword then it is called generator. Here yield statement 
    returns the value only on demand and reduces the memory space.
    
=>Syntax:
	   	def   function_name(start,stop,step):
		        ----------------------------------------
			      ----------------------------------------
			      yield value
			      ----------------
=>The 'yield' key word is used for giving the value back to function call from function defintion and continue the function execution until condition becomes false and gives StopIteration 
=>The advantage of generators over functions concept is that it save lot of memory space in the case large sampling of data. In otherwords Functions gives all the result at once and it take more memory space where as generators gives one value at a time when programmer requested and takes minimized memory space.
=>On the object of generator, we can't perform Indexing and Slicing Operations bcoz They supply the value only on demand.

----------------------------------------------------------------------------------------
Writing Memory Efficient Programs Using Generators in Python
----------------------------------------------------------------------------------------
When writing code in Python, wise use of memory is important, especially when dealing with large amounts of data. One way to do this is to use Python generators. Generators are like special functions that help save memory by processing data one at a time, rather than all at once.

The logic behind memory efficient functions and Python generators is to create functions that generate values ​​on the fly, avoiding the need to store the entire data set in memory. This is especially useful when dealing with large data sets.
============================X===============================================================
