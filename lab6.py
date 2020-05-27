"""
Lab 6
"""

#3.1
for num in range(6):
    if num != 3:
        print(num)
        
#3.2

result_32=1
for num in range(1,6):
    result_32= result_32 * num
print(result_32)

#3.3
result = 0
for num in range(1,6):
    result = result + num
    
print(result)

#3.4
result=1 
for each_num in range(3,9):
    result=result*each_num
print(result)

#3.5
result=1
for num in range(1,9):
    result=result*num
    
divisor=1
for num in range(1,4):
    divisor=divisor*num
    
final_answer=result/divisor
print(final_answer)

#3.6

result = 0
for word in 'this is my 6th string'.split():
    #print(word)
    result = result + 1
print(result)

#3.7

my_tweet = {
    'favorite count':1138,
    'lan':'en',
    'coordinates':(-75,40),
    'entities':{
                'hashtags':['Preds','Pens','SingintoSpring']
        }
}  

result=0
for hashtag in my_tweet ['entities']['hashtags']:
    result=result+1
print(result)