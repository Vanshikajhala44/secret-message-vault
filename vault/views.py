from django.shortcuts import render, redirect
from django.conf import settings
from .forms import SecretMessageForm
from .models import SecretMessage
from django.shortcuts import get_object_or_404
from django.utils import timezone

def create_message(request):
    if request.method == "POST":
        form = SecretMessageForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data["message"]
            expires_at = form.cleaned_data["expires_at"]

            encrypted = settings.FERNET.encrypt(
                message.encode()
            ).decode()

            secret = SecretMessage.objects.create(
                encrypted_message=encrypted,
                expires_at=expires_at
            )

            return redirect("success", secret_id=secret.id)
    else:
        form = SecretMessageForm()

    return render(request, "vault/create.html", {"form": form})

def success(request, secret_id):
    link = request.build_absolute_uri(f"/message/{secret_id}/")
    return render(request, "vault/success.html", {"link": link})

def view_message(request, secret_id):
    secret = get_object_or_404(SecretMessage, id=secret_id)

    # Already viewed
    if secret.viewed:
        return render(request, "vault/expired.html")

    # Expired by time
    if secret.expires_at and timezone.now() > secret.expires_at:
        return render(request, "vault/expired.html")

    # Decrypt message
    message = settings.FERNET.decrypt(
        secret.encrypted_message.encode()
    ).decode()

    # Mark as viewed
    secret.viewed = True
    secret.save()

    return render(request, "vault/view.html", {"message": message})
