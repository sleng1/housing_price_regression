from django import forms

class HouseForm(forms.Form):
    beds = forms.IntegerField(label="", 
                              widget=forms.TextInput(
                                  attrs={'placeholder': 'Beds'}))
    baths = forms.DecimalField(label="", max_digits=4, decimal_places=1, 
                               widget=forms.TextInput(
                                   attrs={'placeholder': 'Baths'}))
    square_feet = forms.IntegerField(label="", 
                                     widget=forms.TextInput(
                                         attrs={'placeholder': 'Square Feet'}))
    year_built = forms.IntegerField(label="",
                                    widget=forms.TextInput(
                                        attrs={'placeholder': 'Year Built'}))
    garages = forms.IntegerField(label="",
                                 widget=forms.TextInput(
                                     attrs={'placeholder': 'Garage Spaces'}))
    lot_sqft = forms.IntegerField(label="",
                                  widget=forms.TextInput(
                                      attrs={'placeholder': 'Lot Square Feet'}))