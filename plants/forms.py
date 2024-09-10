from django import forms
from .widgets import CustomClearableFileInput
from .models import Plant, Category, PlantReview, SeasonalEvent

class PlantForm(forms.ModelForm):
    
    class Meta:
        model = Plant
        fields = "__all__"

    image = forms.ImageField(
        label="Image", required=False, widget=CustomClearableFileInput
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields["category"].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "border-black rounded-0"

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price <= 0:
            raise forms.ValidationError('Price must be a positive value.')
        return price

    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if rating is not None and (rating < 1 or rating > 5):
            raise forms.ValidationError('Rating must be between 1 and 5.')
        return rating

class ReviewForm(forms.ModelForm):
    
    class Meta:
        model = PlantReview
        fields = "__all__"

class EventForm(forms.ModelForm):
    
    class Meta:
        model = SeasonalEvent
        fields = "__all__"
