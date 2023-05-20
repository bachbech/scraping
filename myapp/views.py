from django.views.generic import ListView
from .models import MyModel , House
from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.paginator import Paginator
import json
"""class HomePageView(TemplateView):
     template_name="my_model_list.html"
@staticmethod
def your_view(request): 
        print("Your view function called")
        data = House.objects.all()
        
        paginator = Paginator(data, 10)  # Specify the number of items per page

        page_number = request.GET.get('page')  # Get the current page number from the request
        page_obj = paginator.get_page(page_number)  # Get the Page object for the current page

        return render(request, 'my_model_list.html', {'page_obj': page_obj})
        #return render(request, 'my_model_list.html', {'data': data})"""
from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.paginator import Paginator
from .models import House
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.db.models.functions import Substr, Length
class HomePageView(TemplateView):
    template_name = "my_model_list.html"


def your_view(request):
    location = request.GET.get('location')
    ville = request.GET.get('ville')
    chambre = request.GET.get('chambre')
    min_price = request.GET.get('min-price')
    max_price = request.GET.get('max-price')
    sort_by = request.GET.get('sort_by')
    contact = request.GET.get('contact')
  
    houses = House.objects.all()
    if location:
        houses = houses.filter(location__contains=f", {location}")
    if ville:
        houses = houses.filter(location__contains=f"{ville},")
    if chambre:
        houses = houses.filter(chambre=chambre)
    if min_price and max_price:
        houses = houses.filter(price__gte=min_price, price__lte=max_price)



    if sort_by == 'asc_price':
        houses = houses.order_by('price')
    elif sort_by == 'desc_price':
        houses = houses.order_by('-price')
    elif sort_by == 'recent':
        houses = houses.order_by('-date_added')
    elif sort_by == 'least_recent':
        houses = houses.order_by('date_added')

    paginator = Paginator(houses, 10)  
    page_number = request.GET.get('page')  
    page_obj = paginator.get_page(page_number)  

    

    context = {
        'page_obj': page_obj,
        'location': location,
        'ville': ville,
        'chambre': chambre,
        'min_price': min_price,
        'max_price': max_price,
        'sort_by': sort_by,
    }
    return render(request, 'my_model_list.html', context)
"""@login_required
def add_to_bookmarks(request, house_id):
    house = House.objects.get(id=house_id)
    bookmark, created = Bookmark.objects.get_or_create(user=request.user)
    bookmark.houses.add(house)
    return redirect('bookmarks')
@login_required
def bookmarks(request):
    bookmark = Bookmark.objects.get(user=request.user)
    houses = bookmark.houses.all()
    return render(request, 'bookmarks.html', {'houses': houses})
"""