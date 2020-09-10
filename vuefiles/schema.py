import graphene
from files.schema import FileQuery, FileMutation


class Query(FileQuery, graphene.ObjectType):
    pass


class Mutation(FileMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)