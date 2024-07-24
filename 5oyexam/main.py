#barat sho'rayev
#1-savol
import psycopg2
from psycopg2 import sql


host = "localhost"
database = "n48"
user = "postgres"
password = "123"


try:
    connection = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password
    )
    cursor = connection.cursor()

    create_table_query = '''
    create table product (
        id serial primary key,
        name varchar(255) not null,
        price decimal(10, 2) not null,
        color varchar(50),
        image  bytea
    );
    '''
    cursor.execute(create_table_query)
    connection.commit()


except (Exception, psycopg2.Error) as error:
    print("product jadvali allaqacho yaratilgan", error)
finally:
    if connection:
        cursor.close()
        connection.close()

#2-savol
def update_product():
    select_all_products()
    _id = (input(" 1:"))
    name = str(input(" telefon:"))
    price = int(input("  1.200:"))
    color = str(" black:")
    image = str("product url:")
    update_query = 'update product set name = %s, price = %s,color =%S,image =%s where id = %s;'
    update_params = (_id,name,price,color,image)
    curr.execute(update_query,update_params)
    conn.commit()

#3-savol
class Alphabet:
    def __init__(self):
        self.letters  ='abcdefghijklmnopqrtstuvwxyz'
        self.index =0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.letters):
            letter = self.letters[self.index]
            self.index += 1
            return letter
        else:
            raise StopIteration

alphabet = Alphabet()
for letter in alphabet:
    print(letter)

#4-savol
import threading
import time

def print_numbers():
    for i in range(1, 6):
        print(i)
        time.sleep(1)

def print_letters():
    letters = "abcde"
    for letter in letters:
        print(letter)
        time.sleep(1)

thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

thread1.start()
thread2.start()

thread1.join()
thread2.join()


#5-savol
class Product:
    def __init__(self, name, price, color, image):
        self.name = name
        self.price = price
        self.color = color
        self.image = image

    def save(self):
        try:
            connection = psycopg2.connect(
                host="localhost",
                database="n48",
                user="postgres",
                password="123"
            )
            cursor = connection.cursor()

            insert_query = '''
             insert into product (name, price, color, image) 
             values (%s, %s, %s, %s)
            '''
            cursor.execute(insert_query, (self.name, self.price, self.color, self.image))
            connection.commit()


        except (Exception, psycopg2.Error) as error:
            print("product jadvali bor", error)
        finally:
            if connection:
                cursor.close()
                connection.close()

product = Product('samsung', 1.200, 'black', None)
product = Product('iphone15', 1.500, 'white', None)
product = Product('samsungs24', 1.600, 'black', None)
product = Product('iphone14pro', 1.100, 'black', None)
product = Product('televizor', 1.200, 'white', None)
product = Product('noutbook', 1.500, 'black', None)
product.save()



#6-savol
class DbConnect:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = None
        self.cursor = None

    def __enter__(self):
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            self.cursor = self.connection.cursor()
            return self.connection, self.cursor
        except Exception as error:
            print("xatolik yuz berdi", error)
            raise

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        if exc_type or exc_val or exc_tb:
            print("xatolik:", exc_type, exc_val)
        return False

with DbConnect("localhost", "n48", "postgres", "123") as (conn, cur):
    try:
        cur.execute("select * from Product")
        products = cur.fetchall()
        for product in products:
            print(product)
    except Exception as e:
        print("xatolik yuz berdi:", e)

#8-misol









