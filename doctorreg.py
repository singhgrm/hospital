#!c:\python27\python.exe
print "content-type:text/html\n\n"
#print "check.."
print """
<html>
<head>
<style>
#con
{
height:600px;
width:1180px;
#border:2 px solid red;
}
#con1
{
height:400px;
width:400px;
float:left;
margin-left:40px;
margin-top:40px;
#background-color:rgba(0,0,0,0.5);
border:2px solid blue;
}
#rgb1
{
height:400px;
width:400px;
float:left;
border:2px solid blue;
}
#con2
{
height:500px;
width:600px;
float:left;
margin-left:40px;
margin-top:40px;
#background-color:rgba(0,0,0,0.5);
border:2px solid blue;
}
#rgb2
{
height:500px;
width:600px;
float:left;
#border:2px solid green;
}
.m
{
height:40px;
width:190px;
margin:10px;
bottom-border:5px solid blue;
}

.n
{
font-size:17px;
}
</style>
<link rel="stylesheet" href="css/index.css" type="text/css"/>
<link rel="stylesheet" href="css/footer.css" type="text/css"/>
<meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
<link href="css/bootstrap.min.css" rel="stylesheet" type="text/css"/>
<link href="css/bootstrap-theme.min.css" rel="stylesheet" type="text/css"/>
<link href="css/font-awesome.min.css" rel="stylesheet" type="text/css"/>
<script src="js/jquery-2.1.0.min.js"></script>
<script src="js/bootstrap.min.js"></script>
<script>

</script>
</head>
<body id="image" onload="slide()">
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
<div id="menu">
<!--menu start from here..-->
<div class="container-fluid" style="min-height:55px;">
<div class="row" style="min-height:40px;">
<!--menubar starts here....-->
<nav class="navbar navbar-default  navbar-invers" style="margin-bottom:0px;">
  <div class="container-fluid">
    <!-- Brand and toggle get grouped for better mobile display -->
    <div class="navbar-header">
      <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
        <span class="sr-only">Toggle navigation</span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
    </div>

    <!-- Collect the nav links, forms, and other content for toggling -->
    <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
      <ul class="nav navbar-nav">
        <li class="active"><a href="index.html">HOME</a><span class="sr-only">(current)</span></a></li>
        <li class="active"><a href="about.py">ABOUTUS</a><span class="sr-only">(current)</span></li>
        <li class="active"><a href="hospital.py">HOSPITAL</a><span class="sr-only">(current)</span></li>
        <li class="active"><a href="reseach.py">RESEARCH ACTIVITIES</a><span class="sr-only">(current)</span></li>
        <li class="active"><a href="department.py">DEPARTMENTS</a><span class="sr-only">(current)</span></a></li>
		<li class="active"><a href="contact.py">CONTACT US</a><span class="sr-only">(current)</span></a></li>
		<li class="active"><a href="doctorreg.py">DOCTOR REG</a><span class="sr-only">(current)</span></a></li>
		 <li class="active"><a href="registration.py">REGISTRATION</a><span class="sr-only">(current)</span></a></li>
        <li class="active"><a href="jobs.py">AVAILBLE JOBS</a></li>
      </ul>
    </div>
	<!-- navbar-collapse -->
  </div><!-- container-fluid -->
</nav>
</div>
<!--menu ends from here..-->
<!--registration and login stars from here..-->
<div id="reg">
<div id="con">
<div id="con1">
<div id="rgb1">
<form action="doclogcode.py" method="post">
<h3>DOCTOR LOGIN FORM</h3>
<table>
<tr>
<td class="n">email:</td>
<td><input type="email" name="email" required="true" class="m"/></td>
</tr>
<tr>
<td class="n">password:</td>
<td><input type="password" name="pwd" required="true" class="m"></td>
</tr>
<tr>
<td><input type="submit" value="login"/></td>
</tr>
</table>
</form>
</div>
</div>
<div id="con2">
<div id="rgb2">
<form action="docregcode.py" method="post">
<h3>DOCTOR REGISTRATION FORM</h3>
<table>
<tr>
<td class="n">Name</td>
<td><input type="text" name="name" required="true"  class="m"/></td>
</tr>
<tr>
<td class="n">Gender</td>
<td>
<input type="radio" name="d" value="male"/>Male
<input type="radio" name="d" value="female"/>Female
</td>
</tr>
<tr>
<td class="n">Email:</td>
<td><input type="email" name="email" required="true" class="m"/></td>
</tr>
<tr>
<td class="n">Password:</td>
<td><input type="password" name="pwd" required="true" class="m"/></td>
</tr>
<tr>
<td class="n">Department:</td>
<td>
<select name="dept" required="true" class="m">
<option>-select department-</option>
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
<td class="n">Timing:</td>
<td>
<select name="timeji" required="true" class="m">
<option>-select time-</option>
<option>7:00am to 9:00am</option>
<option>10:00am to 2:00pm</option>
<option>1:00pm to 4:00pm</option>
<option>7:00pm to 9:00pm</option>
<option>8:00pm to 11:00pm</option>
</select>
</td>
</tr>
<tr>
<td class="n">days:</td>
<td>
<select name="days" class="m">
<option>-select day-</option>
<option>monday-saturday</option>
<option>monday-wednesday</option>
<option>thursday</option>
<option>friday-saturaday</option>
<option>sunday</option>
<option>tuesday to friday</option>
</select>
</td>
</tr>
<tr>
<td>
<input type="submit" value="submit"/>
</td>
</tr>
</table>
</form>
</div>
</div>
</div>
</div>
<!--registration and login ends from here..-->
<!-- footer starts here -->
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
<!-- footer starts here -->
</div>
</body>
</html>
"""