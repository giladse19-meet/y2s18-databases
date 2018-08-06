from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(subject_id, student, topic, artical, rating):
	topic_info = Knowledge(
		subject_id = subject_id,
		student = student,
		topic = topic,
		artical = artical,
		rating = rating)
	session.add(topic_info)
	session.commit()

#add_article(1, "Gilad", "robotics" , "robotics", 10)
#add_articale(2, "yair", "basketball", "basketball", 8)

def query_all_articles():
	print(session.query(Knowledge).all())

def query_article_by_topic():
	print(session.query(Knowledge).filter_by(topic=topic))

def delete_article_by_topic():
	pass

def delete_all_articles():
	ready = session.query(Knowledge).all()
	for i in range(len(ready)):
		ready[i].delete()
	session.commit()
delete_all_articles()
def edit_article_rating():
	pass
