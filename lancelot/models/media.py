# -*- coding: utf8 -*-

from mongoengine import connect, Document, StringField, IntField

class Media(Document):
    MediaName         = StringField(required=True)
    MediaSnapshot     = StringField(required=True)
    MediaDescription  = StringField()
    MediaLink         = StringField(required=True)
    PlayedCount       = IntField()   
    Likes             = IntField()   
    UploadTime        = IntField()   
    Uploader          = StringField()
    UploaderAvatar    = StringField()
    UploaderSpaceLink = StringField()
    CheckTime         = IntField(required=True)   
    channel           = StringField(required=True)
    FromWebsite       = StringField(required=True)

    # meta = {'db_alias': 'bookstore'}

    @classmethod
    def insert(cls, **kwargs):
        pass

    # @classmethod
    # def write(cls, **kwargs):
        # name = kwargs.get('name', None)
        # print('-------!!!', kwargs, name)


        # foundItem = Bookstore.objects(name=name).first()

        # print foundItem

        # if name:
        #     document_data = {
        #         'name': kwargs.get('name'),
        #         'pages': kwargs.get('pages'),
        #         'price': kwargs.get('price'),
        #         'author': kwargs.get('author'),
        #         'url': kwargs.get('url'),
        #     }
        #     if foundItem:
        #         # update
        #         foundItem.update(**document_data)
        #     else:
        #         # insert
        #         bs = Bookstore(**document_data)
        #         bs.save()

        

if __name__ == '__main__':
    connect('project1', host='mongodb://localhost:27017/watchwhat')

    # Media.write()