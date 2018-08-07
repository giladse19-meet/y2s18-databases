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



def qurey_by_rating(threshold):
	list_t = query_all_articles()
	articales_low_rating = []
	for n in list_t:
		current = session.n.rating
		if current < threshold:
			articales_low_rating.append(n)
	return(articales_low_rating)



def delete_article_by_topic():
	I_delete = input("what topic do you want to delete?")
	want = session.query(Knowledge).filter_by(topic=I_delete)
	session.delete(want)

def delete_all_articles():
	list_s = query_all_articles()
	for i in range(len(list_s)):
		ready = session.query(Knowledge).first()
		session.delete(ready)
	session.commit()

def edit_article_rating(updated_rating, articale_title):
	edit = session.query(Knowledge).filter_by(topic = articale_title).all()
	for t in edit:
		t.rating = updated_rating
	session.commit()
edit_article_rating(9, "robotics")
print(query_all_articles())	
	
