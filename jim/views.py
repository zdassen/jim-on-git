from django.shortcuts import render
from django.views import generic

from .models import Article, Point, Thought


# Create your views here.
class CreateView(generic.CreateView):
    
    def get_context_data(self, **kwargs):
        """埋め込み変数をセットする"""
        context = super().get_context_data(**kwargs)

        # CRUD のタイプをセットする
        context["crud_type"] = "new"

        # ボタンの値をセットする
        context["button_value"] = "新規作成"

        return context


class EditView(generic.UpdateView):
    
    def get_context_data(self, **kwargs):
        """埋め込み変数をセットする"""
        context = super().get_context_data(**kwargs)

        # CRUD のタイプをセットする
        context["crud_type"] = "edit"

        # ボタンの値をセットする
        context["button_value"] = "編集/更新"

        return context


class ArticleIndexView(generic.ListView):
    """記事(ネタ)の一覧"""

    # 対象のモデル
    model = Article

    # 使用するテンプレート
    template_name = "jim/article/article_list.html"

    def get_queryset(self):
        """レコードを取得する"""
        article_list = Article.objects.filter(
            user=self.request.user
        ).order_by("-id")

        return article_list


class ArticleDetailView(generic.DetailView):
    """記事(ネタ)の詳細"""

    # 対象のモデル
    model = Article

    # 使用するテンプレート
    template_name = "jim/article/article_detail.html"


class ArticleFormView(object):
    """記事(ネタ)の新規作成/編集"""

    # 対象のモデル
    model = Article

    # 編集対象のフィールド
    fields = (
        "title",
    )

    # 使用するテンプレート
    template_name = "jim/article/article_form.html"

    def form_valid(self, form):
        """フォームの値が正常な場合の処理"""
        form.instance.user = self.request.user

        return super().form_valid(form)


class ArticleCreateView(ArticleFormView, CreateView):
    """記事(ネタ)の新規作成"""
    pass


class ArticleEditView(ArticleFormView, EditView):
    """記事(ネタ)の編集"""
    pass