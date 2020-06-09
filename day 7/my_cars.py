#my own self thought recursion solution to this problem
def my_cars(arr):
    '''
    finds maximum sm of non adjacent elements in an array
    '''
    if len(arr)==0:
        return 0
    if len(arr)==1:
        return arr[0]
    else:
        ans=[]
        for i in range(2):
            #find max excuding the element beside the the current element
            a=my_cars(arr[i+2:])
            ans.append(arr[i]+a)
        return max(ans)
    


    

#a better recursion solution using Memoization
def My_cars(arr):
    ans=[0]*len(arr)#holds the maximum value for taking each car
    return mc(arr,0,ans)

def mc(arr,i,ans):
    #with respect to the index in view
    #the answer= max(sum including that index,
    #sum excluding that index(i.e including the next index))
    if i>len(arr)-1:
        return 0
    else:
        if ans[i]!=0:
            return ans[i]
        else:
            ans[i]=max(arr[i]+mc(arr,i+2,ans)#taking this current element, excluding the next element
                       ,mc(arr,i+1,ans))# excluding this element and using the next element
            return ans[i]




#using Dynamic programming of the above
def MY_CARS(arr):
    dp=[0]*(len(arr)+2)
    
    for i in range(len(arr)-1,-1,-1):
        dp[i]=max(dp[i+2]+arr[i],dp[i+1])
  
    return dp



#special method found on geeksforgeeks
def myc(arr):
    #at every point in time.
    incl=0#reprents the maximum value I get if I inlcude the current car
    excl=0#maximum value I get if I exclude tthe current car
    for i in arr:
        #if I include a number. I get the value + the maximum of excluding the previous
        #remember no two adjacent cars can be chosen
        n_incl=excl+i 
        #if i exclude the number I could choose to include or not to include the previous one.
        #I use max to determine
        excl=max(incl,excl)
        incl=n_incl
    return max(incl,excl)

#Just to confirm that all functions work properly

a=[[17,8,14,12,10,2,7,17],
   [10,14,5,12,17,11,1,9,3,5],
   [16,1,7,5,14,3,13,17,9,8,11,14,10],
   [8,12,2,7,10,12,14,8,3,7,10,6,18,18,9]]

for i in a:
    print(myc(i))
    print(My_cars(i))
    print(my_cars(i))
    print()
    print()
    
