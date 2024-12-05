########### Exercise 1 ###########
from flask import Flask, request

app = Flask(__name__)
@app.route('/prime_number/<text>')
def calculate_sum(text):
    args = request.args
    number = int(text)
    results = {}
    results['Number'] = number
    results["isPrime"] = True
    for i in range(2, number):
        if number % i == 0:
            results["isPrime"] = False
    return str(results)

########### Exercise 2 ###########
import mysql.connector
@app.route('/airport/<ICAO>')
def calculate_num(ICAO):
    args = request.args

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="114514",
        database="flight_game"
    )
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute(f"select ident as ICAO,name as Name,municipality as Location from airport where ident = '{ICAO}'")
    myresult = mycursor.fetchone()
    return myresult

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)