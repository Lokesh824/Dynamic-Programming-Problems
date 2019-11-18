# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 12:56:09 2019

@author: inkuml05
"""
'''
Finding the Longest increasing subsequence in the given array 
    i/p - 4, 3, 9, 7, 6, 8, 20

We need to find the longest increasing subsequence in the given array, the possible outcomes are,
4,9,8,20
3, 9, 20
etc...

Explanation - 

Here  we are storing the immediate results in output array

output array - |NULL|NULL|NULL|NULL|NULL|NULL|NULL|


now i loop starts 
since the first element in the input array can have only one sequence that is the element itself so we add one 
to its index in output array

output array - |1|NULL|NULL|NULL|NULL|NULL|NULL|

Now j will be iterating reverse towards i
so j = i-1, since it is negative it will move out of j loop 

now i = 1
so j = 1-1 = 0
we update the output array

it will enter while loop, since the j value is j>=0
now check if the i> j ... 3>4 the cond fails 
we move to the next element updating i value 
the output array is still updated with 1 because we have one sub seq of the prev element 
the output array is,
output array - |1|1|NULL|NULL|NULL|NULL|NULL|


now i = 9
we check and update the output array,
here already jth index had value 1 and now the if condition is also true so we update as 2
output array - |1|1|2|NULL|NULL|NULL|NULL|


The above steps are repeated and we get the final output array as 

|1|1|2|2|2|3|4|

we find the max value and return as it is the maximum increasing subseq..


'''
def LIS(inp):
    output = [None]* len(inp)
    for i in range(0,(len(inp))):
        print('i loops from',i, 'value at i is', inp[i])
        output[i] = 1
        j = i-1
        while j>=0:         
            print('Checking if {0} is less than {1}'.format(inp[j], inp[i]))
            if(inp[i] > inp[j]):
                print('yes, updating output array')                
                output[i] = output[j] + 1               
                print('updated value at',i,' index in output array is', output[i])
                break
                
            else:
                print('No')
                
            j= j-1
    print('\n The Final Sequence stored is...',output)
    print('The Longest increasing sub sequence is ..',max(output))

inp = [4,3,9,7,6,8,20]
LIS(inp)
        