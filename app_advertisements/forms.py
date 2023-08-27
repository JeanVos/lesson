from django import forms

# class AdvertisementsForm(forms.Form):
#     title = forms.CharField(max_length=64, 
#         widget = forms.TextInput(attrs={'class':'form-control from-control-lg'})
#     )
#     description = forms.CharField(
#         widget = forms.Textarea(attrs={'class':'form-control from-control-lg'})
#     )
#     price = forms.DecimalField(
#         widget = forms.NumberInput(attrs={'class':'form-control from-control-lg'})
#     )
#     auction = forms.NullBooleanField(required=False,
#         widget = forms.CheckboxInput(attrs={'class':'form-check-imput'})
#     )
#     image = forms.ImageField(
#         widget = forms.FileInput(attrs={'class':'form-control from-control-lg'})
#     )

from .models import Advertisements

class AdvertisementsForm(forms.ModelForm):
    class Meta:
        model = Advertisements
        fields = ['title', 'description','price','auction', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control from-control-lg'}),
            'description': forms.Textarea(attrs={'class': 'form-control from-control-lg'}),
            'price': forms.NumberInput(attrs={'class': 'form-control from-control-lg'}),
            'auction':forms.CheckboxInput(attrs={'class':'form-check-imput'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control from-control-lg'}),
        }
    
    def clean_title(self):
        title = self.cleaned_data['title']
        if title.startswith('?'):
            raise forms.ValidationError("Title can't start with a question mark")
        return title
