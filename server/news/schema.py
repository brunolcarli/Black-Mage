import graphene

class NewsType(graphene.ObjectType):
    '''Representação de uma Noticia'''
    title = graphene.String(description='News title.')
    body = graphene.String(description='News main content.')
    votes = graphene.Int(description='Votes this news has received.')
    publication_date = graphene.DateTime(description='Publish datetime.')
