from django.shortcuts import render, redirect
from .models import Contact
from .forms import *

# Display all contacts
def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contact/contactlist.html', {'contacts': contacts})

# Add new contact
def add_contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        alternative_phone = request.POST.get('alternative_phone', '')
        image = request.FILES.get('image')
        Contact.objects.create(
            name=name, email=email, phone=phone, alternative_phone=alternative_phone, image=image
        )
        return redirect('contactlist')
    return render(request, 'contact/add_contact.html')

# View individual contact
def contact_detail(request, pk):
    contact = Contact.objects.get(pk=pk)
    return render(request, 'contact/contact_detail.html', {'contact': contact})

# Edit contact
def edit_contact(request, pk):
    contact = Contact.objects.get(pk=pk)
    if request.method == 'POST':
        contact.name = request.POST['name']
        contact.email = request.POST['email']
        contact.phone = request.POST['phone']
        contact.alternative_phone = request.POST.get('alternative_phone', '')
        if 'image' in request.FILES:
            contact.image = request.FILES['image']
        contact.save()
        return redirect('contact_detail', pk=pk)
    return render(request, 'contact/edit_contact.html', {'contact': contact})

# Delete contact
def delete_contact(request, pk):
    contact = Contact.objects.get(pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('contactlist')
    return render(request, 'contact/delete_contact.html', {'contact': contact})

# Call contact
def call_contact(request, pk):
    contact = Contact.objects.get(pk=pk)
    return render(request, 'contact/callcontact.html', {'contact': contact})

