#!c:\python27\python.exe
print "content-type:text/html\n\n"
#print "okk..."
import cgi
import MySQLdb
data=cgi.FieldStorage()
n=data.getvalue('name')
mn=data.getvalue('mname')
ln=data.getvalue('lname')
fn=data.getvalue('fname')
dpt=data.getvalue('dpt')
g=data.getvalue('a')
dob=data.getvalue('dob')
email=data.getvalue('email')
pwd=data.getvalue('pwd')
mbno=data.getvalue('mbno')
cno=data.getvalue('cno')
occ=data.getvalue('occupation')
state=data.getvalue('state')
city=data.getvalue('city')
contry=data.getvalue('country')
houseno=data.getvalue('houseno')
st=data.getvalue('street')
pinno=data.getvalue('pinno')
idproof=data.getvalue('idproof')
idcard=data.getvalue('idcard')
#pinno=data.getvalue('pinno')
dname=data.getvalue('dname')
age=data.getvalue('age')
date=data.getvalue('date')
#print n,mn,ln,fn,dpt,email,pwd,mbno,cno,occ,age,state,city,contry,houseno,st,pinno,idproof,idcard,pinno,dname,date
con=MySQLdb.connect("127.0.0.1","root","","hospital",3306)
query="insert into register(name,lname,fname,department,gender,dob,email,pwd,mobileno,contactno,occupation,state,city,country,houseno,street,pinno,idproof,idcardno,doctorname,age,date) values('"+n+"','"+ln+"','"+fn+"','"+dpt+"','"+g+"','"+dob+"','"+email+"','"+pwd+"','"+mbno+"','"+cno+"','"+occ+"','"+state+"','"+city+"','"+contry+"','"+houseno+"','"+st+"','"+pinno+"','"+idproof+"','"+idcard+"','"+dname+"','"+age+"','"+date+"')"
cur=con.cursor()
a=cur.execute(query)
#print "okk..."
if a==1:
 print"<script>alert('welcome...you are registered..')</script>"
else:
 print"<script>alert('ohh...you are not registered..')</script>"













