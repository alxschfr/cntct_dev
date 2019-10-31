# cntct_dev
python3 program to store and manipulate personal contact information for current contacts as
class-objects in Postgresql using SQLAlchemy and Flask. Want to learn python and familiarize myself
with the concept of object-oriented programming. So mostly an exercise up until now. Based on
following tutorials (and tons of SO answers):
- https://scotch.io/tutorials/authentication-and-authorization-with-flask-login
- https://www.codementor.io/garethdwyer/building-a-crud-application-with-flask-and-sqlalchemy-dm3wv7yu2
- https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database
- https://hackersandslackers.com/demystifying-flask-application-factory/

You can find an upp and running deploy on heroku via https://cntct.herokuapp.com. Because if it's the
heroku free plan, the dyno has to be started again if it's the first request for half an hour. That
results in an initial lag in site display. Once the dyno is running response time is quite fast