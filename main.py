from flask import Flask, render_template ,request,redirect,session
import os
import pymysql

app = Flask(__name__,template_folder="templates")
app.secret_key=os.urandom(24)

conn=pymysql.connect(host="localhost",user="root",password="",database="login")
Cursor=conn.cursor()

@app.route('/')
def Login():
    return render_template('login_1.html')

@app.route('/register_1.html')
def register():
    return render_template('register_1.html')  

@app.route('/logout')
def logout():
    session.pop('user_Id')
    return redirect('/')

@app.route('/login_1.html')
def login():
    return render_template('login_1.html')

@app.route('/welcome.html')
def home():
    if 'user_Id' in session:
            return render_template('welcome.html')  
    else:
        return redirect('/')    


#Main Pages:-

@app.route('/language.html')
def language():
    return render_template('language.html') 

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/companies.html')
def companies():
    return render_template('companies.html')

@app.route('/dsa.html')
def dsa():
    return render_template('dsa.html')


#Languages page:

@app.route('/languages/cpp.html')
def cpp():
    return render_template('languages/cpp.html')

@app.route('/languages/java.html')
def java():
    return render_template('languages/java.html')

@app.route('/languages/python.html')
def phython():
    return render_template('languages/python.html')

@app.route('/languages/js.html')
def js():
    return render_template('languages/js.html')

@app.route('/languages/php.html')
def php():
    return render_template('languages/php.html')

@app.route('/#')
def hash():
    return render_template('language.html')


#Companies Pages:
@app.route('/Companies/ibm.html')
def ibm():
    return render_template('Companies/ibm.html')

@app.route('/Companies/wipro.html')
def wipro():
    return render_template('Companies/wipro.html')

@app.route('/Companies/infosys.html')
def infosys():
    return render_template('Companies/infosys.html')

@app.route('/Companies/tcs.html')
def tcs():
    return render_template('Companies/tcs.html')

@app.route('/Companies/microsoft.html')
def microsoft():
    return render_template('companies.html')

@app.route('/Companies/microsoft.html')
def amazon():
    return render_template('companies.html')
   


 
@app.route('/login_validation', methods=['POST'])
def login_validation():
    email=request.form.get('email')
    password=request.form.get('password')

    Cursor.execute(""" SELECT * FROM `pal` WHERE `email` LIKE '{}' AND `password` LIKE '{}'  """.format(email,password))
    pal = Cursor.fetchall()
    if len(pal)>0:
        session['user_Id']=pal[0][0]
        return redirect('/welcome.html')
    else:
        return render_template('/')


@app.route('/add_user', methods=['POST'])
def add_user():
    name=request.form.get('name')
    email=request.form.get('email')
    password=request.form.get('password')

    Cursor.execute(""" INSERT INTO `pal` (`user_Id`,`name`,`email`,`password`) VALUES (NULL,'{}','{}','{}')  """.format(name,email,password))
    conn.commit()

    Cursor.execute(""" SELECT * FROM `pal` WHERE `email` LIKE '{}' """.format(email))
    myuser = Cursor.fetchall()
    session['user_Id'] = myuser[0][0]
    return redirect("/login_1.html")



@app.route('/contact_us', methods=['POST'])
def contact_us():
    name=request.form.get('name')
    email=request.form.get('email')
    message=request.form.get('message')

    Cursor.execute(""" INSERT INTO `contact_us` (`user_Id`,`name`,`email`,`message`) VALUES (NULL,'{}','{}','{}')  """.format(name,email,message))
    conn.commit()

    return redirect("/contact.html")


app.run(debug=True)