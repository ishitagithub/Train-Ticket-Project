from flask import Flask, render_template 
 
app = Flask(_name_) 
 
@app.route('/') 
def index(): 
    return render_template("C:\Users\HP\OneDrive\Desktop\Vinhack train project\website.html")pip 
 
if _name_ == '_main_':
    app.run()
