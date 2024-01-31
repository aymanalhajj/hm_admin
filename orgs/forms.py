from django import forms


class MapForm(forms.Form):
    from_date = forms.DateTimeField(label="from date",widget=forms.widgets.DateInput(
            attrs={
                'type': 'date', 
                'placeholder': 'yyyy-mm-dd (DOB)',
                'class': 'form-control'
            }))
    to_date = forms.CharField(label="to date", max_length=100)