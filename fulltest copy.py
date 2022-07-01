#!/usr/bin/env python
import argparse,sys,os,datetime
from requests_html import HTML
from dateutil.parser import parse
from datetime import date
from datetime import datetime

def wps(test):
    print ("Checking if our Webserver Nginx Based Works....")
    os.system('minikube service nginx-external')
    
def datecorrect(test):
# the dateutil parser 
# This module offers a generic date/time string parser which is able to parse most known formats to represent a date and/or time.
# the argparse 
# for this script to accept arguments 
# requests_HTML 
# enabling us using html parsing .


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
      
# the class erorr used to display error once the user , enters illegul input, such as -blahblahblah , it captures the argument input 
# and also prints the help used enabled by default of the argument parser itself

# if len(sys.argv)==1:
#    parser.print_help(sys.stderr)
#    sys.exit(1)
# used to print out help messages if no arugments are supplied on the command line .  
# the user must add 2 arguments , the first one of the below mentioned argument (wp,dv,dc) and the second is the word test.  

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

