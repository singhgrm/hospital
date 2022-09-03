#!c:\python27\python.exe
print "content-type:text/html\n\n"
print "cheking.."
import cgi
import MySQLdb
data=cgi.FieldStorage()
e=data.getvalue('email')
p=data.getvalue('pwd')
print e,p
con=MySQLdb.connect("127.0.0.1","root","","hospital",3306);
query="select * from register where email='"+e+"' and pwd='"+p+"'" 
cur=con.cursor()
print "thanku"
a=cur.execute(query)
print "thanku"
con.commit()
print "thanku"
con.close()
print "thanku"
if a==1:
 print"<script>alert('welcome your login is successfull..');window.location.href='profile.py';</script>"
else:
 print"<script>alert('opps!!wrong password or email??..');window.location.href='index.html';</script>"
