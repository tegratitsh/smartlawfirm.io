from django.shortcuts import render, redirect
from .models import Field, Topic, Title, Contact, Lawyer
from .forms import ContactForm



def law_home_view(request):


    fields = Field.objects.all()
    topics = Topic.objects.all()


    context = {'fields':fields, 'topics':topics}


    return render(request, 'Law/index.html', context)




def law_contact_view(request):

    contacts = Contact.objects.all()
    topics = Topic.objects.all()
    

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('law-home')  # Redirige vers une page de confirmation
    else:
        form = ContactForm()

    context = {"form": form, 'contacts':contacts, 'topics':topics, }

    return render(request, "Law/law_contact.html", context)




def law_field_view(request):


    fields = Field.objects.all()
    topics = Topic.objects.all()

    context = {'fields':fields, 'topics':topics}




    return render(request, 'Law/law_field.html', context)



def law_team_view(request):

    lawyers = Lawyer.objects.all()
    topics = Topic.objects.all()
    context = {'lawyers':lawyers, 'topics':topics}

    return render(request, 'Law/law_our_team.html', context)




def law_about_us_view(request):

    topics = Topic.objects.all()
    context = {'topics':topics}

    return render(request, 'Law/law_about_us.html',context)

