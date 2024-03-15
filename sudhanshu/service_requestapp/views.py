from django.shortcuts import render

# Create your views here.
# views.py

from django.shortcuts import render, redirect
from .Forms import ServiceRequestForm

def submit_service_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Redirect to a success page
    else:
        form = ServiceRequestForm()
    return render(request, 'submit_service_request.html', {'form': form})

def success_page(request):
    return render(request, 'success_page.html')



# views.py

from django.shortcuts import render
from .models import ServiceRequest

def view_service_requests(request):
    service_requests = ServiceRequest.objects.all()
    return render(request, 'view_service_requests.html', {'service_requests': service_requests})
