# _*_ encoding:utf-8 _*_

from django.shortcuts import render
from django.views.generic.base import View
from . models import Article
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate,login #验证有户名和密码

class AboutView(View):
    def get(self,request):
        return render(request,"about.html")


class ListpicView(View):
    def get(self,request):
        return render(request, "listpic.html")


class NewslispicView(View):
    def get(self,request):
        return render(request, "newslistpic.html")


class indexView(View):
    def get(self,request):
        articles =Article.objects.all()
        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        # Provide Paginator with the request object for complete querystring generation
        p = Paginator(articles,6,request=request)
        orgs = p.page(page)
        return render(request,'index.html',{'articles':orgs})



def article_page(request,article_id):
    article = Article.objects.get(pk=article_id)
    return render(request,'content.html',{'article':article})


class LoginView(View):
    def post(self,request):
        user_name =request.POST.get("username","")
        pass_word = request.POST.get("password", "")#拿到用户名和密码之后要去验证
        user = authenticate(user_name,pass_word)
        if user is not None:
            login(request,user)
            return render(request, "index.html")
    def get(self,request):
        return render(request, "login.html",{})



# class LoginView(View):
#     def get(self,request):
#         return render(request, "login.html", {})
#     def post(self,request):
#         login_form=LoginForm(request.POST)
#         if login_form.is_valid():
#             user_name = request.POST.get("username", "")
#             pass_word = request.POST.get("password", "")
#             user = authenticate(username=user_name, password=pass_word)
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return render(request, "index.html")
#                 else:
#                     return render(request, "login.html", {"msg": "用户名未激活"})
#             else:
#                 return render(request,"login.html",{"msg":"用户名或密码错误"})
#
#         else:
#             return render(request,"login.html",{"login_form":login_form})