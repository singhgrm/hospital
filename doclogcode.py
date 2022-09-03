#!c:\python27\python.exe
print "content-type:text/html\n\n"
print "check.."
import cgi,MySQLdb
data=cgi.FieldStorage()
e=data.getvalue('email')
p=data.getvalue('pwd')
print e,p
con=MySQLdb.connect("127.0.0.1","root","","hospital",3306)
query="select * from doctorreg where email='"+e+"' and password='"+p+"'"
cu=con.cursor()
a=cu.execute(query)
con.commit()
con.close()
print "okk"
if a==1:
 print "<script>alert('your login is succesfull..');window.location.href='appointment.py'</script>"
else:
 print "<script>alert('invalid email or password...');window.location.href='doctorreg.py'</script>"