#!c:\python27\python.exe
print "content-type:text/html\n\n"
print "okk"
import cgi,MySQLdb
data=cgi.FieldStorage()
job=data.getvalue('job')
loc=data.getvalue('loc')
s=data.getvalue('sallery')
d=data.getvalue('deegree')
dept=data.getvalue('dept')
con=MySQLdb.connect("127.0.0.1","root","","hospital",3306)
query="insert into job(post,deegree,location,sallery,department) values('"+job+"','"+d+"','"+loc+"','"+s+"','"+dept+"')"
cur=con.cursor()
a=cur.execute(query)
con.commit()
con.close()
if a==1:
 print "<script>window.location.href='job.py';</script>"
else:
 print "<script>window.location.href='job.py';</script>"

