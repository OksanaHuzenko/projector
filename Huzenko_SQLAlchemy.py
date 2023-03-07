#Add models for Car and Company from previous lessons using SQLAlchemy.

from sqlalchemy import create_engine, ForeignKey, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Company(Base):
    __tablename__ = 'company'

    company_id = Column(Integer, primary_key=True)
    company_name = Column()
    company_adress = Column(String)


class Car3(Base):
    __tablename__ = 'car3'

    car_id = Column(Integer, primary_key=True)
    reg_number = Column(String)
    car_company_id = mapped_column(Integer, ForeignKey(Company.company_id))

DATABASE_URI = 'postgresql://{user}:{password}@{host}:{port}/{database}'

import engine from SQLAlchemy_pass

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

#In your script, add a couple of rows to each table (also using ORM).

c1 = Company()
c1.company_id = 1
c1.company_name = 'Liubava'
c1.company_adress = 'Kyiv, Zhytomyrska Str'
session.add(c2)

c2 = Company()
c2.company_id = 2
c2.company_name = 'TOV Apple'
c2.company_adress = 'Kyiv, Shevchenka Avenue'
session.add(c2)

session.commit()

car1 = Car3()
car1.car_id = 1
car1.reg_number = ('AA 1111 BB')
car1.car_company_id = 1
session.add(car1)

session.commit()

car2 = Car3()
car2.car_id = '2'
car2.reg_number = 'AA 2222 BB'
car2.car_company_id = 2
session.add(car2)

session.commit()

car3 = Car3()
car3.car_id = 3
car3.reg_number = 'AA 3333 BB'
car3.car_company_id = 1
session.add(car3)

session.commit()

#Print the answer for the following questiong (make query usnig ORM): how many cars does the company ‘Liubava’ rent?.

Liubava_cars = session.query(Car3).join(Company, Car3.car_company_id == Company.company_id).filter(Company.company_name == 'Liubava').count()
print(Liubava_cars)

session.close()
