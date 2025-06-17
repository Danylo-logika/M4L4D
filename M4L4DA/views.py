from django.shortcuts import render

from M4L4DA.models import Review

# Create your views here.
def main_page(request):
    review = Review.objects.all()
    context = {
        'review_list': review
    }

    return render(request,"M4L4DA/review_list.html", context)