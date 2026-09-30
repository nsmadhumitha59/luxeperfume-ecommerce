from django.shortcuts import render, get_object_or_404, redirect
from .models import Product


def products(request):

    products = Product.objects.all()

    for product in products:
        product.display_image = get_product_image(
            product.name
        )

    return render(
        request,
        'shop/products.html',
        {
            'products': products
        }
    )




# =====================================================
# PRODUCT IMAGE MAPPING
# =====================================================

def get_product_image(product_name):

    images = {

        "Rose Elegance":
            "https://images.unsplash.com/photo-1547887538-e3a2f32cb1cc?auto=format&fit=crop&w=700&q=90",

        "Midnight Oud":
            "https://images.unsplash.com/photo-1612817288484-6f916006741a?auto=format&fit=crop&w=700&q=90",

        "Citrus Bloom":
            "https://images.unsplash.com/photo-1523293182086-7651a899d37f?auto=format&fit=crop&w=700&q=90",

        "Velvet Vanilla":
            "https://images.unsplash.com/photo-1594035910387-fea47794261f?auto=format&fit=crop&w=700&q=90",

        "Ocean Mist":
            "https://images.unsplash.com/photo-1588405748880-12d1d2a59f75?auto=format&fit=crop&w=700&q=90",

        "Jasmine Dream":
            "https://images.unsplash.com/photo-1592945403244-b3fbafd7f539?auto=format&fit=crop&w=700&q=90",

        "Royal Sandal":
            "https://images.unsplash.com/photo-1595425970377-c9703cf48b6d?auto=format&fit=crop&w=700&q=90",

        "Amber Glow":
            "https://images.unsplash.com/photo-1563170351-be82bc888aa4?auto=format&fit=crop&w=700&q=90",

        "Lavender Bliss":
            "https://images.unsplash.com/photo-1541643600914-78b084683601?auto=format&fit=crop&w=700&q=90",

        "Golden Citrus":
            "https://images.unsplash.com/photo-1557170334-a9632e77c6e4?auto=format&fit=crop&w=700&q=90",
    }

    return images.get(
        product_name,
        images["Rose Elegance"]
    )


# =====================================================
# HOME
# =====================================================

def home(request):

    products = Product.objects.all()

    for product in products:
        product.display_image = get_product_image(product.name)

    return render(
        request,
        'shop/home.html',
        {
            'products': products
        }
    )


# =====================================================
# SHOP
# =====================================================

def products(request):

    products = Product.objects.all()

    # Add correct image to every product
    for product in products:
        product.display_image = get_product_image(product.name)

    return render(
        request,
        'shop/products.html',
        {
            'products': products
        }
    )


# =====================================================
# PRODUCT DETAIL
# =====================================================

def product_detail(request, product_id):

    product = get_object_or_404(
        Product,
        id=product_id
    )

    image = get_product_image(product.name)

    return render(
        request,
        'shop/product_detail.html',
        {
            'product': product,
            'image': image
        }
    )


# =====================================================
# ADD TO CART
# =====================================================

def add_to_cart(request, product_id):

    product = get_object_or_404(
        Product,
        id=product_id
    )

    cart = request.session.get(
        'cart',
        {}
    )

    product_id = str(product_id)

    if product_id in cart:
        cart[product_id] += 1
    else:
        cart[product_id] = 1

    request.session['cart'] = cart

    request.session.modified = True

    return redirect('cart')


# =====================================================
# CART
# =====================================================

def cart(request):

    cart = request.session.get(
        'cart',
        {}
    )

    cart_items = []

    total = 0

    for product_id, quantity in cart.items():

        product = get_object_or_404(
            Product,
            id=product_id
        )

        subtotal = product.price * quantity

        total += subtotal

        cart_items.append({

            'product': product,

            'quantity': quantity,

            'subtotal': subtotal,

            'image':
                get_product_image(product.name),
        })

    return render(
        request,
        'shop/cart.html',
        {
            'cart_items': cart_items,
            'total': total
        }
    )


# =====================================================
# REMOVE FROM CART
# =====================================================

def remove_from_cart(request, product_id):

    cart = request.session.get(
        'cart',
        {}
    )

    product_id = str(product_id)

    if product_id in cart:
        del cart[product_id]

    request.session['cart'] = cart

    request.session.modified = True

    return redirect('cart')


# =====================================================
# CHECKOUT
# =====================================================

def checkout(request):

    return render(
        request,
        'shop/checkout.html'
    )


# =====================================================
# ABOUT
# =====================================================

def about(request):

    return render(
        request,
        'shop/about.html'
    )


# =====================================================
# CONTACT
# =====================================================

def contact(request):

    return render(
        request,
        'shop/contact.html'
    )


# =====================================================
# LOGIN
# =====================================================

def login_view(request):

    return render(
        request,
        'shop/login.html'
    )


# =====================================================
# REGISTER
# =====================================================

def register(request):

    return render(
        request,
        'shop/register.html'
    )