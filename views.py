from django.shortcuts import render,redirect
from django.contrib.auth.models import auth
from django.contrib.auth.hashers import make_password
from django.contrib.auth.base_user import BaseUserManager
from django.contrib import messages
from . models import Users,Plan,Plantype
from django.core.mail import send_mail
import datetime
from datetime import date,timedelta 
import calendar
# Create your views here.




def signup(request):
    return render(request,'signup.html')



def register(request):
    
    if request.method == 'POST':
        name= request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        city = request.POST['city']
        address = request.POST['address']
        pincode = request.POST['pincode']

        password = BaseUserManager().make_random_password()

        if(Users.objects.filter(email = email).exists()):
            messages.info(request,'email taken')
            return redirect('/signup')
        
        elif(Users.objects.filter(mobile = mobile).exists()):
            messages.info(request,'mobile taken')
            return redirect('/signup')
        
        else:
            user=Users.objects.create(name=name, email=email, mobile=mobile, city=city, address=address, pincode=pincode,password=password)
            
            #print('rrrrrrr',email,password) 
            send_mail(
                    'Register success mail',
                    'Your signup successfully, now you password is : '+ password,
                    'talhahamid.syed@gmail.com',
                    [email],     
                    fail_silently=False,
                )
            a=send_mail()
            print('rrrrrr')
            print('rrrrrr',a)
            user.save()
             
            return redirect('login')
        return redirect('/')
    else:
        return render(request,'signup.html')
       



def checkLogin(request):
    if request.method == 'POST':
        mobile = request.POST['mobile']
        password = request.POST['pass']
        user = Users.objects.get(mobile=mobile)
        if Users.objects.filter(mobile = mobile).exists():           
            if Users.objects.filter(password = password).exists():    
                try:
                    request.session['uid']=user.id
                    #sid=request.session['uid']
                                        
                except Users.DoesNotExist:
                    return render('login')

                data=Users.objects.get(id=request.session.get('uid'))
                return render(request, 'home.html',{'data':data})
        else:
            messages.info(request, 'invalid credentials')
            #print("hiiiiii")
            return redirect('login')

    else:    
        return render(request,'login.html')


def home(request):
    data = Users.objects.get(id=request.session.get('uid'))  
    plan = Plan.objects.filter(uid=request.session.get('uid'))
    
    currentdate = datetime.datetime.now()
    currentdate=currentdate.date()
    #currentdate = str(currentdate)
    enddate=[]
    for plan in plan:
        #print("end date ",plan.end_date)
        enddate.append(plan.end_date)  

    enddate.sort()
    bigdate=enddate[-1]
    remainingdate = bigdate - timedelta(days=15)
    
 
    remainingdays= (remainingdate-currentdate) 
    remainingdays = str(remainingdays)
    r=remainingdays[0:3]
     
    r=int(r)
    if(r<=15):
        print("Your remaining days are",r) 
        data = Users.objects.get(id=request.session.get('uid'))
        plan = Plan.objects.filter(uid=request.session.get('uid'))
        return render(request, 'home.html', {'r':r, 'plan':plan, 'data':data})
    else:
        data = Users.objects.get(id=request.session.get('uid'))
        plan = Plan.objects.filter(uid=request.session.get('uid'))
        return render(request, 'home.html', { 'plan':plan, 'data':data})



def profile(request): 
    pro = Users.objects.get(id=request.session.get('uid')) 
    return render(request, 'profile.html',{'pro':pro})  


def logout(request):
    try:
        del request.session['uid']
    except:
        return render(request, 'login.html')
    return render(request, 'login.html')    


def oclist(request):
    return render(request,'optionchangelist.html')


def forget(request):
    if request.method == 'POST':
        email=request.POST['email']
        
        if Users.objects.filter(email=email).exists():
            print('eeeeeeexits') 
            '''send_mail(
                    'PASSWORD',
                    'YOU CAN CHANGE YOUR PASSWORD.',
                    'aleembca007@gmail.com',
                    ['talhahamid.syed@gmail.com'],
                    fail_silently=False,
                )'''
            return render(request, 'login.html')
        else:
            print("doesnt eeeeeeexits")
            return render(request, 'forget.html')            
    return render(request, 'forget.html')                           

def plan(request): 
    plan = Plantype.objects.all()
    return render(request, 'plan.html', {'plan':plan})    



def planstore(request):
    if request.method == "POST":
        plan_name = request.POST['plan_name']
        price = request.POST['price'] 
        uid =   request.session.get('uid')
        
        
        #print("qqqqqqqqq",price,plan_name)
        current_time = datetime.datetime.now()
            
        if plan_name=="Standard":
            end_date = current_time + timedelta(days=30)   
                                     

        if plan_name=="Silver": 
            end_date = current_time + timedelta(days=90)
        
        if plan_name=="Gold":
            end_date = current_time + timedelta(days=180)

        add=Plan(uid=uid, price=price, plan_name=plan_name, start_date=current_time, end_date=end_date, status='1')  
        add.save()
    
        messages.info(request, 'Your \' '+ plan_name + ' Plan \' is successfully activated.')
        return redirect(plan)


def sidepanel(request):
    data = Users.objects.get(id=request.session.get('uid'))
    plan = Plan.objects.filter(uid=request.session.get('uid'))
    return render(request, 'sidepanel.html',{'data':data})