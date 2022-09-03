#!c:\python27\python.exe
print "content-type:text/html\n\n"
print "cheking.."
#!c:\python27\python.exe
print "content-type:text/html\n\n"
#print "check.."
print """
<html>
<head>
<style>
#outer
{
background-image:url('images/bg13.jpg');
}
/* Style The Dropdown Button */
.dropbtn {
  background-color:#4CAF50;
  color:white;
  margin:20px;
  width:200px;
  padding: 16px;
  font-size: 16px;
  border: none;
  cursor: pointer;
}

/* The container <div> - needed to position the dropdown content */
.dropdown {
  position: relative;
  display: inline-block;
  #background-color:red;
}

/* Dropdown Content (Hidden by Default) */
.dropdown-content {
  display: none;
  #color:white;
  position: absolute;
  #background-color: #f9f9f9;
  background-color:#004080;
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  z-index: 1;
}

/* Links inside the dropdown */
.dropdown-content a {
  color:#00ffff;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
}

/* Change color of dropdown links on hover */
.dropdown-content a:hover {background-color: #f1f1f1}

/* Show the dropdown menu on hover */
.dropdown:hover .dropdown-content {
  display: block;
}

/* Change the background color of the dropdown button when the dropdown content is shown */
.dropdown:hover .dropbtn {
  background-color:black;
}
#bg
{
min-height:600px;
width:1194px;
margin:1px;
#border:5px solid white;
background-image:url('images/p5.jpg');
}
#rgb
{
height:400px;
width:700px;
#margin-top:70px;
margin:70px;
margin-left:210px;
border:5px solid #ffff80;
background-color:rgba(0,0,0,0.5);
}
#con
{
height:400px;
width:700px;
#margin-bottom:40px;
#margin:50px;
}
.st1
{
color:#ffff80;
font-size:28px;
}
.st2
{
height:40px;
width:250px;
margin:15px;
border:1px solid white;
border-bottom:2px solid #ffff80;
}
</style>
<link rel="stylesheet" href="css/index.css" type="text/css"/>
<link rel="stylesheet" href="css/footer.css" type="text/css"/>
</head>
<body id="image">
<div id="outer">
<div id ="logo">
<div id="logo1">
</div>
<div id="logo2">
<center>
<h1>SANJAY GANDHI POSTGRADUATE </h1>
<h1>INSTITUTE OF MEDICAL SCIENCE</h1>
</center>
</div>
</div>
<!--menu starts from here-->
<div class="dropdown">
  <button class="dropbtn">MENU</button>
  <div class="dropdown-content">
    <a href="pt_feedback.py">FEEDBACK</a>
    <a href="pt_complain.py">COMPLAIN</a>
    <a href="doctorlist.py">DOCTOR LIST</a>
    <a href="pt_contact.py">CONTACT US</a>
    <a href="pt_query.py">QUERY</a>
    <a href="pt_logout.py">LOGOUT</a>
  </div>
</div>
<!--menu starts from here-->
<!--content starts from here-->
<div id="bg">
<div id="rgb">
<div id="con">
<form action="pt_contactcode.py" method="post">
<center>
<table>
<h3 style="color:#ffff80;">CONTACT WITH US</h3>
<tr>
<td class="st1">Name:</td>
<td><input type="text" name="name" class="st2"/></td>
</tr>
<tr>
<td class="st1">Email:</td>
<td><input type="email" name="email" class="st2"/></td>
</tr>
<tr>
<td class="st1">Mob no:</td>
<td><input type="number" name="mob" class="st2"/></td>
</tr>
<tr>
<td class="st1">Message:</td>
<td><textarea name="message" class="st2">
</textarea>
</td>
</tr>
<tr>
<td><input type="submit" value="submit" style="background-color:#ffff80;margin-left:110px;height:35px;width:70px;"></td>
</tr>
</table>
</center>
</form>
</div>
</div>
</div>
<!--content ends from here-->
<!-- footer stars here -->
<div id="footer">
<div id="footer1">
<div class="f1">
<center>
<h3>DEPARTMENT</h3>
<p>health informatics</p>
<p>cardiology</p>
<p>hemathology</p>
<p>microbiology</p>
<p>nuclear medicine</p>
<p>radiotherapy</p>
</center>
</div>
<div class="f1">
<center>
<h3>ACADEMIC ACTIVITIES</h3>
<p>academic programs</p>
<p>courses</p>
<p>traning</p>
<p>learning</p>
<p>teaching</p>
<p>specialities</p>
</center>
</div>
<div class="f1">
<center>
<h3 style="center">CONTACTUS</h3>
<p>general enquiry:05222494070</p>
<p>emergency:05222494470</p>
<p>patient ralative query: 05222494787</p>
<p>VIP patient guest house:05222494787</p>
<p>vishramalay:05222494788</p>
<p></p>
</center>
</div>
</div>
<div id="social">
<a href="https://www.facebook.com/"><img src="images/fb.jpg" style="height:50px;width:50px;margin-left:500px;"/></a>
<a href="https://web.whatsapp.com/ "><img src="images/w.jpg" style="height:50px;width:50px;"/></a>
<a href="https://twitter.com/ "><img src="images/t.jpg" style="height:50px;width:50px;"/></a>
<a href="https://www.youtube.com/watch?v=E5AjQNlrQLw"><img src="images/y.jpg" style="height:50px;width:50px;"/></a>
<object align="left" style="color:black;padding:0px;">copyright &copy; all reserved</object>
 <p style="color:red;font-size:25px;float:right;">SGPGI LKO</p>
</div>
</div>
<!-- footer ends from here -->
</div>
</body>
</html>
"""