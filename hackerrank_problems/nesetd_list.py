if __name__ == '__main__':
    num_entries = int(input())
    min_score = 2000000
    score_dict = {}
    # Input name and score pairs
    for _ in range(num_entries):
        name = input()
        score = float(input())
        
        if score < min_score:
            min_score = score
        
        score_dict[name] = score

    m2=2000000
    # Print the names after all entries are input
    for key in score_dict.keys():
        if(m2>score_dict[key] and score_dict[key]!=min_score):
            m2=score_dict[key]
    a=[]
    for key in score_dict.keys():
        if(score_dict[key]==m2):
            a.append(key)
    a.sort()
    for i in a:
        print(i)