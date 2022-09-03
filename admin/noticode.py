#!c:\python27\python.exe
print "content-type:text/html\n\n"
print "okk.."
import cgi
import MySQLdb
data=cgi.FieldStorage()
noti=data.getvalue('noti')
print noti
con=MySQLdb.connect("127.0.0.1","root","","hospital",3306)
query="insert into pt_notification(notify,date) values('"+noti+"',curdate())"
cur=con.cursor()
a=cur.execute(query)
con.commit()
con.close()
if a==1:
 print""""
 <script>
 window.location.href="shownotifi.py"
 </script>
 print"""
else:
 print""""
 <script>
 window.location.href="shownotifi.py"
 </script>
 print"""