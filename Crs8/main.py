########### Exercise 1 ###########
import mysql.connector
def get_airport_by_indent(code):
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="114514",
    database="flight_game"
  )
  mycursor = mydb.cursor(dictionary=True)
  mycursor.execute(f"SELECT name,municipality FROM airport where ident = '{code}'")
  myresult = mycursor.fetchone()
  print(myresult['name'],";", myresult['municipality'])

code = input("Enter the ICAO code of an airport: ")
get_airport_by_indent(code)
########### Exercise 2 ###########
def get_airport_by_area(code):
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="114514",
    database="flight_game"
  )
  mycursor = mydb.cursor(dictionary=True)
  mycursor.execute(f"SELECT name,type FROM airport where iso_country = '{code}' order by type")
  myresult = mycursor.fetchall()
  for i in myresult:
    print(i['name'],";",i['type'])

code = input("Enter the country code of an airport: ")
get_airport_by_area(code)
########### Exercise 3 ###########
from geopy import distance, location


def get_location_by_ident(code):
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="114514",
    database="flight_game"
  )
  mycursor = mydb.cursor(dictionary=True)
  mycursor.execute(f"SELECT latitude_deg,longitude_deg FROM airport where ident = '{code}'")
  myresult = mycursor.fetchone()
  latitude = myresult['latitude_deg']
  longitude = myresult['longitude_deg']
  airport = (latitude, longitude)
  return airport
code1 = input("Enter the country code of the first airport: ")
code2 = input("Enter the country code of the second airport: ")
airport1=get_location_by_ident(code1)
airport2=get_location_by_ident(code2)
print(distance.distance(airport1,airport2).km)