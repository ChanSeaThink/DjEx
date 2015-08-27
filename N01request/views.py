# -*- coding: utf8 -*-
#此应用关于展示get和post两种请求的例子。
from django.shortcuts import render_to_response
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello World!")

def hello(request):
    if request.method == 'GET':
        return render_to_response('hello.html')
    elif request.method == 'POST':
        message = request.POST['msg']
        #message = request.POST.get('msg', '')此语句为，当获取name为msg的值失败时，自动把第二个参数的值赋给message。
        return render_to_response('hello.html', {'message':message})
    else:
        return HttpResponse('仅支持get和post方法。')