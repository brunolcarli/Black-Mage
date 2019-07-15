import graphene

# models
from users.schema import UserType
from civil_cultural.models import (Portal, Topic, Article, Question, Tag, Rule,
                                    SimilarSuggestion, News)

# resolvers
# from civil_cultural.resolvers import get_news

# other stuff
from users.utils import access_required
from graphql_relay import from_global_id


##########################################################################
# GraphQl Objects
##########################################################################
class PortalType(graphene.ObjectType):
    '''
        Defines a GraphQl Portal object.
    '''
    class Meta:
        interfaces = (graphene.relay.Node,)

    name = graphene.String()
    founding_datetime = graphene.DateTime()
    topics = graphene.ConnectionField('civil_cultural.schema.TopicConnection')
    news = graphene.ConnectionField('civil_cultural.schema.NewsConnection')
    rules = graphene.ConnectionField('civil_cultural.schema.RuleConnection')
    # TODO - add Chat
    # TODO - add Users
    # TODO - add Tags

    def resolve_topics(self, info, **kwargs):
        return self.topic_set.all()

    def resolve_rules(self, info, **kwargs):
        return self.rule_set.all()

    def resolve_news(self, info, **kwargs):
        return self.news_set.all()


class PortalConnection(graphene.relay.Connection):
    class Meta:
        node = PortalType


class TopicType(graphene.ObjectType):
    '''
        Defines a GraphQl Topic object.
    '''
    class Meta:
        interfaces = (graphene.relay.Node,)

    name = graphene.String()
    description = graphene.String()
    scope = graphene.String()
    creation_datetime = graphene.DateTime()
    portal = graphene.Field(
        PortalType
    )
    # TODO - add Tags
    articles = graphene.List(
        'civil_cultural.schema.ArticleType'
    )

    def resolve_portal(self, info, **kwargs):
        return self.topic_portal

    def resolve_articles(self, info, **kwargs):
        return self.article_set.all()


class TopicConnection(graphene.relay.Connection):
    class Meta:
        node = TopicType


class ArticleType(graphene.ObjectType):
    '''
        Defines an Article GraphQl object.
    '''
    class Meta:
        interfaces = (graphene.relay.Node,)

    title = graphene.String()
    publication_date = graphene.DateTime()
    post_author = graphene.Field(
        UserType,
        description='User that published the article.'
    )
    article_authors = graphene.List(
        graphene.String
    )
    abstract = graphene.String()
    body = graphene.String()
    pro_votes = graphene.Int()
    cons_votes = graphene.Int()
    references = graphene.String()
    questions = graphene.List(
        'civil_cultural.schema.QuestionType'
    )
    # TODO add tags
    # TODO reports
    # TODO similar suggestions

    def resolve_article_authors(self, info, **kwargs):
        return [author for author in self.article_authors.split(';')]

    def resolve_questions(self, info, **kwargs):
        return self.question_set.all()


class ArticleConnection(graphene.relay.Connection):
    class Meta:
        node = ArticleType


class QuestionType(graphene.ObjectType):
    '''
        Defines an Question GraphQl object.
        A question is related to a specific Article
    '''
    class Meta:
        interfaces = (graphene.relay.Node,)

    post_author = graphene.Field(
        UserType,
        description='User that published the question.'
    )
    text = graphene.String()
    pro_votes = graphene.Int()
    cons_votes = graphene.Int()
    publish_datetime = graphene.DateTime()
    article = graphene.Field('civil_cultural.schema.ArticleType')

    def resolve_article(self, info, **kwargs):
        return self.published_article


class QuestionConnection(graphene.relay.Connection):
    class Meta:
        node = QuestionType


class TagType(graphene.ObjectType):
    '''
        Defines an Tag GraphQl object.
        A tag is related to a specific subject matter.
        Can be used to filter and group objects.
    '''
    class Meta:
        interfaces = (graphene.relay.Node,)

    reference = graphene.String()


class TagConnection(graphene.relay.Connection):
    class Meta:
        node = TagType


class RuleType(graphene.ObjectType):
    '''
        Defines an Rule GraphQl object.
    '''
    class Meta:
        interfaces = (graphene.relay.Node,)

    description = graphene.String()
    creation_date = graphene.Date()
    portal = graphene.Field(PortalType)

    def resolve_portal(self, info, **kwargs):
        return self.portal_reference


class RuleConnection(graphene.relay.Connection):
    class Meta:
        node = RuleType


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
    pro_votes = graphene.Int(
        description='Positive votes this news has received.'
    )
    cons_votes = graphene.Int(
        description='Negative otes this news has received.'
    )
    publication_date = graphene.DateTime(
        description='Publish datetime.'
    )
    author = graphene.Field(
        UserType,
        description='News author.'
    )
    portal = graphene.Field(
        PortalType
    )

    def resolve_portal(self, info, **Kwargs):
        return self.portal_reference

    # @classmethod
    # def get_node(cls, info, id):
    #     return get_news(id=id)


