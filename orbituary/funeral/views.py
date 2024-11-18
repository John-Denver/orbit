from django.shortcuts import render, redirect, get_object_or_404
from django.utils.text import slugify
from .models import Obituary
from django.http import HttpResponse



def submit_obituary(request):
    if request.method == 'POST':
        # Get form data from the request
        name = request.POST.get('name')
        date_of_birth = request.POST.get('date_of_birth')
        date_of_death = request.POST.get('date_of_death')
        content = request.POST.get('content')
        author = request.POST.get('author')

        # Generate a slug from the name
        slug = slugify(name)

        # Save the obituary data to the database
        obituary = Obituary(
            name=name,
            date_of_birth=date_of_birth,
            date_of_death=date_of_death,
            content=content,
            author=author,
            slug=slug
        )
        obituary.save()

        # Redirect to the list of obituaries after successful submission
        return redirect('view_obituaries')
    else:
        return render(request, 'funeral/obituary_form.html')

    

def view_obituaries(request):
    # Retrieve all obituary records from the database
    obituaries = Obituary.objects.all()

    # Render the template with the obituary data
    return render(request, 'funeral/view_obituaries.html', {'obituaries': obituaries})


def view_obituary_detail(request, slug):
    # Retrieve the obituary based on the slug
    obituary = get_object_or_404(Obituary, slug=slug)

    # Render the obituary detail page
    return render(request, 'funeral/view_obituary_detail.html', {'obituary': obituary})

