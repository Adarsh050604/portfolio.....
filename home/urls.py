from django.urls import path
from .views import index, about, services, portfolio, contact_view, contact_success_view, test_email, generate_qr_code, qr_code_page

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('services/', services, name='services'),
    path('portfolio/', portfolio, name='portfolio'),
    path('contact/', contact_view, name='contact'),
    path('contact/success/', contact_success_view, name='contact_success'),
    path('test-email/', test_email, name='test_email'),  # Test Email Page
    path('generate-qr/<str:text>/', generate_qr_code, name='generate_qr_code'),  # QR Code Generation
    path('qr-code/', qr_code_page, name='qr_code_page'),  # QR Code Page
]