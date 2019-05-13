import graphene

# models
from users.schema import UserType
from news.models import News

# resolvers
from news.resolvers import get_news

# other stuff
from users.utils import access_required
from graphql_relay import from_global_id


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

    news = graphene.relay.ConnectionField(
        NewsConnection,
        author=graphene.Int(
            description="Author's integer ID."
        ),
        title_contains=graphene.String(
            description='The title must contain...'
        ),
        body_contains=graphene.String(
            description='Body text must contain...'
        )
    )

    @access_required
    def resolve_news(self, info, **kwargs):
        '''
        retorna uma lista de noticias registradas
        no sistema.
        '''
        return get_news(**kwargs)


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


class UpdateNews(graphene.relay.ClientIDMutation):
    '''
    Atualiza uma Notícia.
    '''
    news = graphene.Field(
        NewsType,
        description='Updated news data response.'
    )

    class Input:
        title = graphene.String(description='News title.', required=False)
        body = graphene.String(description='News main content.', requried=False)
        id = graphene.ID(description='News ID.', required=True)

    @access_required
    def mutate_and_get_payload(self, info, **_input):
        # captura os inputs
        title = _input.get('title')
        body = _input.get('body')
        _, id = from_global_id(_input.get('id'))

        # identifica o usuario
        user = info.context.user

        # recupera o objeto do banco de dados
        try:
            news = News.objects.get(id=id)
        except Exception as exception:
            raise(exception)

        # somente poderá modificar o objeto se for o autor do mesmo
        if not news.author.id == user.id:
            raise Exception("You don't have permission to do this.")

        # atualiza o objeto
        if title:
            news.title = title
        if body:
            news.body = body
        news.save()

        return UpdateNews(news)


class DeleteNews(graphene.relay.ClientIDMutation):
    '''
    Remove uma Notícia.
    '''
    news = graphene.Field(
        NewsType,
        description='Deleted News.'
    )

    class Input:
        id = graphene.ID(description='ID da notícia', required=True)

    @access_required
    def mutate_and_get_payload(self, info, **_input):
        _, id = from_global_id(_input.get('id'))
        # identifica o usuario
        user = info.context.user

        # recupera o objeto do banco de dados
        try:
            news = News.objects.get(id=id)
        except Exception as exception:
            raise(exception)

        # somente poderá modificar o objeto se for o autor do mesmo
        if not news.author.id == user.id:
            raise Exception("You don't have permission to do this.")

        deleted_data = news
        news.delete()
        return DeleteNews(deleted_data)


class Mutation:
    create_news = CreateNews.Field()
    update_news = UpdateNews.Field()
    delete_news = DeleteNews.Field()
