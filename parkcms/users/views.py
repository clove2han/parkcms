from django.shortcuts import render,redirect,HttpResponse
from users import models
from django.template.context_processors import request
from _overlapped import NULL
# Create your views here.
# @check_login   
def index(request):

    user_list = models.UserInfo.objects.filter()
    return render(request, 'index.html', {"data":user_list})

def login(request):
    # 如果是POST请求，则说明是点击登录按扭 FORM表单跳转到此的，那么就要验证密码，并进行保存session
    if request.method == 'POST':
        username = request.POST.get("username",None)
        password = request.POST.get("password",None)
        user = models.UserInfo.objects.filter(uname = username,pwd = password)
        
        print(user)
        if user:
             #登录成功
            # 1，生成特殊字符串
            # 2，这个字符串当成key，此key在数据库的session表（在数据库存中一个表名是session的表）中对应一个value
            # 3，在响应中,用cookies保存这个key ,(即向浏览器写一个cookie,此cookies的值即是这个key特殊字符）
            request.session['is_login']='1'  # 这个session是用于后面访问每个页面（即调用每个视图函数时要用到，即判断是否已经登录，用此判断）
            
            # request.session['username']=username  # 这个要存储的session是用于后面，每个页面上要显示出来，登录状态的用户名用。
            # 说明：如果需要在页面上显示出来的用户信息太多（有时还有积分，姓名，年龄等信息），所以我们可以只用session保存user_id
            request.session['user_id']=user[0].id
            return redirect('/index/')
    
    # 如果是GET请求，就说明是用户刚开始登录，使用URL直接进入登录页面的
    return render(request,'login.html')


def userinfo(request):
    user_list = models.UserInfo.objects.filter()
    print(user_list)
    for user in user_list:
        print(user.user)
        print(user.pwd)
    return render(request, 'userinfo.html', {"user_list":user_list})


def adduser_html(request):
    return render(request, 'adduser.html')

def adduser(request):
    if request.method == 'POST':
        username = request.POST.get("username",None)
        password = request.POST.get("password",None)
        print(type(username))
        print(password)
        if username !='' and password != '':
            models.UserInfo.objects.create(user = username , pwd = password)
            print("11111111111111111111111")
            return redirect('/adduser_html/')
        else:
            print("2222222222222222222222")
            return render(request, 'adduser.html', {"msg":"用户名或密码不能为空"})