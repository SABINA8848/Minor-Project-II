from django.contrib.auth import logout
from django.shortcuts import render , redirect , HttpResponse
from .models import logins  




# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def dress(request):
    return render(request, 'dress.html')

def skirts(request):
    return render(request, 'skirts.html')

def pants(request):
    return render(request, 'pants.html')

def fav(request):
    return render(request, 'fav.html')

def cart(request):
    return render(request, 'cart.html')

def account(request):
    return render(request, 'account.html')

def collection(request):
    return render(request, 'collection.html')

def product(request):
    return render(request, 'product.html')

def winter(request):
    return render(request, 'winter.html')

def collection_pants(request):
    return render(request, 'collection_pants.html')

def collection_shirts(request):
    return render(request, 'collection_shirts.html')
def finalpayment(request):
    return render(request, 'finalpayment.html')
def success(request):
    return render(request, 'success.html')


    
def login(request):
        if request.method == 'POST':
            if 'signup' in request.POST:
                    obj = logins()
                    obj.name = request.POST.get('name')
                    obj.password = request.POST.get('password')
                    obj.email = request.POST.get('email')

                    obj.save()
                    print("Saved Successfully")
                    return redirect('login')
            elif 'login' in request.POST:
            # Handle login form submission
                x = request.POST.get('lemail')
                y = request.POST.get('lpassword')
                try:
                    z = logins.objects.get(email=x)
                    if y == z.password:
                        return redirect('finalpayment')
                    else:
                        return HttpResponse("Invalid Password")
                except logins.DoesNotExist:
                    return HttpResponse("User does not exist")
    

        return render(request, "login.html")



  







