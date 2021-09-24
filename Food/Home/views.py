from django.shortcuts import render
from .models import Product
from .cart import cart
from django.http import HttpResponse
from django import template
from .forms import PostForm,UserProfile
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def index(request):
    products = Product.objects.all
    return render(request, 'index.html', {'products': products})


def buy(request, **kwargs):
    selected = []
    marked = Product.objects.filter(name=kwargs.get('name', "")).first()
    selected.append(marked)
    return render(request, 'payment.html', {'key1': selected})

def makepayment(request):
    return render(request, 'makepayment.html')

def contactus(request):
    return render(request, 'contactus.html')


#def sign_up(request):
 #   return render(request, 'registration.html')



def sign_up(request):
   if request.method == 'POST':
        form = PostForm(request.POST)
        profile_form = UserProfile(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(form.errors, profile_form.errors)
   else:
        form = PostForm()
        profile_form = UserProfile()

   return render(request, 'registration.html', {'form': form, 'profile_form': profile_form, 'registered': registered})


@login_required
def special(request):
    return HttpResponse("YOu are logged in !")


@login_required
def user_logout(request):
    logout(request)
    try:
        del request.session['username']
    except:
        pass
    return HttpResponseRedirect(reverse('home'))


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                request.session['username'] = username
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse("Your account was inactive")
        else:
            print("failed")
            return HttpResponse("Invalid Login details")
    else:
        return render(request, 'login.html', {})





def addtocart(request):
    return render(request, 'addtocart.html')


def add_item(request,**kwargs):
    product=Product.objects.all
    get_item=product.objects.filter(name=kwargs.get('name',"")).first()
    container=cart()
    buck_len=len(container.bucket)
    if container.add_item(get_item):
        mess="item added to cart"
    return render(request,'index.html',{'message':mess,'products':product,'length':buck_len})


def goto_cart(request):
    container=cart()
    return render(request,'addtocart.html',{'buck':container})


def del_item(request,**kwargs):
    container=cart()
    buck_len=len(container.bucket)
    item_name=Product.objects.filter(name=kwargs.get('name',"")).first()
    if container.del_item(item_name.name):
        mess="item is removed"
    return render(request,'addtocart.html',{'message':mess,'buck':container})


def placed_order(request):
    return HttpResponse("<h1 style='background:lightgreen'>Thanks for placing order  </h1>")
