#!c:\python27\python.exe
print "content-type:text/html\n\n"
print "okk"
import cgi,MySQLdb
data=cgi.FieldStorage()
#n=data.getvalue('name')
e=data.getvalue('email')
mob=data.getvalue('mob')
cont=data.getvalue('message')
print e,mob,cont
con=MySQLdb.connect("127.0.0.1","root","","hospital",3306)
cur=con.cursor()
query="select name from register where email='"+e+"'"
cur.execute(query)
res=cur.fetchall()
name=""
status="false"
for r in res:
 name=r[0]
 status="true"
print name 
q="insert into p_contact(name,email,mobileno,message,date) values('"+name+"','"+e+"','"+mob+"','"+cont+"',curdate())"
print "thanks"
if status=="true":
 n=cur.execute(q) 
 if n==1:
  print"<script>alert('your message is successfully submit to admin..');window.location.href='pt_contact.py';</script>"
 else:
  print"<script>alert('your message is not successfully submit to admin');window.location.href='pt_contact.py';</script>"
else:
 print"<script>alert('your message is not successfully submit to admin');window.location.href='pt_contact.py';</script>"
print "thanks"
 



