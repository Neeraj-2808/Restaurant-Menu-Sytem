from django.views import View

from .models import Menuitems  # Your Menu model

from django.shortcuts import render, redirect,get_object_or_404

from .forms import MenuItemForm # Your MenuForm

from django.contrib import messages

class MenuitemListView(View):

    def get(self,request,*args,**kwargs):

        menus = Menuitems.objects.all()        

        return render(request,'menu/menu_item.html',{'menus': menus})


class MenuitemCreateView(View):
    
    def get(self,request,*args,**kwargs):
        
        form = MenuItemForm()

        return render(request, 'menu/item-registration.html', {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = MenuItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('menuitem-details')  
        return render(request, 'menu/item-registration.html', {'form': form})
    
class MenupriceUpdateView(View):

    def get(self, request, *args, **kwargs):

        uuid = kwargs.get('uuid')

        garbages = get_object_or_404(Menuitems, uuid=uuid)

        form = MenuItemForm(instance=garbages)

        return render(request, 'menu/menu_priceupdate.html', {'form': form})

    def post(self, request, *args, **kwargs):

        uuid = kwargs.get('uuid')

        garbages = get_object_or_404(Menuitems, uuid=uuid)

        form = MenuItemForm(request.POST, request.FILES, instance=garbages)

        if form.is_valid():

            form.save()

            return redirect('menuitem-details')
        
        return render(request, 'menu/menu_priceupdate.html', {'form': form})