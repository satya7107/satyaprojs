from django.shortcuts import render,  redirect
from django.http import HttpResponse
from mysite.models import product
from .models import Cart,CartItem
# Create your views here.
def _cart_id(request):
    cart=request.session.session_key
    if not cart:
        cart=request.session.create()
    return cart


def add_cart(request, product_id):
    prodobj=product.objects.get(id=product_id)
    try:
        cart=Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart=Cart.objects.create(
            cart_id=_cart_id(request)
        )
    cart.save()
    try:
        cart_item=CartItem.objects.get(product=prodobj,cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item=CartItem.objects.create(
            product=prodobj,
            cart=cart,
            quantity=1
        )
        cart_item.save()
    # return HttpResponse(cart_item.product) 
    # exit()
    return redirect('cart')
def remove_cart(request,product_id):
    cart=Cart.objects.get(cart_id=_cart_id(request))
    prodobj=product.objects.get(id=product_id)
    cart_item=CartItem.objects.get(product=prodobj,cart=cart)
    if cart_item.quantity>1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')
def remove_cart_item(request, product_id):
    cart=Cart.objects.get(cart_id=_cart_id(request))
    prodobj=product.objects.get(id=product_id)
    cart_item=CartItem.objects.get(product_id=prodobj,cart=cart)
    cart_item.delete()
    return redirect('cart')        



def cart(request, total=0, quantity=0, cart_items=None):
    try:
        cart=Cart.objects.get(cart_id=_cart_id(request))
        cart_items=CartItem.objects.filter(cart=cart,is_active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price*cart_item.quantity)
            quantity += cart_item.quantity
        tax= int(total- ((total*100)/105) ) 
        ptotal=total-tax
        grandtotal=int(ptotal+tax)  
    except ObjectNotExist:
        pass

    context ={
        "total":total,
        "ptotal":ptotal,
        "quantity":quantity,
        "cart_items":cart_items,
        "tax":tax,
        "grandtotal":grandtotal,
                }      

    return render(request, 'store/cart.html', context)

