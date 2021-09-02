def das_sort(x):    
    
    offset = 0   
    
    #hello how are you
    if x[0] >= 0:        
        arr = [''] * (x[0])
        arr.append([x[0]])
    
    else:
        arr = (abs(x[0])-1) * ['']
        arr.insert(0, [x[0]])
        offset = abs(x[0])
    

    for i in range(1, len(x)):
        
        
        if x[i] >= 0:
            if arr[-1] == '':
                '''Handle situation when negative number is inserted first'''
                temp = [''] * x[i]
                arr.extend(temp)
                arr.append([x[i]])
            
            elif x[i] > arr[-1][0]:            
                ''' When item being insert is outside of exisiting arr'''
                temp = ['']*(x[i]-arr[-1][0]-1)
                arr.extend(temp)
                arr.append([x[i]])
                
            else: 
                if arr[x[i]+offset] == '':
                    arr[x[i]+offset] = [x[i]]
                else:
                    arr[x[i]+offset].append(x[i])
                    

        else:
            if arr[0] == '':
                temp = (abs(x[i])-1)*['']
                temp.insert(0, [x[i]])
                temp.extend(arr)
                arr = temp
                offset = abs(x[i])
                
            elif x[i] < arr[0][0]:
                temp = (abs(x[i]) - offset -1)*['']
                temp.extend(arr)
                arr = temp
                arr.insert(0, [x[i]])                       
                offset = abs(x[i])
                    
            else:
                if arr[x[i]+offset] == '':
                    arr[x[i]+offset] = [x[i]]
                else:
                    arr[x[i]+offset].append(x[i])

    '''flatten the array'''
    res = []
    for i in arr:
        if i != '':
            res += i
    
    return res



# Driver code
import numpy as np
import random
x = [random.randint(-100, 100) for _ in range(100)]
#x = [-90, -86, -85, -84, -83, -83, -82, -80, -79, -77, -76, -76, -73, -68, -67, -66, -65, -63, -56, -56, -52, -51, -49, -49, -40, -39, -38, -38, -37, -36, -35, -34, -34, -33, -32, -31, -31, -30, -30, -30, -28, -19, -14, -8, -4, -4, -77, -71, 9, 13, 13, 14, 14, 15, 15, 16, 18, 19, 20, 22, 23, 27, -49, 30, 36, 38, 40, 42, 43, 45, 45, 47, 52, 54, 55, -18, 62, 62, 66, 70, 74, 76, 76, 80, 81, 81, 81, 81, 82, 82, 84, 84, 85, 88, 89, 95, -70, -63, 96, 100]
#print(x)
y = das_sort(x)
print('das sort', y)
x.sort()
print('python sort', x)
