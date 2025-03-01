from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.http import HttpResponse
from .forms import ContactMessageForm
import qrcode
import io

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            contact_message = form.save()
            # Render email template
            email_content = render_to_string('email/contact_message.html', {
                'name': contact_message.name,
                'email': contact_message.email,
                'message': contact_message.message,
            })
            # Send email notification
            send_mail(
                subject=f"New Contact Message from {contact_message.name}",
                message=email_content,
                from_email='adarshsajeevan050604@gmail.com',
                recipient_list=['adarshsajeevan050604@gmail.com'],
                fail_silently=False,
                html_message=email_content,
            )
            return redirect('contact_success')  # Redirect to a success page or the same page
    else:
        form = ContactMessageForm()
    return render(request, 'contact.html', {'form': form})

def contact_success_view(request):
    return render(request, 'contact_success.html')

def test_email(request):
    send_mail(
        'Test Email',
        'This is a test email.',
        'adarshsajeevan050604@gmail.com',
        ['recipient@example.com'],
        fail_silently=False,
    )
    return HttpResponse('Email sent successfully')

def generate_qr_code(request, text):
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)

    # Create an image from the QR code
    img = qr.make_image(fill='black', back_color='white')

    # Save the image to a BytesIO object
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    # Return the image as an HTTP response
    return HttpResponse(buffer, content_type="image/png")

def qr_code_page(request):
    return render(request, 'qr_code.html', {'text': 'Hello, World!'})