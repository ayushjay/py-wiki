from django.shortcuts import render
import markdown2
from . import util


def index(request):
    return render(request,
                   "encyclopedia/index.html", 
                   {"entries": util.list_entries()})

def entry_page(request, title):
    return render(request,
                "encyclopedia/index.html", 
                {"context": util.get_entry(title)}
                  )
