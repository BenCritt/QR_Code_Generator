# This is the form for the QR Code Generator.
class QRForm(forms.Form):
    # Create a CharField to hold the text input for the QR code.
    qr_text = forms.CharField(
        label="",
        max_length=8000,  # Set the maximum length of the text input to 8000 characters.
        # Configure the TextInput widget with a custom class for styling and set the size attribute.
        widget=forms.TextInput(attrs={"class": "myform", "size": 30}),
    )
