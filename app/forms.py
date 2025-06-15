from django import forms
from .models import Testimonial

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['name', 'role', 'rating', 'message', 'photo']
        widgets = {
            'rating': forms.NumberInput(attrs={
                'min': 1,
                'max': 5,
                'step': 1,
                'placeholder': '1-5'
            }),
            'name': forms.TextInput(attrs={'placeholder': 'Your Name'}),
            'message': forms.Textarea(attrs={'placeholder': 'Your honest feedback...'}),
        }

    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if rating < 1 or rating > 5:
            raise forms.ValidationError("Rating must be between 1 and 5 stars.")
        return rating
