from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views import generic as views

from FINAL_EXAM.common.forms import SearchForm
from FINAL_EXAM.common.models import Like
from FINAL_EXAM.drawings.models import Drawing
from FINAL_EXAM.kids.models import Kid


def show_home_page(request):
    paginate_by = 3
    queryset = Drawing.objects.all()
    search_form = SearchForm()

    page_number = request.GET.get('page', 1)
    search_query = request.GET.get('drawings_of_searched_kid')
    user = request.user

    liked_drawings_by_user = [l.to_drawing_id for l in user.like_set.all()] if user.is_authenticated else []

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
        'liked_drawings_by_user': liked_drawings_by_user

    }
    return render(request, 'common/index.html', context)


@login_required
def like_functionality(request, drawing_id):
    drawing = Drawing.objects.get(id=drawing_id)
    liked_obj = Like.objects.filter(to_drawing_id=drawing_id, user=request.user).first()

    if liked_obj:
        liked_obj.delete()
    else:
        like = Like(to_drawing=drawing, user=request.user)
        like.save()

    return redirect(request.META['HTTP_REFERER'] + f'#{drawing_id}')
