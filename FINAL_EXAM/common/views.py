from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import generic as views

from FINAL_EXAM.accounts.models import AppUser
from FINAL_EXAM.common.forms import SearchForm
from FINAL_EXAM.drawings.models import Drawing
from FINAL_EXAM.kids.models import Kid


def show_home_page(request):
    paginate_by = 3
    queryset = Drawing.objects.all()
    search_form = SearchForm()
    page_number = request.GET.get('page', 1)
    search_query = request.GET.get('drawings_of_searched_kid')
    if search_query:
        queryset = queryset.filter(kid_owner_drawing__name__icontains=search_query).all()

    paginator = Paginator(queryset, paginate_by)
    page_obj = paginator.get_page(page_number)
    kid_added = search_query in [x.name for x in Kid.objects.all()] if Kid.objects.all() else []

    context = {
        'kid_added': kid_added,
        'drawings': page_obj,
        'search_form': search_form,
        'page_obj': page_obj,

    }
    return render(request, 'common/index.html', context)
