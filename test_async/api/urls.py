from aiohttp import web

from api import views

urls = [
    web.view('/todo/{id}', views.TodoViewSingle),
    web.view('/todo', views.TodoViewList)]
