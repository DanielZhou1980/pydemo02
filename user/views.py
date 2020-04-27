import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render


# Create your views here.
def login(request):
    if request.POST:
        # request.POST['q']
        # request.POST.get('q')
        user = request.POST['username']
        print(request.POST['username'])
        print(request.POST.get('password'))

        request.session['login'] = '已经登录'
        return render(request, 'index.html', context={'username': user})
    # get方法
    print(request.GET['id'])
    return render(request, 'login.html')


def getjson(request):
    myjson = {
        'username': '周大哥',
        'password': '123456'
    }
    #return JsonResponse(myjson)
    return HttpResponse(json.dumps(myjson), content_type='application/json')
    # listdata = ["张三", "25", "19000347", "上呼吸道感染"]
    # return JsonResponse(listdata, safe=False)


def json2(request):
    result = json.loads(request.body)
    print(result['ID'])
    return render(request, 'login.html')