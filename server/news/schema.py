import graphene

# models
from users.schema import UserType
from news.models import News

# resolvers
from news.resolvers import get_news

# other stuff
from users.utils import access_required

class NewsType(graphene.ObjectType):
    '''Representação de uma Noticia'''
    class Meta:
        interfaces = (graphene.relay.Node,)

    # atributos
    title = graphene.String(
        description='News title.'
    )
    body = graphene.String(
        description='News main content.'
    )
    votes = graphene.Int(
        description='Votes this news has received.'
    )
    publication_date = graphene.DateTime(
        description='Publish datetime.'
    )
    author = graphene.Field(
        UserType,
        description='News author.'
    )

    @classmethod
    def get_node(cls, info, id):
        return get_news(id=id)
        

class NewsConnection(graphene.relay.Connection):
    class Meta:
        node = NewsType


class Query(object):
    '''
    Consultas GraphQL delimitando-se ao escopo de notícias.
    '''

    node = graphene.relay.Node.Field()

    # news = graphene.List(NewsType)
    news = graphene.relay.ConnectionField(
        NewsConnection
    )

    @access_required
    def resolve_news(self, info, **kwargs):
        '''
        retorna uma lista de noticias registradas
        no sistema.
        '''

        return get_news()


class CreateNews(graphene.relay.ClientIDMutation):
    '''
    Cria uma Noticia
    '''
    news = graphene.Field(
        NewsType,
        description='Created news data response.'
    )

    class Input:
        title = graphene.String(description='News title.')
        body = graphene.String(description='News main content.')

    @access_required
    def mutate_and_get_payload(self, info, **_input):
        # captura dos inputs
        title = _input.get('title')
        body = _input.get('body')

        try:
            news = News.objects.create(
                title=title,
                body=body,
                author=info.context.user
            )
            news.save()

            return CreateNews(news)

        except Exception as exception:
            raise(exception)


class Mutation:
    create_news = CreateNews.Field()
