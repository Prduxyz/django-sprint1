from django.http import Http404
from django.shortcuts import render


posts = [
    {
        'id': 0,
        'location': 'Остров отчаянья',
        'date': '30 сентября 1659 года',
        'category': 'travel',
        'text': '''Наш корабль, застигнутый в открытом море
                страшным штормом, потерпел крушение.
                Весь экипаж, кроме меня, утонул; я же,
                несчастный Робинзон Крузо, был выброшен
                полумёртвым на берег этого проклятого острова,
                который назвал островом Отчаяния.''',
    },
    {
        'id': 1,
        'location': 'Остров отчаянья',
        'date': '1 октября 1659 года',
        'category': 'not-my-day',
        'text': '''Проснувшись поутру, я увидел, что наш корабль сняло
                с мели приливом и пригнало гораздо ближе к берегу.''',
    },
    {
        'id': 2,
        'location': 'Остров отчаянья',
        'date': '25 октября 1659 года',
        'category': 'not-my-day',
        'text': '''Всю ночь и весь день шёл дождь и дул сильный
                порывистый ветер.''',
    },
]

posts_by_id = {post['id']: post for post in posts}


def index(request):
    """Главная страница блога. Показывает все посты."""
    context = {'posts': posts}
    return render(request, 'blog/index.html', context)


def category_posts(request, category_slug):
    """Страница постов определённой категории."""
    context = {'category_slug': category_slug}
    return render(request, 'blog/category.html', context)


def post_detail(request, id):
    """Страница отдельного поста."""
    if id not in posts_by_id:
        raise Http404('Пост не найден')
    context = {'post': posts_by_id[id]}
    return render(request, 'blog/detail.html', context)