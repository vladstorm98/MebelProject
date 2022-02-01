from django.db.models import Count

from .models import *

menu = [{'title': "Оплата и доставка", 'url_name': 'payment_and_delivery'},
        {'title': "Магазины", 'url_name': 'stores'},
        {'title': "Отзывы клиентов", 'url_name': 'customer_reviews'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Добавить позицию", 'url_name': 'add_post'},
        ]

features = [{'title': 'Особенность 1', 'url_name': 'feature_1'},
            {'title': 'Особенность 2', 'url_name': 'feature_2'},
            {'title': 'Особенность 3', 'url_name': 'feature_3'},
            {'title': 'Особенность 4', 'url_name': 'feature_4'},
            ]

advantages = [{'title': 'Топ-сервис', 'url_name': 'advantage_1',
               'content': 'Тысячи покупателей остались довольны слаженной работой нашей команды и рекомендуют Pufetto '
                          'своим друзьям.'},
              {'title': 'Быстрые сроки', 'url_name': 'advantage_2',
               'content': 'Без задержек - наши процессы построены так, чтобы производство ваших заказов не '
                          'прекращалось ни на секунду.'},
              {'title': 'Онлайн статус заказа', 'url_name': 'advantage_3',
               'content': 'В любое время и с любого устройства – актуальный статус вашего заказа всегда под рукой. '
                          'Благодаря отточенной IT-системе мы практически посекундно знаем, на каком этапе находится '
                          'ваш заказ.'},
              {'title': 'High quality продуктовый контент', 'url_name': 'advantage_4',
               'content': 'Высококачественные 3D модели и фотографии для вашей уверенности - доставленный продукт '
                          'будет выглядеть именно так, как на сайте.'},
              ]

instagram = [{'link': '#', 'url_name': 'inst_1'},
             {'link': '#', 'url_name': 'inst_2'},
             {'link': '#', 'url_name': 'inst_3'},
             {'link': '#', 'url_name': 'inst_4'},
             {'link': '#', 'url_name': 'inst_5'},
             {'link': '#', 'url_name': 'inst_6'},
             {'link': '#', 'url_name': 'inst_7'},
             {'link': '#', 'url_name': 'inst_8'},
             {'link': '#', 'url_name': 'inst_9'},
             {'link': '#', 'url_name': 'inst_10'},
             ]


class DataMixin:
    paginate_by = 9

    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.annotate(Count('catalog'))
        most_popular = Catalog.objects.order_by('-views')[:10]
        new = Catalog.objects.order_by('-time_create')[:10]

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(-1)

        context['menu'] = user_menu
        context['features'] = features
        context['advantages'] = advantages
        context['instagram'] = instagram

        context['cats'] = cats
        context['most_popular'] = most_popular
        context['new'] = new

        return context
