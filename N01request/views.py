# -*- coding: utf8 -*-
#此应用关于展示get和post两种请求的例子。
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello World!")