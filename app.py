import flask,sqlitecloud,flask_session,os
from flask import render_template, request, redirect, session, url_for, send_from_directory
from flask_session import Session


# --------- Import Environmental Variables ----------
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("API_KEY")
admin = os.getenv("USERNAME")
admin_pword = os.getenv("PASSWORD")


app = flask.Flask(__name__)

# ---------------- Configuration ----------------
app.config["SESSION_PERMANENT"] = False     # Sessions expire when browser closes
app.config["SESSION_TYPE"] = "filesystem"     # Store session data on the filesystem
Session(app)

# ---------------- Routes ----------------
# Learnt to use redirect, so the url reflects the page properly
# Learnt to use Session/session to hold important info 


@app.route('/')
def index():
    if not session.get("user"):
        return redirect(url_for('login'))
    return render_template("Home.html",user=session["user"])

@app.route('/login', methods=["GET","POST"])
def login():
    if request.method == 'GET':
        return render_template("Login.html")
    if request.method == 'POST':
        if 'user' in request.form and 'Pword' in request.form:
            session["user"] = request.form['user']
            Pword = request.form['Pword']
            if session["user"] == admin and Pword == admin_pword:
                return redirect(url_for('index')) 
            return redirect(url_for("login",invalid=True))


### HOLY SHIT MY API KEY IS VISIBLE FOR EVERYONE TO SEE 
### Fixed the sensitive issue

@app.route('/library')
def database():
    conn = sqlitecloud.connect(API_KEY)
    cursor = conn.execute('SELECT * FROM Friends;')
    friends = cursor.fetchall()
    conn.close()
    return render_template('Data.html',friends=friends)

@app.route('/mod',methods=["GET","POST"])
def mod_data():
    conn = sqlitecloud.connect(API_KEY)
    if request.method == "POST" and "friend" in request.form and "field" in request.form:
        mod_friend = request.form["friend"] #Can they inject their own options into the dropdown list? Possible XSS vunerability
        mod_field = request.form["field"]
        new_data = request.form["u_input"]
        conn.execute("UPDATE Friends SET {} = ? WHERE name = ?".format(mod_field),(new_data,mod_friend)) # Should i change the inserting of field names?
        conn.commit()
        conn.close()
        return redirect(url_for("index"))
    cursor = conn.execute('SELECT * FROM Friends;') #Change * to name?
    friends = cursor.fetchall()
    conn.close()
    return render_template("mod_data.html",friends=friends)

@app.route('/add',methods=["GET","POST"])
def add_data():
    if request.method == "POST" and 'Submit' in request.form:
        
        # ------------------ Process new Friend data ------------------
        fields = ['Name','DOB','Educational_bg','Meet','Likes','Dislikes','Hobbies','Add_info','Relationship','CAA']
        new_friend = {}
        form_data = request.form   
        for field in fields:
            print(field,form_data[field])
            if not form_data[field] == '':
                new_friend[field] = form_data[field]
            else:
                print(field,"not filled")
                new_friend[field] = None
                
        conn = sqlitecloud.connect(API_KEY)
        conn.execute("INSERT INTO Friends VALUES (?,?,?,?,?,?,?,?,?,?)",tuple(new_friend.values())) 
        conn.commit()
        conn.close()
        
    return render_template("add_data.html")

@app.route('/delete',methods=["GET","POST"])
def delete_data():
    conn = sqlitecloud.connect(API_KEY)
    if request.method == "POST" and "friend" in request.form:
        delete_friend = request.form["friend"] #Can they inject their own options into the dropdown list? Possible XSS vunerability
        conn.execute("DELETE FROM Friends WHERE name = ?",(delete_friend,)) # Should i change the inserting of field names?
        conn.commit()
        conn.close()
        return redirect(url_for("index"))
    cursor = conn.execute('SELECT Name FROM Friends;') 
    friends = [list(friend).pop() for friend in cursor.fetchall()]
    print(friends)
    conn.close()
    return render_template("delete_data.html",friends=friends)

@app.route("/image/<filename>")
def get_img(filename):
    return send_from_directory("images",filename)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000)) # Use Render's PORT or a local default
    app.run(host='0.0.0.0', port=port, debug=False)
