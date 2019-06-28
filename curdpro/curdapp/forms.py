from django import forms

class ProductForm(forms.Form):
    product_number = forms.IntegerField(
        label='enter product number',
        widget = forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'product number'
            }
        )
    )
    product_name = forms.CharField(
        label ='enter product name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'product name'
            }

        )
    )
    product_cost = forms.IntegerField(
        label = 'enter product cost',
        widget=forms.NumberInput(
            attrs={
            'class':'form-control',
            'placeholder':'product cost'
            }
        )
    )

    product_class = forms.CharField(
        label ='enter product class',
        widget = forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'product class'
            }
        )
    )
    product_weight = forms.IntegerField(
        label='enter product weight',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'product weight'
            }
        )
    )
class UpdatingData(forms.Form):
    product_number = forms.IntegerField(
        label='enter product number',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'product number'
            }
        )
    )


    product_cost = forms.IntegerField(
    label='enter product cost',
    widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'product cost'
        }
    )
)
class DeletingData(forms.Form):
    product_number = forms.IntegerField(
        label='enter product number',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'product number'
            }
        )
    )

