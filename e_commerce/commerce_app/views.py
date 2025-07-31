from django.shortcuts import render, get_object_or_404, redirect
from commerce_app.models import *
from django.contrib import messages

# Create your views here.
def homepage(request):# anasayfa
    return render(request, "commerce_app/homepage.html")

def log_in(request):#giriş yap kısmı
    if request.method == "POST":
        e_mail = request.POST.get("e_mail")
        password = request.POST.get("password")
        
        try:
            user = Users.objects.get(e_mail = e_mail, password = password)
            request.session["user_id"] = user.id #Kullanıcı id'sini oturumda saklıyoruz.
            messages.success(request , f"Başarıyla Giriş yaptınız {user.username}")
            return redirect('commerce_app:homepage') # Giriş başarılıysa anasayfaya yönlendiriyoruz.        
        except Users.DoesNotExist:
            messages.error(request, "Kullanıcı adı veya şifre yanlış")
            return render(request, "comemrce_app/log_in.html")
    return render(request, "commerce_app/log_in.html")
    return render(request, "commerce_app/log_in.html")

def register(request):# kaydol kısmı
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        e_mail = request.POST.get("e_mail")
        surname = request.POST.get("surname")
        
        if username and password and e_mail and surname :
            Users.objects.create(
                username = username,
                password = password,
                e_mail = e_mail,
                surname = surname
            )
        return render (request, "commerce_app/log_in.html")
    return render(request, "commerce_app/register.html")
def categories(request): # kategoriler kısmı
    return render(request, "commerce_app/categories.html")

def products(request): # ürünler kısmı
    product = Product.objects.all()# tüm ürünleri aldık.
    return render(request, "commerce_app/product.html", {"products": product})

def product_view(request, product_id): # ürün detayları kısmı
    product = get_object_or_404(Product,id= product_id)# ürün id'sine göre ürünü aldık.
    return render(request, "commerce_app/product_view.html",{"product": product})

def add_to_cart(request, product_id): #sepete ekleme işlemi
    product = get_object_or_404(Product, id = product_id) # ürün idsine göre ürünü aldık.
    return render(request, "commerce_app/add_to_cart.html", {"product": product})

def cart(request, product_id=None): 
    cart = request.session.get("cart", {}) 
    
    if request.method == "POST" and product_id:
        quantity = int(request.POST.get("quantity", 1))
        cart[str(product_id)] = cart.get(str(product_id), 0) + quantity
        request.session["cart"] = cart
    
    cart_items = []
    total_price = 0
    for pid, qty in cart.items():
        product = get_object_or_404(Product, pk=pid)
        item_total = product.product_price * qty
        total_price += item_total
        cart_items.append({
            "product": product,
            "quantity": qty,
            "total_price": item_total
        })
        
    return render(request, "commerce_app/cart.html", {
        "cart_items": cart_items,
        "total_price": total_price
    })

def remove_product(request, product_id):
    cart = request.session.get("cart", {})
    if str(product_id) in cart:
        cart.pop(str(product_id))
    request.session["cart"] = cart
    return redirect('commerce_app:cart_home')

def increase_qty(request, product_id):
    cart = request.session.get("cart", {})
    if str(product_id) in cart:
        cart[str(product_id)] += 1
    request.session["cart"] = cart
    return redirect('commerce_app:cart_home')

def decrease_qty(request, product_id):
    cart = request.session.get("cart", {})
    if str(product_id) in cart:
        cart[str(product_id)] -= 1
        if cart[str(product_id)] <= 0:
            cart.pop(str(product_id))
    request.session["cart"] = cart
    return redirect('commerce_app:cart_home')

