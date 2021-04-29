from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from jinja2 import Template




app = Flask(__name__, template_folder='templates')
app.secret_key = "Secret Key"

#SqlAlchemy Database Configuration With Mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://APAC//rgctisvccapu01:global.ip.user.analytics.008@sd-ccfe-be78.nam.nsroot.net//cd20analytics'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


#Creating model table for our CRUD database
class Data(db.Model):
  # Date = db.Column(db.Integer, primary_key = True)
   # name = db.Column(db.String(100))
    #email = db.Column(db.String(100))
    #phone = db.Column(db.String(100))
    id = db.Column(db.Integer, primary_key = True)
    Date = db.Column(db.String(100))
    Month = db.Column(db.String(100))
    JIRA_URL = db.Column(db.String(100))
    Task = db.Column(db.String(100))
    Deliverable = db.Column(db.String(100))
    Dashboard_URL = db.Column(db.String(100))
    BusinessValue = db.Column(db.String(100))
    Stakeholders = db.Column(db.String(100))
    Designation = db.Column(db.String(100))
  


    #def __init__(self, name, email, phone):

     #   self.name = name
      #  self.email = email
       # self.phone = phone
    
    
    def __init__(self, id, Date, Month, JIRA_URL, Task, Deliverable, Dashboard_URL, BusinessValue, Stakeholders, Designation):

        self.id = id
        self.Date = Date
        self.Month = Month
        self.JIRA_URL = JIRA_URL
        self.Task = Task
        self.Deliverable = Deliverable
        self.Dashboard_URL = Dashboard_URL
        self.BusinessValue = BusinessValue
        self.Stakeholders = Stakeholders
        self.Designation = Designation
        





#This is the index route where we are going to
#query on all our employee data
@app.route('/')
def Index():
    #all_data = db.all()
    #all_data = Data.query.all()

    return render_template("tracker.html")

@app.route('/tasks')
def tasks():
    #all_data = db.all()
    all_data = Data.query.all()

    return render_template("tasks.html", tasks = all_data)


#app.add_url_rule('/', 'index', index)
#app.add_url_rule('/tasks', 'tasks', tasks)
#this route is for inserting data to mysql database via html forms
@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == 'POST':

        #name = request.form['name']
        #email = request.form['email']
        #phone = request.form['phone']


        #my_data = Data(name, email, phone)
        #db.session.add(my_data)
        #db.session.commit()

        #flash("Employee Inserted Successfully")

        #return redirect(url_for('Index'))
    
    
        #id = request.form['id']
        Date = request.form['Date']
        Month = request.form['Month']
        JIRA_URL = request.form['JIRA_LINK']
        Task = request.form['Task']
        Deliverable = request.form['Deliverable']
        Dashboard_URL = request.form['Dashboard_URL']
        BusinessValue = request.form['BusinessValue']
        Stakeholders = request.form['Stakeholders']
        Designation = request.form['Designation']


        my_data = Data(id, Date, Month,JIRA_URL, Task, Deliverable, Dashboard_URL, BusinessValue, Stakeholders, Designation)
        db.session.add(my_data)
        db.session.commit()

        flash("Task Inserted Successfully")

        return redirect(url_for('tasks'))


#this is our update route where we are going to update our employee
@app.route('/update', methods = ['GET', 'POST'])
def update():

    if request.method == 'POST':
        my_data = Data.query.get(request.form.get('id'))

        id = request.form['id']
        Date = request.form['Date']
        Month = request.form['Month']
        JIRA_URL = request.form['JIRA_LINK']
        Task = request.form['Task']
        Deliverable = request.form['Deliverable']
        Dashboard_URL = request.form['Dashboard_URL']
        BusinessValue = request.form['BusinessValue']
        Stakeholders = request.form['Stakeholders']
        Designation = request.form['Designation']

        db.session.commit()
        flash("Employee Updated Successfully")

        return redirect(url_for('tasks'))




#This route is for deleting our employee
@app.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):
    my_data = Data.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Employee Deleted Successfully")

    return redirect(url_for('tasks'))






if __name__ == "__main__":
    app.run(host='sd-ccfe-be78.nam.nsroot.net', port='5002', debug=True)
    #app.run(debug=True)