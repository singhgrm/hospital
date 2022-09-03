#!c:\python27\python.exe
print "content-type:text/html\n\n"
#print "okk"
import cgi,MySQLdb
data=cgi.FieldStorage()
n=data.getvalue('name')
e=data.getvalue('email')
mob=data.getvalue('mob')
cont=data.getvalue('message')
print e,mob,cont
con=MySQLdb.connect("127.0.0.1","root","","hospital",3306)
cur=con.cursor()
q="insert into p_contact(name,email,mobileno,message,date) values('"+n+"','"+e+"','"+mob+"','"+cont+"',curdate())"
print "thanks"
n=cur.execute(q) 
con.commit()
con.close()
if n==1:
 print"<script>alert('your message is successfully submit to admin..');window.location.href='contact.py';</script>"
else:
 print"<script>alert('your message is not successfully submit to admin');window.location.href='contact.py';</script>"
print "thanks"
 



