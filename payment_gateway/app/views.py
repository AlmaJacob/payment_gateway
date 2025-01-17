from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from django.conf import settings
import razorpay
import json 
from django.views.decoraters.csrf import csrf_exempt

# Create your views here.
def home(request):
    return render(request,"index.html")

def order_payment(request):
    if request.method == "POST":
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID,settings.RAZORPAY_KEY_SECRET))
        razorpay_order = client.order.create(
            {"amount": int(amount) *100, }
        )