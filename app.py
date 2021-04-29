# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 10:39:35 2021

@author: rgctisvccapu01
"""

from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
from flask_mysqldb import MySQL
from flask import Flask, jsonify
import pymssql
import pandas as pd
import pymssql
import numpy as np
from datetime import *
from elasticsearch import Elasticsearch
import elasticsearch.helpers

app = Flask(__name__)
app.secret_key = "Secret Key"

@app.route('/')
def Index():
    return render_template("tracker.html")

@app.route('/tasks')
def tasks():
    connection = pymssql.connect(host='sd-fdce-df72.nam.nsroot.net', port='2431', database='cd20analytics',user='APAC\\rgctisvccapu01',password='global.ip.user.analytics.008')
    cur = connection.cursor()
    cur.execute("SELECT  * FROM DataReportTracker")
    data = cur.fetchall()
    cur.close()
    return render_template('tasks.html', tasks=data )

@app.route("/range",methods=["POST","GET"])
def range(): 
    if request.method == 'POST':
        From = request.form['From']
        to = request.form['to']
        print(From)
        print(to)
        connection = pymssql.connect(host='sd-fdce-df72.nam.nsroot.net', port='2431', database='cd20analytics',user='APAC\\rgctisvccapu01',password='global.ip.user.analytics.008')
        cur = connection.cursor() 
        #query = "SELECT * from DataReportTracker WHERE Date BETWEEN '{}' AND '{}'".format(From,to)
        cur.execute("SELECT * from DataReportTracker WHERE Date BETWEEN '{}' AND '{}'".format(From,to))
        ordersrange = cur.fetchall()
        cur.close()
        #connection.commit()
    return jsonify({'htmlresponse': render_template('response.html', ordersrange=ordersrange)})
    #return render_template('response.html', ordersrange=ordersrange )
    #return redirect(url_for('range'))
    #return jsonify(ordersrange)
    
@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == "POST":
       #id = request.form['id']
        Date = request.form['Date']
        Month = request.form['Month']
        JIRA_URL = request.form['JIRA_URL']
        Task = request.form['Task']
        Deliverable = request.form['Deliverable']
        Dashboard_URL = request.form['Dashboard_URL']
        BusinessValue = request.form['BusinessValue']
        Stakeholders = request.form['Stakeholders']
        Designation = request.form['Designation']
        connection = pymssql.connect(host='sd-fdce-df72.nam.nsroot.net', port='2431', database='cd20analytics',user='APAC\\rgctisvccapu01',password='global.ip.user.analytics.008')
        cur = connection.cursor()
        cur.execute("INSERT INTO DataReportTracker (Date, Month, JIRA_URL, Task, Deliverable, Dashboard_URL, BusinessValue, Stakeholders, Designation) VALUES ( %s, %s,%s, %s, %s,%s, %s, %s, %s)", (Date, Month, JIRA_URL, Task, Deliverable, Dashboard_URL, BusinessValue, Stakeholders, Designation))
        connection.commit()
        flash("Data Inserted Successfully")
        return redirect(url_for('tasks'))

@app.route('/delete/<id>', methods = ['GET'])
def delete(id):
    connection = pymssql.connect(host='sd-fdce-df72.nam.nsroot.net', port='2431', database='cd20analytics',user='APAC\\rgctisvccapu01',password='global.ip.user.analytics.008'
    cur = connection.cursor()
    cur.execute("DELETE FROM DataReportTracker WHERE id=%d", (id))
    connection.commit()
    flash("Record Has Been Deleted Successfully")
    return redirect(url_for('tasks'))

@app.route('/update',methods=['POST','GET'])
def update():
    if request.method == 'POST':
        id = request.form['id']
        Date = request.form['Date']
        Month = request.form['Month']
        JIRA_URL = request.form['JIRA_URL']
        Task = request.form['Task']
        Deliverable = request.form['Deliverable']
        Dashboard_URL = request.form['Dashboard_URL']
        BusinessValue = request.form['BusinessValue']
        Stakeholders = request.form['Stakeholders']
        Designation = request.form['Designation']
        connection = pymssql.connect(host='sd-fdce-df72.nam.nsroot.net', port='2431', database='cd20analytics',user='APAC\\rgctisvccapu01',password='global.ip.user.analytics.008')
        cur = connection.cursor()
        cur.execute("""UPDATE DataReportTracker SET Date=%s, Month=%s, JIRA_URL=%s, Task=%s, Deliverable=%s, Dashboard_URL=%s, BusinessValue=%s, Stakeholders=%s, Designation=%s WHERE id=%d""", (Date, Month, JIRA_URL, Task, Deliverable, Dashboard_URL, BusinessValue, Stakeholders, Designation,id))
        connection.commit()
        flash("Data Updated Successfully")
        return redirect(url_for('tasks'))
        #return render_template('tasks.html')
        
        
if __name__ == "__main__":
    app.run(debug=True)
    #app.run(host='0.0.0.0',port=8080, debug=True)
    #app.run(host='sd-ccfe-be78.nam.nsroot.net', port='5002', debug=True)
    #serve(app, host='0.0.0.0',port=8080, threads=1)