class NewsConnection(graphene.relay.Connection):
    class Meta:
        node = NewsType


class SimilarSuggestionType(graphene.ObjectType):
    '''
        Defines an Similar Suggestion GraphQl object.
    '''
    class Meta:
        interfaces = (graphene.relay.Node,)

    post_author = graphene.Field(
        UserType
    )
    description = graphene.String()
    link = graphene.String(required=True)
    pro_votes = graphene.Int()
    cons_votes = graphene.Int()
    publish_datetime = graphene.DateTime()


class SimilarSuggestionConnection(graphene.relay.Connection):
    class Meta:
        node = SimilarSuggestionType


##########################################################################
# Schema QUERY
##########################################################################
class Query(object):
    '''
        Queries for civil_cultural.
    '''
    node = graphene.relay.Node.Field()

    portals = graphene.relay.ConnectionField(
        PortalConnection
    )

    # @access_required
    def resolve_portals(self, info, **kwargs):
        '''
            Returns all portals from civil cultural.
        '''
        return Portal.objects.all()

    topics = graphene.relay.ConnectionField(
        TopicConnection
    )

    # @access_required
    def resolve_topics(self, info, **kwargs):
        '''
            Returns all topics from civil cultural.
        '''
        return Topic.objects.all()

    articles = graphene.relay.ConnectionField(
        ArticleConnection
    )

    # @access_required
    def resolve_articles(self, info, **kwargs):
        return Article.objects.all()

    questions = graphene.relay.ConnectionField(
        QuestionConnection
    )

    # @access_required
    def resolve_questions(self, info, **kwargs):
        return Question.objects.all()

    tags = graphene.relay.ConnectionField(TagConnection) 

    # @access_required
    def resolve_tags(self, info, **kwargs):
        return Tag.objects.all()

    rules = graphene.relay.ConnectionField(RuleConnection)

    # @access_required
    def resolve_rules(self, info, **kwargs):
        return Rule.objects.all()

    similar_suggestions = graphene.relay.ConnectionField(
        SimilarSuggestionConnection
    )

    # @access_required
    def resolve_similar_suggestions(self, info, **kwargs):
        return SimilarSuggestion.objects.all()

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
        # filtros
        author = kwargs.get('author')
        title_contains = kwargs.get('title_contains')
        body_contains = kwargs.get('body_contains')

        # se fornecer filtro por autor, traz somente as noticias do autor
        if author:
            news = News.objects.filter(author=author)

        else:
            news = News.objects.all()

            if title_contains and body_contains:
                filtered_news = [
                    n for n in news if title_contains.lower() in n.title.lower()
                ]
                filtered_news += [
                    n for n in news if body_contains.lower() in n.body.lower()
                ]
                return filtered_news

            else:
                if title_contains and not body_contains:
                    news = [
                        n for n in news if title_contains.lower() in n.title.lower()
                    ]

                if body_contains and not title_contains:
                    news = [
                        n for n in news if body_contains.lower() in n.body.lower()
                    ]
        return news


##########################################################################
# MUTATION - Create
##########################################################################
class CreatePortal(graphene.relay.ClientIDMutation):
    '''
        Creates a portal
    '''
    portal = graphene.Field(
        PortalType,
        description='Created portal data response.'
    )

    class Input:
        name = graphene.String(description='Portal title.')

    # @access_required
    def mutate_and_get_payload(self, info, **_input):
        # captura dos inputs
        name = _input.get('name')

        try:
            portal = Portal.objects.create(
                name=name,
            )
            portal.save()

            return CreatePortal(portal)

        except Exception as exception:
            raise(exception)


class CreateTopic(graphene.relay.ClientIDMutation):
    '''
        Creates a topic
    '''
    topic = graphene.Field(
        TopicType,
        description='Created topic data response.'
    )

    class Input:
        name = graphene.String(
            required=True,
            description='Topic title.'
        )
        description = graphene.String(
            description='Topic description.'
        )
        scope = graphene.String(
            description='Topic focus and scope.'
        )
        portal = graphene.ID(
            required=True,
            description='Topic portal ID.'
        )

    # @access_required
    def mutate_and_get_payload(self, info, **_input):
        # captura dos inputs
        name = _input.get('name')
        description = _input.get('description', '')
        scope = _input.get('scope', '')
        portal_id = _input.get('portal')

        _, portal_id = from_global_id(portal_id)

        try:
            portal = Portal.objects.get(id=portal_id)
        except Portal.DoesNotExist:
            raise Exception(
                'Given portal does not exist!'
            )

        try:
            topic = Topic.objects.create(
                name=name,
                description=description,
                scope=scope,
                topic_portal=portal
            )
            topic.save()
            return CreateTopic(topic)

        except Exception as exception:
            raise(exception)


