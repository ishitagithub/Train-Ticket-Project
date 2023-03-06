from flask import Flask, render_template,request
import datetime
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
    mycur.execute("select * from ticket_book")
    print(tno)
    for i in mycur:
        print(i[3])
        if i[3]==int(tno) and str(i[6])==date:
            print("equal")
            mycur.execute("delete from ticket_book where train_no="+tno+" limit 1")
            mydb.commit()
            return render_template('pass.html',fname=fname,lname=lname,tname=tname,tno=tno,email=email,tel=tel,date=date)
    return render_template('pass2.html',fname=fname,lname=lname,tname=tname,tno=tno,email=email,tel=tel,date=date)
if __name__ == '__main__': 
    app.run(debug=True)
