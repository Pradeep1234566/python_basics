if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    a=[]
    for i in student_marks.keys():
        if(i==query_name):
            a=student_marks[i]
    sum=0
    for i in a:
        sum=sum+i
    print(f"{sum / 3:.2f}")
