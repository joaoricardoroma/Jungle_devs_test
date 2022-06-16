from django_elasticsearch_dsl import Document, fields, Index
from django_elasticsearch_dsl.registries import registry
from .models import Author, Article


@registry.register_document
class AuthorDocument(Document):

    class Index:
        name = 'author'
        setting = {
            'number_of_shards': 1,
            'number_of_replicas': 1
        }

    class Django:
        model = Author

        fields = ["id", "name", "picture"]


@registry.register_document
class ArticleDocument(Document):

    class Index:
        name = 'article'
        setting = {
            'number_of_shards': 1,
            'number_of_replicas': 1
        }

    class Django:
        model = Article

        fields = ["id", "category", "title", "summary", "first_paragraph", "body"]
