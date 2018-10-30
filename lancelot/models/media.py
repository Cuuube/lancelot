# -*- coding: utf8 -*-

from mongoengine import connect, Document, StringField, IntField

class Media(Document):
    media_name         = StringField(required=True)
    media_snapshot     = StringField(required=True)
    media_description  = StringField()
    media_link         = StringField(required=True)
    played_count       = IntField()   
    likes              = IntField()   
    upload_time        = IntField()   
    uploader           = StringField()
    uploader_avatar    = StringField()
    uploader_spaceLink = StringField()
    check_time         = IntField(required=True)   
    channel            = StringField(required=True)
    from_website       = StringField(required=True)
    original_id       = StringField()

    # meta = {'db_alias': 'bookstore'}

    @classmethod
    def insert(cls, **kwargs):
        original_id = kwargs.get('original_id', None)
        # print('-------!!!', kwargs, original_id)

        foundItem = cls.objects(original_id=original_id).first()

        print foundItem

        if original_id:
            document_data = kwargs
            # {
            #     'name': kwargs.get('name'),
            #     'pages': kwargs.get('pages'),
            #     'price': kwargs.get('price'),
            #     'author': kwargs.get('author'),
            #     'url': kwargs.get('url'),
            # }
            if foundItem:
                # update
                foundItem.update(**document_data)
            else:
                # insert
                bs = cls(**document_data)
                bs.save()

        

if __name__ == '__main__':
    connect('project1', host='mongodb://localhost:27017/watchwhat')

    # Media.write()