#!c:\python27\python.exe
print "content-type:text/html\n\n"
print "check.."
print """
<html>
<head>
<style>
#about
{
min-height:500px;
whidth:1200px;
margin-top:50px;
#border:2px solid blue;
}
#con
{
height:400px;
width:1175px;
border-radius:50px;
#border:2px solid green;
#background-image:url('images/bg5.jpg');
}
p
{
margin-left:30px;
padding:20px;
font-size:18px;
color:black;
}
#text
{
height:1510px;
width:1180px;
#border:5px solid;
#background-image:url('images/bg10.jpg');
box-shadow:7px 7px 5px 4px #40ff9f;
background-color:rgba(0,0,0,0.1);
}
#slider
{
height:500px;
width:1170px;
#border:2px solid blue;
}
.f1 p
{
text:12px;
color:black;
padding:5px;
margin:1px;
}
</style>
<script>
var img=["sgpgi.png","h2.jpg","h3.jpg","s8.jpg","sg1.jpg"];
var i=0;
function slide()
{
var n=document.getElementById("slider");
n.style.backgroundImage="url('images/"+img[i]+"')";
i++;
if(img.length==i)
{
i=0;
}
window.setTimeout("slide()",1000);
}
</script>
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
        <li class="active"><a href="about.py">ABOUTUS</a><span class="sr-only">(current)</span></a></li>
        <li class="active"><a href="hospital.py">HOSPITAL</a><span class="sr-only">(current)</span></a></li>
        <li class="active"><a href="reseach.py">RESEARCH ACTIVITIES</a><span class="sr-only">(current)</span></a></li>
        <li class="active"><a href="department.py">DEPARTMENTS</a><span class="sr-only">(current)</span></a></li>
		<li class="active"><a href="contact.py">CONTACT US</a><span class="sr-only">(current)</span></a></li>
		<li class="active"><a href="doctorreg.py">DOCTOR REG</a><span class="sr-only">(current)</span></a></li>
		 <li class="active"><a href="registration.py">REGISTRATION</a><span class="sr-only">(current)</span></a></li>
        <li class="active"><a href="confrence.py">CONFRENCES</a></li>
      </ul>
    </div>
	<!-- navbar-collapse -->
  </div><!-- container-fluid -->
</nav>
</div>
<!--menu ends from here..-->
<!--about stars from here..-->
<div id ="about">
<div id="con">
<center><h2 style="bgcolor:gray;">AN OVERVIEW</h2></center>
<p style="font-size:20px;margin:20px;padding:15px;">
Sanjay Gandhi Postgraduate Institute of Medical Sciences (SGPGIMS), Lucknow (India) is a University established under State Act in 1983. The Institute is located on a sprawling 550 acres residential campus at Raebareli Road, 15 km away from the main city. The institute offers its own degrees, which are duly recognized by the Medical Council of India. The Institute is rated amongst the top medical institutions in the country, delivering state-of-art tertiary medical care, super-specialty teaching, training and research. Dedicated faculty members endeavor to provide quality education, patient care and research and strive to meet the challenges and needs of the society. The Institute offers DM, MCh, MD, PhD, Post Doctoral Fellowships (PDF) and Post Doctoral Certificate Courses (PDCC), and Senior Residency in various specialties. The peers in the field have recognized the courses offered by the Institute and the candidates obtaining degrees from SGPGIMS have been highly placed both within the country and abroad.</p>
</div>
<div id="slider">
</div>
<div id="text">
<div id=text1>
<center><h3>COURCES</h3></center>
<h4>DM Courses 	</h4>
<p>Cardiology, Clinical Immunology, Endocrinology, Gastroenterology, Medical Genetics, Nephrology, Neurology
</p>
<h4>MCh Courses	</h4>
<p>Cardiothoracic and Vascular Surgery, Neurosurgery, Surgical Gastroenterology, Urology
</p>
<h4>Post-Doctoral Certificate Courses (PDCC)</h4>
<p>Blood Component Therapy and Apheresis Technology, Cardiac Anaesthesia, Endocrine Surgery, Infectious Diseases, Neuro-anaesthesia, Neuro-Radiology, Nuclear Nephro-Urology, Pediatric Gastroenterology, Renal Pathology, Pediatric Endocrinology
</p>
<h4>MD Courses	</h4>
<p>Anaesthesiology, Microbiology, Nuclear Medicine, Pathology, Radiodiagnosis, Radiotherapy, Transfusion Medicine
</p>
<h4>PhD Courses	</h4>
<p>In various departments of the Institute [Currently offered in departments of Endocrinology, Gastroenterology, Immunology, Medical Genetics, Microbiology, Neurology, Nuclear Medicine, Pathology, Radiotherapy (Medical Physics) and Transfusion Medicine]
</p>
</div>
<div id=text2>
<center><h3>TRAINING</h3></center>
<p>DM, MCh and MD courses are of 3-year duration each. PDCC courses are of one-year duration. PhD students may submit their thesis after a minimum of  3 years. Maximium period of registration for PhD students is  5 years. 
Senior Residents (Hospital Service) are appointed initially for one year; this appointment can be renewed every year, up to a maximum period of 3 years. 

Students admitted to DM, MCh and PDCC courses are simultaneously appointed as Senior Residents and receive a salary at par with that paid to Senior Residents elsewhere, (Rs 10,940, 11,295, and  11,650 in first, second and third year, respectively); in addition, they receive dearness allowance and other allowances as per rules and are provided free furnished accomodation on the campus. 

Students admitted to MD, courses are simultaneously appointed as Junior Residents and receive a salary at par with that paid to Junior Residents elsewhere (Rs 9,400, 9725, and 10,050 in first, second and third year, respectively); in addition, they receive dearness allowance and other allowances as per rules and are provided free furnished accomodation on the campus. 
</p>
</div>
<div id=text3>
<center><h3>ACADEMIC FACILITIES</h3></center>
<p>Library Facilities
The Institute has a well-equipped library with nearly 16,000 books. The library subscribes to nearly 450 scientific journals. The library provides facilities for loaning of library books and journals, photocopying, internet access for literature search, etc. In addition, the library has inter-library loan arrangements with libraries of several other scientific institutions in the city. 
 

Computer Facilities
The Institute has a hospital-wide computer network with more than 200 computers spread all over the hospital and departments. Internet connections are available in all the departments. All faculty members, residents and students are provided with e-mail facilities. The patient care activites are computerised with implementation of Windows-based hospital information system

Auditorium and Seminar Rooms
The Institute currently has an auditorium with a seating capacity for nearly 140 persons. A larger main auditorium complex is under construction. In addition, each department had seminar room(s) for conducting departmental teaching activities</p>
</div>
<div id=text4>
<center><h3>SPECIAL FEATURES</h3></center>
<p>Research: A publication in an indexed national / international journal is a basic, mandatory requirement for DM and MCh programs. Thesis is a compulsory part of MD programs. The curriculum is designed to integrate the themes of globalisation, quality, comparative advantage, service, change, technology, and historical perspective, and to provide opportunities for the development of interpersonal skills including leadership, oral and written communication and practical applications.

Faculty: The faculty members at SGPGI include nationally and internationally renowned specialists recognized for their contributions to advance the medical science. They are also recognized for their dedication to excellence in teaching. The faculty combines its work in the frontier areas of medicine and science with a realistic modern view of medicine and brings to the institute exciting real life perspectives and insight.</p>
</div>
</div>
</div>
<!--about ends from here..-->
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