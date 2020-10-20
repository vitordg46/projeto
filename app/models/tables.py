from app import db
import peewee


class BaseModel(peewee.Model):

  class Meta:
    database = db


class User(BaseModel):
	
	name = peewee.CharField(unique=True)
	email = peewee.CharField(unique=True)
	password = peewee.CharField()

	@property
	def is_authenticated(self):
		return True

	@property
	def is_active(self):
		return True
	
	@property
	def is_anonymous(self):
		return False
	
	def get_id(self):
		return str(self.id)


class Mascara(BaseModel):

	title = peewee.CharField()
	about = peewee.TextField()
	price = peewee.CharField()