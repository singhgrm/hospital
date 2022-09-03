#!c:\python27\python.exe
print "content-type:text/html\n\n"
#print "check"
import MySQLdb
import cgi
data=cgi.FieldStorage()
n=data.getvalue('name')
g=data.getvalue('d')
e=data.getvalue('email')
p=data.getvalue('pwd')
dpt=data.getvalue('dept')
t=data.getvalue('timeji')
day=data.getvalue('days')
#print day
#print n,g,e,p,d,day
con=MySQLdb.connect("127.0.0.1","root","","hospital",3306)
query="insert into doctorreg(name,gender,email,password,department,time,days) values('"+n+"','"+g+"','"+e+"','"+p+"','"+dpt+"','"+t+"','"+day+"')"
cur=con.cursor()
a=cur.execute(query)
print "thanku"
if a==1:
 print"<script>alert('welcome! you are registerd..');window.location.href='doctorreg.py';</script>"
else:
 print"<script>alert('opps!! you are registerd..');window.location.href='doctorreg.py';</script>"
 