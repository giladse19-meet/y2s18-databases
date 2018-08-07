from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(student, topic, articale, rating):
	topic_info = Knowledge(
		student = student,
		topic = topic,
		articale = articale,
		rating = rating)
	session.add(topic_info)
	session.commit()

#add_article("Gilad", "robotics" , "robotics", 10)
#add_article("yair", "basketball", "basketball", 5)

def query_all_articles():
	all_articales = session.query(Knowledge).all()
	return(all_articales)

def query_article_by_topic():
	I_want = input("what do you learn about?")
	print(session.query(Knowledge).filter_by(topic=I_want).first())

articales_low_rating = []

def qurey_by_rating(threshold):
	list_d = query_all_articles()
	for i in range(len(list_d)):
		if list_d[i] < threshold:
			articales_low_rating.append(list_d[i])
	return(articales_low_rating)

print(qurey_by_rating(7))

def delete_article_by_topic():
	pass

def delete_all_articles():
	list_s = query_all_articles()
	for i in range(len(list_s)):
		ready = session.query(Knowledge).first()
		session.delete(ready)
	session.commit()
def edit_article_rating():
	pass
