from flask import Flask, render_template,request
 
app = Flask(__name__) 
 
@app.route('/') 
def index(): 
    return render_template("website.html") 
@app.route('/',methods=['POST'])
def getvalue():
    fname=request.form['fname']
    lname=request.form['lname']
    tname=request.form['tname']
    tno=request.form['tno']
    email=request.form['email']
    tel=request.form['tel']
    date=request.form['date']
    import mysql.connector
    mydb=mysql.connector.connect(user='root',
                                 host='localhost',
                                 password='Ishita.mysql')
    mycur=mydb.cursor(buffered=True)
    mycur.execute("use vinhackathon")
    v="insert into ticket_book values(%s,%s,%s,%s,%s,%s,%s)"
    data=(fname,lname,tname,tno,email,tel,date)
    mycur.execute(v,data)
    mydb.commit()
    return render_template('pass.html',fname=fname,lname=lname,tname=tname,tno=tno,email=email,tel=tel,date=date)
if __name__ == '__main__': 
    app.run(debug=True)
