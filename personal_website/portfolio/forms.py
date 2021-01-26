from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(required=True, label='Your name',max_length=100,
                widget=forms.TextInput(
                    attrs={
                        'class': 'form-control'
                        }
                )
)

    from_email = forms.EmailField(
            required=True,
            widget=forms.EmailInput(
                    attrs={
                        'class': 'form-control'
                        }
                )

        )
    subject = forms.CharField(
            required=False, 
            max_length=100,
            widget=forms.TextInput(
                    attrs={
                        'class': 'form-control'
                        }
                )
        )
    message = forms.CharField(
            widget=forms.Textarea(
                    attrs={
                        'rows': 5,
                        'class': 'form-control'
                        }
                )
        )
