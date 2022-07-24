from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
allbooks = [
    {"title": "pan tadeusz", "author": "adam mickiewicz", "year": 1865, "pages": 200},
    {"title": "krzyżacy", "author": "henryk sienkiewicz", "year": 1905, "pages": 210},
    {"title": "lalka", "author": "boleslaw prus", "year": 1900, "pages": 199},
]


# books/
def listview(request):
    return render(
        request=request,
        template_name="books/list.html",
        context={'books': allbooks}
    )


def details(request, book_id: int):
    book = allbooks[book_id - 1]
    return render(
        request=request,
        template_name="books/details.html",
        context={'book': book}
    )
