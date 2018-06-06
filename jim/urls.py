# jim/urls.py
from django.urls import path

from . import views


app_name = "jim"

urlpatterns = [

    # # # # # Article モデル # # # # #

    # 記事(のネタ)の一覧
    # ex: /jim/articles/
    path("articles/",
        views.ArticleIndexView.as_view(),
        name="article-index"
    ),

    # 記事(のネタ)の詳細
    # ex: /jim/articles/42/
    path("articles/<int:pk>/",
        views.ArticleDetailView.as_view(),
        name="article-detail"
    ),

    # 記事(のネタ)の新規作成
    # ex: /jim/articles/new/
    path("articles/new/",
        views.ArticleCreateView.as_view(),
        name="article-new"
    ),

    # 記事(のネタ)の編集
    # ex: /jim/articles/edit/42/
    path("articles/edit/<int:pk>/",
        views.ArticleEditView.as_view(),
        name="article-edit"
    ),

]