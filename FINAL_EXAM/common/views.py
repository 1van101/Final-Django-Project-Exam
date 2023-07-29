from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import generic as views


class Index(views.View):
    template_name = 'common/index.html'

    def get(self, request):
        your_data = [...]  # Replace this with your list of card data

        # Number of cards to display per page
        cards_per_page = 3

        paginator = Paginator(your_data, cards_per_page)

        # Get the current page number from the request's GET parameters
        page_number = request.GET.get('page')

        # Get the Page object for the current page number
        page_obj = paginator.get_page(page_number)

        return render(request, self.template_name, {'page_obj': page_obj})