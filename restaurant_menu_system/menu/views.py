from django.views import View

from .models import Menu  # Your Menu model

from django.shortcuts import render, redirect

from .forms import MenuForm  # Your MenuForm

class MenuListView(View):

    def get(self,request,*args,**kwargs):

        menus = Menu.objects.all()         #  .order_by('-id')   Get all menus, newest first

        print(menus)

        return render(request,'menu/menu.html',{'menus': menus})


class MenuCreateView(View):
    
    def get(self,request,*args,**kwargs):
        
        form = MenuForm()

        return render(request, 'menu/registration.html', {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = MenuForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('menu-details')  
        return render(request, 'menu/registration.html', {'form': form})