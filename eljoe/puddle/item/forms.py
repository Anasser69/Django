from django import forms


from .models import Item

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image',)

        widgets = {
            'category': forms.Select(attrs={
                'class': 'text-center p-2',
                'style': 'width: 100%;outline:none;border:none;'
            }),
            'name': forms.TextInput(attrs={
                'placeholder': 'Name of the Item :',
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Description for the Item :',
                'class': 'rounded p-1',
                'style': 'outline:none;border:none;'
            }),
            'price': forms.TextInput(attrs={
                'placeholder': 'price of the Item $ :',
            }),
        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'image', 'is_sold')

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Name of the Item :',
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Description for the Item :',
                'class': 'rounded p-1',
                'style': 'outline:none;border:none;'
            }),
            'price': forms.TextInput(attrs={
                'placeholder': 'price of the Item $ :',
            }),
        }