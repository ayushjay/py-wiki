from django.shortcuts import render
import markdown2
from . import util


def index(request):
    return render(request,
                   "encyclopedia/index.html", 
                   {"entries": util.list_entries()})

def entry_page(request, title):
    title_dict = util.get_entry(title)
    return render(request,
                "encyclopedia/entry.html", 
                {"title_dict1": title_dict}
                  )
# IMPORTANT LEARNING: IT IS THE CONTEXT DICTIONARY  NAME NAME NAME THAT IS PASSED INTO THE HTML PAGE FOR USE
def trial_page(request, name):
    return render(request,
                  "encyclopedia/trial_html.html",
                  {"name_dict": name}
                  )

