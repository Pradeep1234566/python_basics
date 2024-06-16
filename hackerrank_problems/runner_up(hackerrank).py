if __name__ == '__main__':
    n = int(input())
    arr=[]
    k=(input())
    #print(k)
    num_str_list = k.split()
    arr = []  # Initialize the array to store integers
    max1 = float('-inf') 
    max2 = float('-inf') 
    for num_str in num_str_list:
        a = int(num_str)  
        arr.append(a)
    for i in range(n):
        if(max1<arr[i]):
            max1=arr[i]
    for i in range(n):
        if(max2<arr[i] and arr[i]!=max1):
            max2=arr[i]
    print(max2)