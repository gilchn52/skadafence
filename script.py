#!/usr/bin/env python
import argparse,sys,subprocess,webbrowser,os, js2py, moment
from requests_html import HTML
import datetime
from dateutil.parser import parse
from datetime import date
from datetime import datetime


def datevalid():
    
    html = HTML(html="<a href='index.html'>")
    script = """  
    var today = new Date()
    var date = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate();
    document.innerHTML = date;
    """
    val = html.render(script=script, reload=False)
    # printing the date value as shown on the javascript on our index.html file 
    print(val) 
    # Converting the "val" variable string object,  into datetime object, using strptime
    javadate = datetime.strptime(val, '%Y-%m-%d')
    # Remove Padding to match result as python date output 
    correctedvalue = javadate.strftime('%Y-M%m-D%d').replace("M0","").replace("D0","")
    # checking today's date 
    today = date.today()
    # remove padding for today's date
    todaycorreted = today.strftime('%Y-M%m-D%d').replace("M0","").replace("D0","")
    
    # comparing both variables
  
    print("the date by the java object",correctedvalue)
    print("the date by the python",todaycorreted)
    
    
    if correctedvalue == todaycorreted:
          return print("date is corret")
    else:
          return print("date is not corret")
datevalid()

    
