#!c:\python27\python.exe
print "content-type:text/html\n\n"
#print "ok done"
print """
<html>
<head>
<style>
#form
{
min-height:800px;
width:100%;
#margin-left:65px;
padding:19px;
border:5px solid;
opacity:0.9;
background-image:url('images/regg.jpg');
}
</style>
</head>
<body>
<div id="form">
<form action="regcode.py" method="post">
<center>
<table  cellpadding="11" cellspacing="17">
<h2>REGISTRATION FORM</h2>
<tr>
<td>Name:</td>
<td><input type="text" name ="name" placeholder="first name"/></td>
<td><input type="text" name ="mname" placeholder="middle name"/></td>
<td><input type="text" name ="lname" placeholder="last name"/></td>
</tr>
<tr>
<td>Father's Name:</td>
<td><input type="text" name ="fname" placeholder="father's name"/></td>
<td>department</td>
<td>
<select  name=dpt>
<option>-select-</option>
<option>anaesthesia</option>
<option>apex trauma center</option>
<option>cardiology</option>
<option>endocrine surgery</option>
<option>endocrinology</option>
<option>general hosptal</option>
<option>immunology</option>
<option>microbiology</option>
<option>neonatology</option>
<option>others</option>
</select>
</td>
</tr>
<tr>
<td>Gender:</td>
<td><input type="radio" name ="a"/>male
<input type="radio" name="a"/>female
</td>
<td>D.O.B:</td>
<td><input type="text" name ="dob" placeholder="dob" name="dob"/></td>
</tr>
<tr>
<td>Email</td>
<td><input type="text" name ="email" placeholder="email"/></td>
<td>password:</td>
<td><input type="password" name ="pwd" placeholder="password"/></td>
</tr>
<tr>
<td>mobile no:</td>
<td><input type="number" name ="mbno" placeholder="mobile no"/></td>
<td>contact no:</td>
<td><input type="number" name ="cno" placeholder="contact no"/></td>
</tr>
<tr>
<td>occupation:</td>
<td>
<select name="occupation">
<option>-select-</option>
<option>doctor</option>
<option>farmer</option>
<option>student</option>
<option>buisness</option>
<option>advocate</option>
<option>others</option>
</select>
</td>
<td>Age:</td>
<td><input type="text" name ="age" placeholder="age"/></td>
</tr>
<tr>
<td>Address:</td>
<td><input type="text" name ="state" placeholder="state"/></td>
<td><input type="text" name ="city" placeholder="city"/></td>
<td><input type="text" name ="country" placeholder="country"/></td>
</tr>
<tr>
<td>Address:</td>
<td><input type="text" name ="houseno" placeholder="house"/></td>
<td><input type="text" name ="street" placeholder="street"/></td>
<td><input type="text" name ="pinno" placeholder="pin no"/></td>
</tr>
<tr>
<td>Identity proof:</td>
<td>
<select  name="idproof">
<option>-select-</option>
<option>adhar card</option>
<option>pan card</option>
<option>BPL card</option>
<option>voter id card</option>
<option>driving license</option>
<option>others</option>
</select>
</td>
<td name="idcardno">Identity card no</td>
<td><input type="text" name="idcard" required="true" placeholder="ID card no"></td>
</tr>
<tr>
<td>referring doctor:</td>
<td><input type="text" name ="dname" placeholder="doctor name"/></td>
<td>Date:</td>
<td><input type="date" name ="date" placeholder="date"/></td>
</tr>
<tr>
<td>
<input type="submit" value="submit"/>
</td>
</tr>
</table>
</center>
</form>
</div>
</body>
</html>
"""