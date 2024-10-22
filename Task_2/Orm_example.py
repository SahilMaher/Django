
from sqlalchemy.orm import declarative_base,sessionmaker
from sqlalchemy import Column,Integer,String,create_engine
import os

Base=declarative_base()



class MyObject(Base):
    __tablename__='my_objects'
    id=Column(Integer,primary_key=True)
    name=Column(String)

engine=create_engine('sqlite:///mydatabase.db')

Base.metadata.create_all(engine)

Session=sessionmaker(bind=engine)

def add_sample_data(session):
    if session.query(MyObject).count()==0:
        sample_data=[
            MyObject(id=1,name="Sahil"),
            MyObject(id=2,name="Ajay"),
            MyObject(id=3,name="Rahul"),
            MyObject(id=4,name="Vijay"),
        ]
        session.bulk_save_objects(sample_data)
        session.commit()
        print("Sample Data Added")
    else:
        print("Data Already Exist")

def get_even_objects(session):
    return session.query(MyObject).filter(MyObject.id%2==0).all()

def edit_Object(session,object_id,new_name):
    obj=session.query(MyObject).filter(MyObject.id==object_id).first()
    if obj is None:
        return "Object Not Found"
    if obj.id % 2!=0:
        return "Can't Edit Odd Id"
    obj.name=new_name
    session.commit()
    return "Data Updated Susscesfully"

if __name__ =="__main__":
    session=Session()
    if os.path.exists("mydatabase.db"):
        try:
            session.close()
            os.remove("mydatabase.db")
            print("Data Base Removed")
        except Exception as e:
            print(f"Exception Occured:{e}")
    session=Session()
    try:
        add_sample_data(session)
        even_objects=get_even_objects(session)
        print("Even Id's")
        for data in even_objects:
            print(f"ID:{data.id}-Name:{data.name}")
            result=edit_Object(session,2,"Update Object 2")
            print(result)
            result=edit_Object(session,3,"Udate Object 3")
            print(result)
            update_even_objects=get_even_objects(session)
            print("Update Even Objects")
            for obj in update_even_objects:
                print(f"ID:{obj.id}-Name:{obj.name}")
    finally:
        session.close()