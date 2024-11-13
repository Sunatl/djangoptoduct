# views.py
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView,TemplateView
from .models import Order, Customer, Product
from .forms import OrderForm, CustomerForm, ProductForm

from django.contrib.auth import logout
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

@login_required
def user_logout(request):
    logout(request) 
    return render(request, 'registration/log_out.html') 

def login(request):
    return redirect("accounts/login/")


class Base(TemplateView):
    template_name = "base.html"


# Order

class OrderListView(ListView):
    model = Order
    template_name = 'o_list.html'



class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'o_cr.html'
    success_url = reverse_lazy('o_list')

class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'o_up.html'
    success_url = reverse_lazy('o_list')
    
    def get_queryset(self):
        return Order.objects.filter(user = self.request.user)

class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'o_delete.html'
    success_url = reverse_lazy('order-list')
    
    def get_queryset(self):
        return Order.objects.filter(user = self.request.user)

class OrderDetailView(DetailView):
    model = Order
    template_name = 'o_detail.html'
    context_object_name = "object"

# Customer
class CustomerListView(ListView):
    model = Customer
    template_name = 'c_list.html'

class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'c_cr.html'
    success_url = reverse_lazy('c_list')


class CustomerUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'c_up.html'
    success_url = reverse_lazy('c_list')
    def get_queryset(self):
        return Customer.objects.filter(user = self.request.user)

class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'c_delete.html'
    success_url = reverse_lazy('c_list')
    
    def get_queryset(self):
        return Customer.objects.filter(user = self.request.user)

class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'c_detail.html'
    context_object_name = "object"

# Product
class ProductListView(ListView):
    model = Product
    template_name = 'p_list.html'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'p_cr.html'
    success_url = reverse_lazy('p_list')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'p_up.html'
    success_url = reverse_lazy('p_list')
    
    def get_queryset(self):
        return Product.objects.filter(user = self.request.user)

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'p_delete.html'
    success_url = reverse_lazy('p_list')
    def get_queryset(self):
        return Product.objects.filter(user = self.request.user)

class ProductDetailView(DetailView):
    model = Product
    
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["vakansi"] = Order.objects.filter(product = self.kwargs['pk'])
        return context
    template_name = 'p_detail.html'
    context_object_name = "object"