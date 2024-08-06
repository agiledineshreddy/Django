from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import dream112

def dream(request):
    return render(request, 'intro.html')

def register(request):
    if request.method == 'POST':
        phone = request.POST.get('input1')
        passw = request.POST.get('input2')
        
        # Check if the phone number already exists
        if dream112.objects.filter(phone=phone).exists():
            return HttpResponse("Number already exists")  # Or render the register page with an error message
        else:
            user = dream112(phone=phone, passw=passw)
            user.save()
            print('created')
            return redirect('login')
    else:
        return render(request, 'register.html')
def login(request):
    if request.method == 'POST': 
        phone = request.POST.get('input1')
        passw = request.POST.get('input2')
        if phone and passw:
            user_exists = dream112.objects.filter(phone=phone, passw=passw).exists()
            if user_exists:
                request.session['phone'] = phone  # Store phone number in session
                return redirect('bet')  # Redirect to bet page after successful login
            else:
                return HttpResponse("Invalid login credentials")  # No users found
        else:
            return HttpResponse("Both phone and password are required")  # Handle missing data
    else:
        return render(request, 'login.html')

def bet(request):
    if 'phone' in request.session:
        phone = request.session['phone']
        return render(request, 'bet.html', {'ph': phone})
    else:
        return redirect('login')  # Redirect to login if no phone number in session
# views.py
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse

class ProcessPaymentView(View):
    def post(self, request):
        account_number = request.POST.get('account_number')
        routing_number = request.POST.get('routing_number')
        amount = request.POST.get('amount')
        
        # Implement your own payment processing logic here
        if account_number and routing_number and amount:
            # Simulate payment processing
            # In reality, you would integrate with your bank's API here
            return HttpResponse("Payment processing not implemented", status=200)
        else:
            return HttpResponse("Payment failed: Missing information.", status=400)

# urls.py
from django.urls import path
from .views import ProcessPaymentView

urlpatterns = [
    path('payment/', ProcessPaymentView.as_view(), name='process_payment'),
]
