#!c:\python27\python.exe
print "content-type:text/html\n\n"
print "check.."
print """
<html>
<head>
<style>
#formm
{
min-height:700px;
width:1000px;
margin-left:100px;
background-image:url('images/p7.jpg');
#border:2px solid green;
}
#rgb
{
height:700px;
width:1000px;
background-color:rgba(0,0,0,0.1);
}
.z
{
height:40px;
#width:240px;
#color:red;
margin:8px;
border:2px solid white;
outline:none;
border-bottom:4px solid #0080c0;
}
.y
{
font-size:20px;
color:white;
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
        <li class="active"><a href="index.html">HOME</a><span class="sr-only">(current)</span></li>
        <li class="active"><a href="about.py">ABOUTUS</a><span class="sr-only">(current)</span></li>
        <li class="active"><a href="hospital.py">HOSPITAL</a><span class="sr-only">(current)</span></li>
        <li class="active"><a href="reseach.py">RESEARCH ACTIVITIES</a><span class="sr-only">(current)</span></li>
        <li class="active"><a href="department.py">DEPARTMENTS</a><span class="sr-only">(current)</span></li>
		<li class="active"><a href="contact.py">CONTACT US</a><span class="sr-only">(current)</span></li>
		<li class="active"><a href="doctorreg.py">DOCTOR REG</a><span class="sr-only">(current)</span></li>
		 <li class="active"><a href="registration.py">REGISTRATION</a><span class="sr-only">(current)</span></li>
        <li class="active"><a href="jobs.py">AVAILBLE JOBS</a></li>
      </ul>
    </div>
	<!-- navbar-collapse -->
  </div><!-- container-fluid -->
</nav>
</div>
</div>
<!--menu ends from here..-->
<!--register starts from here..-->
<div id="formm">
<div id="rgb">
<form action="regcode.py" method="post">
<center>
<table>
<h2 style="color:white;">PATIENT REGISTRATION FORM</h2>
<tr>
<td class="y">Name:</td>
<td><input type="text" name ="name"  class="z" placeholder="first name"/></td>
<td class="y">problem:</td>
<td><input type="text" name ="lname"  class="z" placeholder="last name"/></td>
</tr>
<tr>
<td class="y">Father's Name:</td>
<td><input type="text" name ="fname" class="z" placeholder="father's name"/></td>
<td class="y">department</td>
<td>
<select name="dpt" class="z">
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
<td class="y">Gender:</td>
<td><input type="radio" name ="a" value="male"/>male
<input type="radio" name="a"  value="female"/>female
</td>
<td class="y">D.O.B:</td>
<td><input type="date" name ="dob" class="z" placeholder="dob" name="dob"/></td>
</tr>
<tr>
<td class="y">Email</td>
<td><input type="text" name ="email" class="z" placeholder="email"/></td>
<td class="y">password:</td>
<td><input type="password" class="z" name ="pwd" placeholder="password"/></td>
</tr>
<tr>
<td class="y">mobile no:</td>
<td><input type="number" class="z" name ="mbno" placeholder="mobile no"/></td>
<td class="y">contact no:</td>
<td><input type="number" class="z" name ="cno" placeholder="contact no"/></td>
</tr>
<tr>
<td class="y">occupation:</td>
<td>
<select name="occupation" class="z">
<option>-select-</option>
<option>doctor</option>
<option>farmer</option>
<option>student</option>
<option>buisness</option>
<option>advocate</option>
<option>others</option>
</select>
</td>
<td class="y">Age:</td>
<td><input type="text"  class="z" name ="age" placeholder="age"/></td>
</tr>
<tr>
<td class="y">Address:</td>
<td><input type="text" class="z" name ="state" placeholder="state"/></td>
<td><input type="text"class="z" name ="city" placeholder="city"/></td>
<td><input type="text" class="z" name ="country" placeholder="country"/></td>
</tr>
<tr>
<td class="y">Address:</td>
<td><input type="text"class="z" name ="houseno" placeholder="house"/></td>
<td><input type="text" class="z" name ="street" placeholder="street"/></td>
<td><input type="text" class="z" name ="pinno" placeholder="pin no"/></td>
</tr>
<tr>
<td class="y">Identity proof:</td>
<td>
<select  name="idproof" class="z">
<option>-select-</option>
<option>adhar card</option>
<option>pan card</option>
<option>BPL card</option>
<option>voter id card</option>
<option>driving license</option>
<option>others</option>
</select>
</td>
<td name="idcardno" class="y">Identity card no</td>
<td><input type="text" class="z" name="idcard" required="true" placeholder="ID card no"></td>
</tr>
<tr>
<td class="y">referring doctor:</td>
<td><input type="text" class="z" name ="dname" placeholder="doctor name"/></td>
<td class="y">Date:</td>
<td><input type="date"class="z" name ="date" placeholder="date"/></td>
</tr>
<tr>
<td>
<center>
<input type="submit" class="z" value="submit" style="background-color:#0080c0;height:45px;width:120px;"/>
</center>
</td>
</tr>
</table>
</center>
</form>
</div>
</div>
<!--register ends from here..-->
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
<!-- footer ends from here -->
</div>
</body>
</html>
"""