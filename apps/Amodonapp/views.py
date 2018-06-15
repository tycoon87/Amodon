from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

def index (request):
    return render (request, 'Amodonapp/index.html')

def checkout(request):
    return render(request,'Amodonapp/checkout.html')

def purchese(request):
    if 'cart' not in request.session:
        request.session['cart'] = 0
        request.session['price'] = 0
    if request.POST['id'] == '001':
        request.session['cart'] += int(request.POST['quantity'])
        Total = 19.99 * int(request.POST['quantity'])
        request.session['price'] += Total
        request.session['charge'] = Total
        request.session['item'] = 'Dojo Tshirt'
    if request.POST['id'] == '002':
        request.session['cart'] += int(request.POST['quantity'])
        Total = 49.99 * int(request.POST['quantity'])
        request.session['price'] += Total
        request.session['charge'] = Total
        request.session['item'] = 'Algorithm Book'
    if request.POST['id'] == '003':
        request.session['cart'] += int(request.POST['quantity'])
        Total = 49.99 * int(request.POST['quantity'])
        request.session['price'] += Total
        request.session['charge'] = Total
        request.session['item'] = 'Dojo Sweater'
    if request.POST['id'] == '004':
        request.session['cart'] += int(request.POST['quantity'])
        Total = 49.99 * int(request.POST['quantity'])
        request.session['price'] += Total
        request.session['charge'] = Total
        request.session['item'] = 'Dojo Cup'
    return redirect('/checkout')

def clear (request):
    request.session.clear()
    return redirect('/')