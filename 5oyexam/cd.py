import psycopg2
from psycopg2 import sql

host ='localhost'
database='n48'
user ='postgres'
password='123'


try:
    connection =psycopg2.connect(
        host=host,
        database= database,
        user = user,
        password=password

    )

    cursor = connection.cursor()\


    create_table_query ='''
    create table product (
    
    
    
    '''