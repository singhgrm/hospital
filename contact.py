#!c:\python27\python.exe
print "content-type:text/html\n\n"
#print "check.."
print """
<html>
<head>
<style>
#bg
{
min-height:600px;
width:1194px;
margin:1px;
#border:5px solid white;
background-image:url('images/p6.jpg');
}
#rgb
{
height:400px;
width:700px;
#margin-top:70px;
margin:70px;
margin-left:210px;
border:5px solid #00ff80;
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
color:#00ff80;
font-size:28px;
}
.st2
{
height:40px;
width:250px;
margin:15px;
border-bottom:4px solid #00ff80;
#border-bottom:2px solid #ffff80;
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
<!--content starts from here-->
<div id="bg">
<div id="rgb">
<div id="con">
<form action="contactcode.py" method="post">
<center>
<table>
<h3 style="color:#00ff80;">CONTACT WITH US</h3>
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
<td><input type="submit" value="submit" style="background-color:#00ff80;margin-left:110px;height:35px;width:70px;"></td>
</tr>
</table>
</center>
</form>
</div>
</div>
</div>
<!--content ends from here-->
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