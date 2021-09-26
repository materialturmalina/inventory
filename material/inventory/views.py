from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Item, PISOS
from django.contrib.auth.models import User


#from django.db.models import CharField
#from django.db.models.functions import Lower
#CharField.register_lookup(Lower)


def home(request):
	return render(request, 'inventory/home.html')

def info(request):
	return render(request, 'inventory/info.html')

class ItemListView(ListView):
	model = Item
	template_name = 'inventory/home.html'
	context_object_name = 'items'
	#ordering = ['item_name', 'box', '-date_posted']
	paginate_by = 5

	def get_queryset(self):
		filter_val = self.request.GET.get('filter', '')
		order = self.request.GET.get('orderby', 'item_name')
		if filter_val:
			#new_context = Item.objects.filter(item_name__unaccent__lower__trigram_similar=filter_val, ).order_by(order)
			new_context = Item.objects.filter(item_name__icontains=filter_val, ).order_by(order)
		else:
			new_context = Item.objects.order_by(order)
		return new_context

	def get_context_data(self, **kwargs):
		context = super(ItemListView, self).get_context_data(**kwargs)
		context['filter'] = self.request.GET.get('filter', '')
		context['orderby'] = self.request.GET.get('orderby', 'item_name')
		return context

class PisoItemListView(ListView):
	model = Item
	template_name = 'inventory/piso_items.html'
	context_object_name = 'items'
	paginate_by = 5

	def get_queryset(self):
		this_piso = self.kwargs.get('piso')

		this_piso_name = [ piso_name[0] for piso_name in PISOS if piso_name[1] == this_piso ]#to get ['Turmalina'] from "TU"
		this_piso_name = this_piso_name[0]#to get "Turmalina" from ['Turmalina']

		new_context = Item.objects.filter(piso=this_piso_name)
		filter_val = self.request.GET.get('filter', '')
		order = self.request.GET.get('orderby', 'item_name')
		if filter_val:
			new_context = new_context.filter(item_name__icontains=filter_val, ).order_by(order)
		else:
			new_context = new_context.order_by(order)
		return new_context

	def get_context_data(self, **kwargs):
		context = super(PisoItemListView, self).get_context_data(**kwargs)
		context['filter'] = self.request.GET.get('filter', '')
		context['orderby'] = self.request.GET.get('orderby', 'item_name')
		return context

class UserItemListView(ListView):
	model = Item
	template_name = 'inventory/user_items.html'
	context_object_name = 'items'
	paginate_by = 5

#	def get_queryset(self):
#		user = get_object_or_404(User, username=self.kwargs.get('username'))
#		return Item.objects.filter(author=user).order_by('item_name', 'box', '-date_posted')

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		new_context = Item.objects.filter(author=user)
		filter_val = self.request.GET.get('filter', '')
		order = self.request.GET.get('orderby', 'item_name')
		if filter_val:
			new_context = new_context.filter(item_name__icontains=filter_val, ).order_by(order)
		else:
			new_context = new_context.order_by(order)
		return new_context

	def get_context_data(self, **kwargs):
		context = super(UserItemListView, self).get_context_data(**kwargs)
		context['filter'] = self.request.GET.get('filter', '')
		context['orderby'] = self.request.GET.get('orderby', 'item_name')
		return context

class BoxListView(ListView):
	model = Item
	template_name = 'inventory/box_view.html'
	context_object_name = 'items'
	ordering = ['box']
	#paginate_by = 5

	def get_queryset(self):
		this_piso_name = [ piso_name[0] for piso_name in PISOS if piso_name[1] == self.request.GET.get('selected_piso', 'TU') ]#to get ['Turmalina'] from "TU"
		this_piso_name = this_piso_name[0]#to get "Turmalina" from ['Turmalina']
		new_context = Item.objects.filter(piso=this_piso_name)
		return new_context

	def get_context_data(self, **kwargs):
		context = super(BoxListView, self).get_context_data(**kwargs)
		context['selected_piso'] = self.request.GET.get('selected_piso', 'TU')
		return context

class ItemDetailView(DetailView):
	model = Item

class BoxDetailView(ListView):
	model = Item
	context_object_name = 'items'
	ordering = ['item_name']
	template_name = 'inventory/box_detail_view.html'

	def get_queryset(self):
		self.this_piso_name = [ piso_name[0] for piso_name in PISOS if piso_name[1] == self.kwargs.get('piso') ]#to get ['Turmalina'] from "TU"
		self.this_piso_name = self.this_piso_name[0]#to get "Turmalina" from ['Turmalina']
		new_context = Item.objects.filter(piso=self.this_piso_name)
		return new_context


class ItemCreateView(LoginRequiredMixin, CreateView):
	model = Item
	fields = ['item_name', 'piso', 'box',]

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class ItemUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Item
	fields = ['item_name', 'piso', 'box']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		item = self.get_object()
		if self.request.user == item.author:
			return True
		else:
			return False

class ItemDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Item
	success_url = '/home/'

	def test_func(self):
		item = self.get_object()
		if self.request.user == item.author:
			return True
		else:
			return False

def pisos(request):
    context= {
    	'pisos_list':PISOS
    }
    return render(request, 'inventory/pisos_view.html', context)
