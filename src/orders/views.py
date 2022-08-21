from django.http import HttpResponseRedirect
from django.views import generic
from . forms import BookInCartAddForm, CartAddForm, OrderAddForm
from . models import BookInCart, Cart, Order
from book.models import Book
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin

# Create your views here.

def get_cart(view):
    card_id = view.request.session.get('cart')
    if not card_id:
        if view.request.user.is_anonymous:
            customer = None
        else:
            customer = view.request.user
        cart = Cart.objects.create(
            customer=customer
        )
        view.request.session['cart'] = cart.pk
    else:
        cart = Cart.objects.get(pk=card_id)
    return cart

class DeleteFromCart(generic.DeleteView):
    template_name = "orders/delete-item.html"
    model = BookInCart
    success_url = reverse_lazy("orders:add-to-cart")

class UpdateCart(generic.UpdateView):
    template_name = "orders/cart.html"
    model = BookInCart
    form_class = BookInCartAddForm
    success_url = reverse_lazy("orders:add-to-cart")
        
    def get_object(self, **kwargs):
        cart = get_cart(self)
        for good in self.request.POST.keys():
            if good[:5] == "good_":
                good_in_cart_pk = good.split("_")[1]
                book_in_cart = BookInCart.objects.get(pk=int(good_in_cart_pk))
                book_in_cart.quantity = int(self.request.POST.get(good))
                book_in_cart.price = book_in_cart.book.price * book_in_cart.quantity
                book_in_cart.save()
        action_type = self.request.POST.get('action_type')
        if action_type == 'Order':
            order = Order.objects.create(
            cart = book_in_cart.cart,
            name = self.request.POST.get('name'),
            email = self.request.POST.get('email'),
            phone = self.request.POST.get('phone'),
            address = self.request.POST.get('address'),
            comment = self.request.POST.get('comment')
            )
            del self.request.session["cart"]
        return cart
    
    def render_to_response(self, context, **response_kwargs):
        action_type = self.request.POST.get('action_type')
        if action_type == 'Order':
            return HttpResponseRedirect("/")
        return super().render_to_response(context, **response_kwargs)

 
class AddToCart(generic.UpdateView):
    model = Cart
    form_class = CartAddForm
    template_name = "orders/cart.html"
    success_url = reverse_lazy("orders:add-to-cart")
    def get_object(self, **kwargs):
        book_id = self.request.POST.get('book_id')
        cart = get_cart(self)
        if book_id:
            quantity = int(self.request.POST.get('quantity'))
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
        return cart

class OrderList(PermissionRequiredMixin, generic.ListView):
    template_name = "orders/order_list.html"
    model = Order
    paginate_by = 20
    permission_required = ('orders.view_order')
    login_url = "user_app:login"
    
class OrderView(PermissionRequiredMixin, generic.DetailView):
    template_name = "orders/order_view.html"
    model = Order
    permission_required = ('orders.view_order')
    login_url = "user_app:login"

class OrderEdit(PermissionRequiredMixin, generic.UpdateView):
    template_name = "orders/order_edit.html"
    model = Order
    form_class = OrderAddForm
    permission_required = ('orders.change_order')
    login_url = "user_app:login"
    success_url = reverse_lazy("orders:order-list")

class OrderDelete(PermissionRequiredMixin, generic.DeleteView):
    template_name = "orders/order_delete.html"
    model = Order
    success_url = reverse_lazy("orders:order-list")
    permission_required = ('orders.delete_order')
    login_url = "user_app:login"
    

 
