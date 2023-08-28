from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def main_page(request):
   cat = Category.objects.all()

   if request.user.is_authenticated:
           
           user_id = request.user.id

           user = User.objects.get(id=user_id)

           cart_user = Cart.objects.filter(user=user)

           i = 0

           for data in cart_user:
                i+=1
   else:
         i = 0            

   return render(request,'main.html',{'cat':cat,"cart":i})


def view_cat(request,id):
   if request.user.is_authenticated:
           
           user_id = request.user.id

           user = User.objects.get(id=user_id)

           cart_user = Cart.objects.filter(user=user)

           i = 0

           for data in cart_user:
                i+=1
   else:
         i = 0    
   pro = Category.objects.get(id=id)
   pro_c = Products.objects.filter(cat=pro)

   return render(request,'view_page.html',{'pro_c':pro_c,"cart":i})


def Login(request):
      
      if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('pass')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return HttpResponse("Wrong password")
      return render(request,'login.html')

def Register(request):
    return render(request,'register.html')

def Register_user(request):

    name = request.POST.get('name')    
    email = request.POST.get('email')  
    pas = request.POST.get('pass')     
    repass = request.POST.get('repass')

    if pas == repass:

            user = User.objects.filter(username=name)
            isuser = user.exists()
            if isuser is False:
                new_user = User.objects.create_user(username=name,email=email,password=pas)
                new_user.save()

                authuser = authenticate(username=name,password=pas)
                login(request,authuser)
                return redirect('/')
    else:
            return HttpResponse("password Does not match ")  

         

def about(request):
    return render(request,'about.html')


def help(request):
    return render(request,'help.html')


def save_item(request):
    return render(request,'main.html')

def addtoCartPage(request,id):
   if request.user.is_authenticated:
           
           user_id = request.user.id

           user = User.objects.get(id=user_id)

           cart_user = Cart.objects.filter(user=user)

           i = 0

           for data in cart_user:
                i+=1
   else:
         i = 0    

   pro = Products.objects.get(id=id)
   #print(pro)
    
   return render(request,"addtoCartPage.html",{"data":pro,"cart":i})

def addtoCartImp(request):



    if request.user.is_authenticated:
           
           user_id = request.user.id

           user = User.objects.get(id=user_id)

           no = request.POST.get('no') 
           id = request.POST.get('id')

           product = Products.objects.get(id=id)   

           if int(product.stock)-int(no) <= 0:
                return HttpResponse("OUT OF STOCK") 
           
           else:
                 price = int(product.price)*int(no)
                 product.stock = int(product.stock)-int(no)
                 product.save()
            
           cart = Cart(user=user,product=product,no=no,new_price=price)
           cart.save()
           return redirect("/")

    else:
         
         return redirect("/login")  

def viewUsercart(request):
      
   if request.user.is_authenticated:
           
           user_id = request.user.id

           user = User.objects.get(id=user_id)

           cart_user = Cart.objects.filter(user=user)

           i = 0

           for data in cart_user:
                i+=1
   else:
         i = 0          
     
   user_id = request.user.id

   user = User.objects.get(id=user_id)

   cart_user = Cart.objects.filter(user=user)
     

    
   return render(request,"viewUsercart.html",{"pro_c":cart_user,"cart":i})  
    

def deletefromcart(request,id):
     
     user_id = request.user.id

     user = User.objects.get(id=user_id)

     cart_user = Cart.objects.get(id=id,user=user)
     cart_user.delete()

     return redirect("/viewUsercart")


def checkOutPage(request,id):
     
     user_id = request.user.id

     user = User.objects.get(id=user_id)

     cart_user = Cart.objects.get(id=id,user=user)

     return render(request,"checkOutPage.html",{"user":user,"cart":cart_user})

def SuccessPage(request,id):
     user_id = request.user.id

     user = User.objects.get(id=user_id)

     cart_user = Cart.objects.get(id=id,user=user)

     cart_user.delete()
     
     return render(request,"SuccessPage.html")
     




def Logout_(request):
       logout(request)
       return redirect("/")
  