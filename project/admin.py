from suit.apps import DjangoSuitConfig
from suit.menu import ParentItem, ChildItem


class SuitConfig(DjangoSuitConfig):
    layout = 'vertical'

    menu = [
        ParentItem(
            'Основное',
            children=[
                ChildItem(model='core.calltoaction'),
                ChildItem(model='core.gallery'),
                ChildItem(model='core.subscribeblock')
            ]
        ),
        ParentItem(
            'Главная страница',
            children=[
                ChildItem(model='homepage.homepage'),
            ]
        ),
        ParentItem(
            'О компании',
            children=[
                ChildItem(model='about.aboutpage'),
            ]
        ),
        ParentItem(
            'Контакты',
            children=[
                ChildItem(model='contacts.contactspage'),
            ]
        ),
        ParentItem(
            'Страницы',
            children=[
                ChildItem(model='pages.flatpage'),
            ]
        ),
        ParentItem(
            'Принятые формы',
            children=[
                ChildItem(model='forms.feedback'),
                ChildItem(model='forms.order'),
                ChildItem(model='forms.subscribe')
            ]
        ),
        ParentItem(
            'Бренды',
            children=[
                ChildItem(model='brands.brand')
            ]
        ),
        ParentItem(
            'Проекты',
            children=[
                ChildItem(model='projects.project'),
                ChildItem(model='projects.projectcategory'),
                ChildItem(model='projects.projectspage')
            ]
        ),
        ParentItem(
            'Мероприятия',
            children=[
                ChildItem(model='events.event'),
                ChildItem(model='events.peventcategory'),
                ChildItem(model='events.eventspage')
            ]
        ),
        ParentItem(
            'Услуги',
            children=[
                ChildItem(model='services.service'),
                ChildItem(model='services.servicespage')
            ]
        ),
        ParentItem(
            'Блог',
            children=[
                ChildItem(model='blog.article'),
                ChildItem(model='blog.blogpage')
            ]
        ),
        ParentItem(
            'SEO',
            children=[
                ChildItem(model='seo.redirect')
            ]
        ),
        ParentItem(
            'Настройки',
            children=[
                ChildItem(model='vars.menu'),
                ChildItem(model='vars.menuitem'),
                ChildItem(model='vars.dbconfig'),
                ChildItem(model='vars.siteconfig'),
                ChildItem(model='vars.orderrole')
            ]
        ),
        ParentItem(
            'Пользователи',
            children=[
                ChildItem(model='users.user'),
                ChildItem(model='auth.group')
            ]
        )
    ]
