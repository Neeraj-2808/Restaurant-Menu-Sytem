from django import forms

from .models import Menu

class MenuForm(forms.ModelForm):

    class Meta:
        
        model = Menu

        exclude =  ['id','uuid','active_status']
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                                           'placeholder': 'Enter menu name'}),
            'description': forms.Textarea(attrs={'class': 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input',
                                                 'rows': 4,
                                                 'placeholder': 'Enter description'})
        }
