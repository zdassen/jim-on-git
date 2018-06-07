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

    # # # # # Point モデル # # # # #

    # 要点の新規作成
    # ex: /jim/articles/42/points/new/
    path("articles/<int:article_id>/points/new/",
        views.PointCreateView.as_view(),
        name="point-new"
    ),

    # 要点の編集
    # ex: /jim/articles/42/points/edit/42/
    path("articles/<int:article_id>/points/edit/<int:pk>/",
        views.PointEditView.as_view(),
        name="point-edit"
    ),

    # # # # # Thought モデル # # # # #

    # 思考の新規作成
    # ex: /jim/articles/42/points/42/thoughts/new/
    path("articles/<int:article_id>/points/<int:point_id>/thoughts/new/",
        views.ThoughtCreateView.as_view(),
        name="thought-new"
    ),

    # 思考の編集
    # ex: /jim/articles/42/points/42/thoughts/new/
    path("articles/<int:article_id>/points/<int:point_id>/thoughts/edit/<int:pk>/",
        views.ThoughtEditView.as_view(),
        name="thought-edit"
    ),

]