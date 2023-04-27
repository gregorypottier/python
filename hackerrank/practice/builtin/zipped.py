# Built in - zipped

numstudents, numsubjects = map(int, input().split())

gradeList = [list(map(float, input().split()))for _ in range(numsubjects)]
    
studentGrades = zip(*gradeList) # unpack a list of lists, then zip elements

for sg in studentGrades:
    print(sum(sg)/numsubjects)
    
