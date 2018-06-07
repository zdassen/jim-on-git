from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy

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


class PointFormView(object):
    """要点の新規作成/編集"""

    # 対象のモデル
    model = Point

    # 編集対象のフィールド
    fields = (
        "content",
    )

    # 使用するテンプレート
    template_name = "jim/point/point_form.html"

    def get_context_data(self, **kwargs):
        """埋め込み変数をセットする"""
        context = super().get_context_data(**kwargs)

        # 記事の ID をセットする
        context["article_id"] = self.kwargs["article_id"]

        return context

    def form_valid(self, form):
        """値が正常な場合の処理"""
        form.instance.user = self.request.user

        # 記事を取得する & フォームにセットする
        article = get_object_or_404(
            Article, pk=self.kwargs["article_id"])
        form.instance.article = article

        return super().form_valid(form)

    def get_success_url(self):
        """作成/編集成功時のリダイレクト先"""
        return reverse_lazy("jim:article-detail",
            kwargs={"pk": self.kwargs["article_id"]})


class PointCreateView(PointFormView, CreateView):
    """要点の新規作成"""
    pass


class PointEditView(PointFormView, EditView):
    """要点の編集"""
    pass


class ThoughtFormView(object):
    """思考の新規作成/編集"""

    # 対象のモデル
    model = Thought

    # 編集対象のフィールド
    fields = (
        "thought_type",
        "content",
    )

    # 使用するテンプレート
    template_name = "jim/thought/thought_form.html"

    def get_context_data(self, **kwargs):
        """埋め込み変数をセットする"""
        context = super().get_context_data(**kwargs)

        # 記事の ID をセットする
        context["article_id"] = self.kwargs["article_id"]

        # 要点の ID をセットする
        context["point_id"] = self.kwargs["point_id"]

        return context

    def form_valid(self, form):
        """フォームの値が正常な場合の処理"""
        form.instance.user = self.request.user

        # 記事をセットする
        form.instance.article = get_object_or_404(
            Article, pk=self.kwargs["article_id"])

        # 要点をセットする
        form.instance.point = get_object_or_404(
            Point, pk=self.kwargs["point_id"])

        return super().form_valid(form)

    def get_success_url(self):
        """"作成/編集成功時のリダイレクト先"""
        return reverse_lazy("jim:article-detail",
            kwargs={"pk": self.kwargs["article_id"]})


class ThoughtCreateView(ThoughtFormView, CreateView):
    """思考の新規作成"""
    pass


class ThoughtEditView(ThoughtFormView, EditView):
    """思考の新規作成"""
    pass