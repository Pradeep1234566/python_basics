if __name__ == '__main__':
    n = int(input())
    arr=[]
    k=(input())
    #print(k)
    num_str_list = k.split()
    arr = []  # Initialize the array to store integers
    max1=0
    max2=0
    for num_str in num_str_list:
        a = int(num_str)  
        arr.append(a)
    for i in range(n):
        if(max1<arr[i]):
            max1=arr[i]
   
    for i in range(n):
        if(max2<arr[i] ):
            if(max2!=max2):
                 max2=arr[i]
            else:
                pass
    print(max2)