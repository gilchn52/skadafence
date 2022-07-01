#!/usr/bin/env python
import argparse,sys,subprocess,webbrowser,os, js2py, moment
from requests_html import HTML
import datetime
from dateutil.parser import parse
from datetime import date
from datetime import datetime

def wps(test):
    print ("Checking if our Webserver Nginx Based Works....")
    os.system('minikube service nginx-external')
    
def datecorrect(test):

# This module offers a generic date/time string parser which is able to parse most known formats to represent a date and/or time.


    html = HTML(html="<a href='index.html'>")
    script = """  
    var today = new Date()
    var date = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate();
    document.innerHTML = date;
    """
    val = html.render(script=script, reload=False)
    print(val) 

    if val:
      try:
          parse(val)
          return print("date is valid")
      except:
        return print("date is not valid")
    return False
       
    
    
def datevalid(test):
    
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
  
    print("The date by the java object",correctedvalue)
    print("Today's date is:",todaycorreted)
    
    
    if correctedvalue == todaycorreted:
          return print("date is corret")
    else:
          return print("date is not corret")
      
    

class MyParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: %s\n' %message)
        self.print_help()
        sys.exit(2)
parser = MyParser()
parser = argparse.ArgumentParser(description='my process.')
parser.add_argument("-wp", "--webpage", action="store", help="webpage test", type=wps)
parser.add_argument("-dv", "--datevalid", action="store", help="date validaity test", type=datevalid)
parser.add_argument("-dc", "--datecorret", action="store", help="date corret checkup", type=datecorrect)
if len(sys.argv)==1:
    parser.print_help(sys.stderr)
    sys.exit(1)
    

args = vars(parser.parse_args())

