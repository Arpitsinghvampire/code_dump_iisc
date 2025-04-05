import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import math
def index(last_list,filter_size,stride,frame_size):
    m,n = filter_size.shape
    k,l = frame_size.shape
    if last_list == [0,0,0,0]:
        print([0,0,m,n])
        return [0,0,m,n]
    else:
        if last_list[2]+stride+m<=k and last_list[3]<=l:
            print([last_list[0]+stride,last_list[1],last_list[2]+stride,last_list[3]])
            return [last_list[0]+stride,last_list[1],last_list[2]+stride,last_list[3]]
        
        elif (last_list[2]+stride+m>k and last_list[3]+stride+n<=l):
            print([0,last_list[1]+stride,m,last_list[3]+stride])
            return [0,last_list[1]+stride,m,last_list[3]+stride]
        
        else:
            return None

def convolution_operator(frame ,filter_size,stride):
    #now we have created  a function that gives us a range of indices 
    #we need to convolve the frame with the filter
    final_tensor = []
    index_list = index([0,0,0,0],filter_size,stride,frame)
    while index_list :
        intermediate = []
        for i in range(index_list[0],index_list[2]):
            for j in range(index_list[1],index_list[3]):
                intermediate.append(frame[i,j])
        intermediate = np.asarray(intermediate)
        intermediate = np.reshape(intermediate,filter_size.shape)
        output_array = filter_size* intermediate
        final_tensor.append(np.sum(output_array))
        index_list = index(index_list,filter_size,stride,frame)
        
    final_tensor = np.asarray(final_tensor)
    final_tensor = final_tensor.reshape(math.floor((frame.shape[0]-filter_size.shape[0])/stride),math.floor((frame.shape[1]-filter_size.shape[1])/stride))
    
    return final_tensor


filter_size = np.asarray([1,2,3,1,2,3,1,2,3])
print(filter_size.shape)

filter_size = np.reshape(filter_size,[3,3])
print(filter_size.shape)

image = [1]*256**2

print(image)
image = np.asarray(image)

image = np.reshape(image,[256,256])

print(image.shape)

stride_length  = int(input("enter the stride you want to observe "))

#now we have the image and the filter size 
convolved_tensor = convolution_operator(image ,filter_size,stride_length)

print("the shape of the convolved tensor is ", convolved_tensor.shape)


#check whether the array is in a decreasing order or not 
l = [5,3,2,1,8,9,10]
m = l.sort(reverse=True)

if l == m:
    print("yes")
    
else:
    print("no")