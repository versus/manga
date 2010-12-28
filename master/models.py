from django.db import models

# Create your models here.
from mongoengine import *
import datetime

class User(Document):
	name = StringField()
	
	def __unicode__(self): 
		return self.name

class Comment(EmbeddedDocument):
	content = StringField()
	author = ReferenceField(User)

class Page(Document):
	title = StringField(max_length=200, required=True)
	date_modified = DateTimeField(default=datetime.datetime.now)
	comments = ListField(EmbeddedDocumentField(Comment))
	author = ReferenceField(User)
	
	def __unicode__(self):
		return '%s %s' % (self.title, self.author.name)