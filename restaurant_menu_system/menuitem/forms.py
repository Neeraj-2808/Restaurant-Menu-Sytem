from django import forms
from .models import Menuitems

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = Menuitems
        exclude = ['id', 'uuid', 'active_status']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 '
                         'focus:border-purple-400 focus:outline-none focus:shadow-outline-purple '
                         'dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                'placeholder': 'Enter menu name'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 '
                         'focus:border-purple-400 focus:outline-none focus:shadow-outline-purple '
                         'dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                'placeholder': 'Enter price'
            }),
            'is_vegetarian': forms.CheckboxInput(attrs={
                'class': 'form-checkbox h-5 w-5 text-green-600 transition duration-150 ease-in-out'
            }),
            
        }
        menu = forms.ModelChoiceField(queryset=Menuitems.objects.all(),widget=forms.Select(attrs={'class':'block w-full mt-1 text-sm dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 form-select focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:focus:shadow-outline-gray',
                                                                                           }))  
