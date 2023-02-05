from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .models import Product, Customer
from .forms import ProductForm, CustomerForm, Product_listForm

def index(request):
    if not request.user.is_authenticated:
        error = ""
        if request.method == 'POST':
            u = request.POST['username']
            p = request.POST['password']
            user = authenticate(username = u, password = p)

            try:
                if user.is_staff:
                    login(request, user)
                    error = "no"
                    return render(request, 'dashboard.html', locals())
                else:
                    error = "yes"
            except Exception:
                error = 'yes'
        return render(request, 'index.html', locals())
    else:
        return redirect('dashboard')


def user_logout(request):
    logout(request)
    return redirect(index)


def dashboard(request):
    if not request.user.is_authenticated:
        return redirect(index)

    if request.method == "POST":
        form = ProductForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            form = ProductForm()
    else:
        form = ProductForm()
    product = Product.objects.all()
    return render(request, 'dashboard.html', locals())


def forget_password(request):
    if not request.user.is_authenticated:
        return redirect(index)
    error = ""
    user = request.user
    if request.method == "POST":
        old = request.POST['password1']
        new = request.POST['password2']
        try:
            u = User.objects.get(id=request.user.id)
            if user.check_password(old):
                u.set_password(new)
                u.save()
                error = 'no'
            else:
                error = 'yes'
        except:
            error = 'yes'
    return render(request, 'forget_password.html', locals())


def bill(request):
    # product = Product.objects.all()
    return render(request, 'bill.html', locals())
    