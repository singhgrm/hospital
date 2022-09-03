#!c:\python27\python.exe
print "content-type:text/html\n\n"
#print "hello"
import MySQLdb
print """
<html>
<head>
<style>
body
{
background-image:url('images/bg14.jpg');
}
#con
{
min-height:700px;
width:100%
margin-top:0px;
background-image:url('images/bg14.jpg');
}
#rgb
{
min-height:400px;
width:700px;
margin:60px;
margin-left:230px;
border:6px solid #004080;
background-color:rgba(0,0,0,0.4);
}
#cn
{
min-height:400px;
width:700px;
}
tr th
{
color:white;
margin:3px;
}
tr td
{
color:white;
margin:3px;
}
</style>
</head>
<body>
<!--content starts here-->
<div id="con">
<div id="rgb">
<div id="cn">
<center>
<h3 style="color:white;">view patients registration list</h3>
<form>
<table border="4" cellpadding="4" cellspacing="4" style="border:4px solid white;border-color:white;">
<tr>
<th>ID</th>
<th>NAME</th>
<th>PROBLEM</th>
<th>DEPARTMENT</th>
<th>GENDER</th>
<th>DOB</th>
<th>MOBILE NO</th>
<th>DOCTOR NAME</th>
</tr>
"""
con=MySQLdb.connect("127.0.0.1","root","","hospital",3306)
#print "thanku.."
query="select * from register"
cur=con.cursor()
cur.execute(query)
q=cur.fetchall()
for row in q:
 print "<tr><td>",row[0],"</td>"
 print "<td>",row[1],"</td>"
 print "<td>",row[2],"</td>"
 print "<td>",row[4],"</td>"
 print "<td>",row[5],"</td>"
 print "<td>",row[9],"</td>"
 print "<td>",row[10],"</td>"
 print "<td>",row[20],"</td></tr>"
print """
</table>
</form>
</center>
</div>
</div>
</div>
</body>
</html>
"""