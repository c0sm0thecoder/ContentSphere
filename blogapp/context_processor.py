from .models import Category


def category_choices(request):
    return {'category_choices': Category.choices}
