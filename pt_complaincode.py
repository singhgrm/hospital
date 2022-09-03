#!c:\python27\python.exe
print "content-type:text/html\n\n"
#print "cheking.."
import cgi,MySQLdb
data=cgi.FieldStorage()
#n=data.getvalue('name')
e=data.getvalue('email')
comp=data.getvalue('comp')
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
q="insert into p_complain(name,email,complain,date) values('"+name+"','"+e+"','"+comp+"',sysdate())"
if status=="true":
 n=cur.execute(q)
 if n==1:
  print"<script>alert('your complain is successfully submit to admin..');window.location.href='pt_complain.py';</script>"
 else:
  print"<script>alert('your complain is not successfully submit to admin');window.location.href='pt_complain.py';</script>"
else:
 print"<script>alert('your complain is not successfully submit to admin');window.location.href='pt_complain.py';</script>"
print "thanks"
 


