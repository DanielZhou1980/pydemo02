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
