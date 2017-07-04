import time
import datetime
import json


class DBObject(object):
    """This class defines how objects in the mongoDB should be represented."""

    def __init__(
            self,
            classes=[],
            type='',
            meta={}
            ):
        self.created = datetime.datetime.now()
        self.updated = datetime.datetime.now()
        self.classes = classes
        self.type = type
        self.meta = meta
        self.structure = '{}{}'.format('#', self.__class__.__name__)


    def export(self):
        """This function exports the object as a dict. This is used when
        putting an object in the database."""

        return self.__dict__


class Page(DBObject):
    def __init__(
            self,
            page_route=None,
            page_template=None,
            editables=None,
            *args,
            **kwargs
            ):
        DBObject.__init__(self, *args, **kwargs)
        self.page_route = page_route
        self.page_template = page_template
        self.editables = editables

class Option(DBObject):
    def __init__(
            self,
            key=None,
            value=None,
            *args,
            **kwargs
            ):
        DBObject.__init__(self, *args, **kwargs)
        self.key = key
        self.value = value

class ThemeDBOption(DBObject):
    def __init__(
            self,
            key=None,
            value=None,
            *args,
            **kwargs
            ):
        DBObject.__init__(self, *args, **kwargs)
        self.key = key
        self.value = value

class User(DBObject):
    def __init__(
            self,
            username=None,
            password=None,
            *args,
            **kwargs
            ):
        DBObject.__init__(self, *args, **kwargs)
        self.username = username
        self.password = password
