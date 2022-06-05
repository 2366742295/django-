from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse
from 用户登录 import models
def index(request):
    if request.is_ajax():
        name = request.POST.get('name')
        password = request.POST.get('password')
        age = request.POST.get('age')
        models.UserInfo.objects.create(name=name, password=password, age=age)
        response = JsonResponse({"info":"用户创建成功"})
    if request.method =='GET':
        data_list=models.UserInfo.objects.all()
        return render(request,'index.html',{"data_list":data_list},status=200)
    return redirect("/index/")


def delete(request):
    nid = request.GET.get('nid')
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect('/index')
def edit(request):
    nid = request.GET.get('nid')
    print(nid)
    name = request.POST.get('name')
    print(name)
    password = request.POST.get('password')
    age = request.POST.get('age')
    models.UserInfo.objects.filter(id=nid).update(name=name)
    models.UserInfo.objects.filter(id=nid).update(password=password)
    models.UserInfo.objects.filter(id=nid).update(age=age)

    return redirect('/index')
