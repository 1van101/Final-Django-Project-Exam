from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import generic as views
from django.db.models import Count

from FINAL_EXAM.common.forms import SearchForm, CommentForm
from FINAL_EXAM.common.models import Like, Comment
from FINAL_EXAM.drawings.models import Drawing
from FINAL_EXAM.kids.models import Kid

UserModel = get_user_model()


def show_home_page(request):
    user = request.user
    queryset = Drawing.objects.all().order_by('-id')
    search_form = SearchForm()
    liked_drawings_by_user = [l.to_drawing_id for l in user.like_set.all()] if user.is_authenticated else []

    search_query = request.GET.get('drawings_of_searched_kid')

    if request.method == 'GET':
        search_form = SearchForm(request.GET)
        if search_form.is_valid():
            queryset = queryset.filter(kid_owner_drawing__name__iexact=search_query).all()

    paginate_by = 3
    paginator = Paginator(queryset, paginate_by)
    page_number = request.GET.get('page', 1)

    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    kid_added = search_query in [x.name for x in Kid.objects.all()] if Kid.objects.all() else []

    context = {
        'kid_added': kid_added,
        'drawings': page_obj,
        'search_form': search_form,
        'page_obj': page_obj,
        'liked_drawings_by_user': liked_drawings_by_user,

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


class AddCommentView(LoginRequiredMixin, views.CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        drawing_id = self.kwargs['drawing_id']
        drawing = Drawing.objects.get(id=drawing_id)

        comment = form.save(commit=False)
        comment.to_drawing = drawing
        comment.user = self.request.user
        comment.save()

        return super().form_valid(form)

    def get_success_url(self):
        drawing_id = self.kwargs['drawing_id']
        return f'{self.request.META["HTTP_REFERER"]}#{drawing_id}'


@login_required
def admin_panel(request):
    return HttpResponseRedirect(
        "http://127.0.0.1:8000/admin/"
    )


class LeaderboardView(views.ListView):
    template_name = 'common/leaderboard.html'
    model = Drawing

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['drawings_with_likes'] = self.object_list.annotate(
            num_likes=Count('like')).order_by('-num_likes')

        return context
