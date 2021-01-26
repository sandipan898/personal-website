from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(required=True, label='Your name',max_length=100)

    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=False, max_length=100)
    message = forms.CharField(widget=forms.Textarea(
                attrs={
                        'rows': 5,
                }
        )
    )
