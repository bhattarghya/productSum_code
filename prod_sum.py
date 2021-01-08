"""
Submitted by : Arghyadeep Bhattacharjee
Algorithm    : For each recursive call the 'mult' argument
               is multplied with the parent multiplier to get the
               parent multiplier of the next call.
Time take    : 10 mins (approx)
Tested in    : Pytest (test file attached)
"""



def ProductSum(A,mult=1):
    if mult==1 and A==[]:
        print("List is empty")
        return
    elif A==[]: return 0
    result=0
    count=0
    for i in A:
        if type(i)==list:            
            if count%2==0 : even=True
            else: even=False
            if even :                
                result+=ProductSum(i,mult*2)             
            else:                
                result+=ProductSum(i,mult*3)
        else:            
            result += mult*i                                                                                                             
        count+=1    
    return result        



    
