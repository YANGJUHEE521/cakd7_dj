from multiprocessing.connection import answer_challenge
from django.shortcuts import render

def inputdata(request):
    return render(request, 'program/inputdata.html')

def result(request):
    lis = []
    lis.append(request.GET['a'])
    lis.append(request.GET['b']) #a, b를 받아서

    sum = 0
    for l in lis:
        sum += int(l)
    
    ans = sum 

    return render(request, 'program/result.html', {'ans':ans, 'lis':lis}) #결과를 랜더링
    # return render(request, 'program/result.html') #세팅만 확인하고 지우삼 ~ 