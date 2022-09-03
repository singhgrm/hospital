#!c:\python27\python.exe
print "content-type:text/html\n\n"
#print "cheking.."
import cgi,MySQLdb
data=cgi.FieldStorage()
#n=data.getvalue('name')
e=data.getvalue('email')
feed=data.getvalue('feed')
#print e,comp
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
#print name 
q="insert into p_feedback(name,email,feedback,date) values('"+name+"','"+e+"','"+feed+"',sysdate())"
if status=="true":
 n=cur.execute(q)
 if n==1:
  print"<script>alert('your feedback is successfully submit to admin..');window.location.href='pt_feedback.py';</script>"
 else:
  print"<script>alert('your feedback is not successfully submit to admin');window.location.href='pt_feedback.py';</script>"
else:
 print"<script>alert('invalid email feedback is not successfully submit to admin');window.location.href='pt_feedback.py';</script>"
print "thanks"
 