class CreateArticle(graphene.relay.ClientIDMutation):
    '''
        Creates an Article
    '''
    article = graphene.Field(
        ArticleType,
        description='Created article data response.'
    )

    class Input:
        title = graphene.String(
            requried=True,
            description='Article title.'
        )
        article_authors = graphene.List(
            graphene.String,
            required=True
        )
        abstract = graphene.String()
        body = graphene.String(
            requried=True
        )
        references = graphene.String(
            required=True
        )
        topic = graphene.ID(
            required=True
        )

    @access_required
    def mutate_and_get_payload(self, info, **_input):
        # captura dos inputs
        title = _input.get('title')
        article_authors = _input.get('article_authors', '')
        abstract = _input.get('abstract')
        body = _input.get('body')
        references = _input.get('references')
        topic = _input.get('topic')
        _, topic_id = from_global_id(topic)

        authors = ';'.join(author for author in article_authors)

        # identifica o usuario
        user = info.context.user

        try:
            topic = Topic.objects.get(
                id=topic_id
            )
        except Topic.DoesNotExist:
            raise Exception('Given topic does not exists.')

        try:
            article = Article.objects.create(
                title=title,
                abstract=abstract,
                body=body,
                references=references,
                post_author=user,
                article_authors=authors,
                published_topic=topic
            )
            article.save()

            return CreateArticle(article)

        except Exception as exception:
            raise(exception)


class CreateQuestion(graphene.relay.ClientIDMutation):
    '''
        Creates an Question on an Article
    '''
    question = graphene.Field(
        QuestionType,
        description='Created article data response.'
    )

    class Input:
        text = graphene.String(
            requried=True,
            description='Question text.'
        )
        article = graphene.ID(
            required=True
        )

    @access_required
    def mutate_and_get_payload(self, info, **_input):
        # captura dos inputs
        text = _input.get('text')
        article = _input.get('article')
        _, article_id = from_global_id(article)

        # identifica o usuario
        user = info.context.user

        try:
            article = Article.objects.get(
                id=article_id
            )
        except Article.DoesNotExist:
            raise Exception('Given article does not exists.')

        try:
            question = Question.objects.create(
                text=text,
                post_author=user,
                published_article=article
            )
            question.save()

            return CreateQuestion(question)

        except Exception as exception:
            raise(exception)


class CreateTag(graphene.relay.ClientIDMutation):
    '''
        Creates a Tag
    '''
    tag = graphene.Field(
        TagType,
        description='Created Tag data.'
    )

    class Input:
        reference = graphene.String(
            required=True
        )

    # @access_required
    def mutate_and_get_payload(self, info, **_input):
        reference = _input.get('reference')

        try:
            tag = Tag.objects.create(
                reference=reference
            )
            tag.save()
            return CreateTag(tag)

        # TODO - handle the right exception when the time comes
        except Exception:    
            raise Exception(
                "Impossible to create this tag. \
                Maybe this reference already exists."
            )


class CreateRule(graphene.relay.ClientIDMutation):
    '''
        Creates a Rule
    '''
    rule = graphene.Field(RuleType)

    class Input:
        description = graphene.Field(
            graphene.String,
            required=True
        )
        portal = graphene.ID(
            required=True
        )

    # @access_required
    def mutate_and_get_payload(self, info, **_input):
        description = _input.get('description')
        portal_id = _input.get('portal')
        _, portal_id = from_global_id(portal_id)

        try:
            portal = Portal.objects.get(id=portal_id)
        except Portal.DoesNotExist:
            raise Exception('The given Portal does not exist.')

        try:
            rule = Rule.objects.create(
                description=description,
                portal_reference=portal
            )
            rule.save()
            return CreateRule(rule)
        except Exception:    
            raise Exception(
                "Impossible to create this rule. \
                Maybe it already exists."
            )


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
        portal = graphene.ID(
            required=True,
            description='Topic portal ID.'
        )

    @access_required
    def mutate_and_get_payload(self, info, **_input):
        # captura dos inputs
        title = _input.get('title')
        body = _input.get('body')
        portal_id = _input.get('portal')
        _, portal_id = from_global_id(portal_id)

        try:
            portal = Portal.objects.get(id=portal_id)

        except Portal.DoesNotExist:
            raise Exception('The given portal does not exist.')

        try:
            news = News.objects.create(
                title=title,
                body=body,
                author=info.context.user,
                portal_reference=portal
            )
            news.save()

            return CreateNews(news)

        except Exception as exception:
            raise(exception)


##########################################################################
# MUTATION - Update
##########################################################################
class UpdateNews(graphene.relay.ClientIDMutation):
    '''
        Updates a published News.
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


##########################################################################
# MUTATION - Delete
##########################################################################
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


##########################################################################
# Schema Mutation
##########################################################################
class Mutation:
    # Create
    create_portal = CreatePortal.Field()
    create_topic = CreateTopic.Field()
    create_article = CreateArticle.Field()
    create_question = CreateQuestion.Field()
    create_tag = CreateTag.Field()
    create_rule = CreateRule.Field()
    ceate_news = CreateNews.Field()

    # Update
    update_news = UpdateNews.Field()

    # Delete
    delete_news = DeleteNews.Field()
