from flask import Flask,render_template, jsonify
from flask import request, redirect, url_for
from flask_mysqldb import MySQL
import MySQLdb.cursors

 
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'geeks4geeks'
mysql = MySQL(app)


@app.route('/')
def index():
    cursor=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("select * from Inventory")
    items=cursor.fetchall()
    cursor.close()
    return render_template('index.html',items=items)

@app.route("/additem")
def add_item():
    return render_template("create_item.html")

@app.route("/postitem",methods=['POST'])
def post_item():
    cursor=mysql.connection.cursor(MySQLdb.cursors.DictCursor)

    sql = "INSERT INTO Inventory (Name, Description, Quantity, Price) VALUES (%s, %s, %s, %s)"
    val = (request.form['name'], request.form['description'], request.form['quantity'], request.form['price'])
    cursor.execute(sql, val)
    mysql.connection.commit()
    return redirect(url_for("index"))

@app.route("/deleteitem<item_id>")
def delete_item(item_id):
    cursor=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    sql = "DELETE FROM Inventory WHERE Id = %s"
    id = (item_id,)
    cursor.execute(sql,id)
    mysql.connection.commit()
    return redirect(url_for("index"))

@app.route("/updateitem<item_id>")
def update_item(item_id):
    cursor=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    sql = "Select * FROM Inventory WHERE Id = %s"
    id = (item_id,)
    cursor.execute(sql,id)
    item=cursor.fetchall()
    cursor.close()
    return render_template("update_item.html",item=item[0])

@app.route("/ajaxlivesearch",methods=["POST"])
def ajaxlivesearch():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        search_word = request.form['search']
        if search_word == '':
            query = "SELECT * from Inventory"
            cur.execute(query)
            items = cur.fetchall()
        else:    
            query = "SELECT * from Inventory WHERE Name LIKE '%{}%' OR Description LIKE '%{}%' ORDER BY id DESC LIMIT 20".format(search_word,search_word)
            cur.execute(query)
            items= cur.fetchall()
    else:
        print(request.method)
        
    return jsonify({'htmlresponse': render_template('response.html', items=items)})

@app.route("/postupdate",methods=['POST'])
def post_update():
    cursor=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    id=request.form['id']
    sql = "UPDATE Inventory SET Name = %s, Description = %s, Quantity = %s, Price = %s WHERE Id = %s"
    val = (request.form['name'], request.form['description'], request.form['quantity'], request.form['price'],id)
    cursor.execute(sql, val)
    mysql.connection.commit()
    return redirect(url_for("index"))

if __name__=='__main__':
    app.run()
#import webbrowser

#webbrowser.open('C:/Users/dell/Desktop/Project/index.html', new=2)