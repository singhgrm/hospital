#!C:\python27\python.exe
print "content-type:text/html\n\n"
#print "heelo"
import cgi,MySQLdb
data=cgi.FieldStorage()
e=data.getvalue('email')
p=data.getvalue('password')
#print e ,p
con=MySQLdb.connect("127.0.0.1","root","","hospital",3306)
query="select *from admin where email='"+e+"' and password='"+p+"'" 
cur=con.cursor()
a=cur.execute(query)
con.commit()
con.close()
print"thanku"
if a==1:
 print"""
 <script>
 location.href="home1.py"
 </script>
 """
else:
 print"""
 <script>
 location.href="index.html"
 </script>
 """