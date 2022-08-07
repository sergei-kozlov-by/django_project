from django.shortcuts import render
from django.views import generic
from . models import BookInCart, Cart
from . forms import CartAddForm
from book.models import Book
from django.urls import reverse_lazy

# Create your views here.

class AddToCart(generic.TemplateView):
    template_name = "orders/cart.html"
    def get_context_data(self, **kwargs):
        print(self.request.session.items())
        card_id = self.request.session.get("cart")
        book_id = self.request.GET.get('book_id')
        quantity = int(self.request.GET.get('quantity'))
        if not card_id:
            if self.request.user.is_anonymous:
                customer = None
            else:
                customer = self.request.user
            cart = Cart.objects.create(
                customer=customer
            )
            self.request.session["cart"] = cart.pk
        else:
            cart = Cart.objects.get(pk=card_id)  
            book =  Book.objects.get(pk=book_id)
            price = book.price * quantity
            book_in_cart, created = BookInCart.objects.get_or_create(
                cart=cart,
                book=book,
                defaults={
                    'quantity': quantity,
                    'price': price
                }
            )
            if not created:
                book_in_cart.quantity = book_in_cart.quantity + quantity
                book_in_cart.price = book_in_cart.price + price
                book_in_cart.save()
        context = super().get_context_data(**kwargs)
        return context

 
