from app import db
from datetime import datetime
import re


def slugify(s):
	pattern = r'[^\w+]'
	return re.sub(pattern, '-', s)


class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(147))
	slug = db.Column(db.String(140), unique=True)
	body = db.Column(db.Text)
	created = db.Column(db.DateTime, default=datetime.now())

	def __init__(self, *args, **kwargs):
		super(Post, self).__init__(*args, **kwargs)
		self.generate_slug()

	def generate_slug(self):
		if self.title:
			self.slug = slugify(self.title)

	def __repr__(self):
		return '<Post id: {}, title: {}>'.format(self.id, self.title)


class Tag(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100))
	slug = db.Column(db.String(100))

	def __init__(self, *args, **kwargs):
		super(Tag, self).__init__(*args, **kwargs)
		self.slug = slugify(self.name)
	
	def __repr__(self):
		return '<Tag id: {}, name: {}>'.format(self.id, self.name)