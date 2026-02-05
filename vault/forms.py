from django import forms

class SecretMessageForm(forms.Form):
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            "rows": 5,
            "placeholder": "Type your secret message..."
        }),
        required=True
    )

    expires_at = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(attrs={
            "type": "datetime-local"
        })
    )
