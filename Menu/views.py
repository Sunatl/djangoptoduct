# views.py
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView,TemplateView
from .models import Order, Customer, Product
from .forms import OrderForm, CustomerForm, ProductForm


class Base(TemplateView):
    template_name = "base.html"


# Views барои Order

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

class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'o_delete.html'
    success_url = reverse_lazy('order-list')

class OrderDetailView(DetailView):
    model = Order
    template_name = 'o_detail.html'
    context_object_name = "object"

# Views барои Customer
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

class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'c_delete.html'
    success_url = reverse_lazy('c_list')

class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'c_detail.html'
    context_object_name = "object"

# Views барои Product
class ProductListView(ListView):
    model = Product
    template_name = 'p_list.html'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'p_cr.html'
    success_url = reverse_lazy('p_list')

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'p_up.html'
    success_url = reverse_lazy('p_list')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'p_delete.html'
    success_url = reverse_lazy('p_list')

class ProductDetailView(DetailView):
    model = Product
    
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["vakansi"] = Order.objects.filter(product = self.kwargs['pk'])
        return context
    template_name = 'p_detail.html'
    context_object_name = "object"