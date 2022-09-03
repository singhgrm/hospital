#!c:\python27\python.exe
print "content-type:text/html\n\n"
print """
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">

    <title>Hospital</title>
<style>
#con
{
min-height:500px;
width:100%;
background-image:url('d5.jpg');
}	
#rgb
{
height:300px;
width:600px;
margin:20px;
background-color:rgba(0,0,0,0.01);
}
</style>	
  </head>
  <link rel="stylesheet" href="home.css">
    <!-- Optional JavaScript; choose one of the two! -->

    <!-- Option 1: Bootstrap Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-ygbV9kiqUc6oa4msXn9868pTtWMgiQaeYH7/t7LECLbyPA2x65Kgf80OJFdroafW" crossorigin="anonymous"></script>

    <!-- Option 2: Separate Popper and Bootstrap JS -->
    <!--
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.4/dist/umd/popper.min.js" integrity="sha384-q2kxQ16AaE6UbzuKqyBE9/u/KzioAlnx2maXQHiDX9d4/zp8Ok3f+M7DPm+Ib6IU" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.min.js" integrity="sha384-pQQkAEnwaBkjpqZ8RU1fF1AKtTcHJwFl3pblpTlHXybJjHpMYo79HY3hIi4NKxyj" crossorigin="anonymous"></script>
    -->
<nav>
   <label class="img"><img src="plus.png" alt="" width="140" height="100"></label>
  <h1>Sanjay Gandhi PostGraduate Institute of Medical Science</h1>
  </nav>
  <body>
  <div id ="outer">
  <div class="go">
  <ol>
  <li><button class="btn btn-success" type="button"><a href="home1.py">Home</a></i></button></li>
    <li><button class="btn btn-success" type="button"><a href="showpatient.py">VIEW PATIENT</a></button></li>
    <li><button class="btn btn-success" type="button"><a href="showdoctor.py">VIEW DOCTOR</a></button></li>
    <li><button class="btn btn-success" type="button"><a href="showcomplain.py">VIEW COMPALIN</a></button></li>
    <li><button class="btn btn-success" type="button"><a href="showfeedback.py">VIEW FEEDBACK</a></button></li>
    <li><button class="btn btn-success" type="button"><a href="showquery.py">VIEW QUERY</a></button></li>
    <li><button class="btn btn-success" type="button"><a href="showcontact.py">VIEW CONTACT</a></button></li>
	<li><button class="btn btn-success" type="button"><a href="shownotifi.py">ADD NOTIFICATION</a></button></li>
	<li><button class="btn btn-success" type="button"><a href="job.py">ADD JOB </a></button></li>
  </ol>
</div>
<!--content starts here-->
<div id="con">
<div id="rgb">
<div id="cn">
<h1></h1>
</div>
</div>
</div>
<!--content ends here-->
<!--footer starts here-->
<div id="footer">
<div class=f1>
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
<div class=f1>
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
<div class=f1>
<center>
<h3 style="center">CONTACTUS</h3>
<p>general enquiry:05222494070</p>
<p>emergency:05222494470</p>
<p>patient ralative query: 05222494787</p>
<p>VIP patient guest house:05222494787</p>
<p>vishramalay:05222494788</p>
</center>
</div>
<div id="social">
<a href="https://www.facebook.com/"><img src="fb.jpg" style="height:50px;width:50px;margin-left:500px;"/></a>
<a href="https://web.whatsapp.com/ "><img src="w.jpg" style="height:50px;width:50px;"/></a>
<a href="https://twitter.com/ "><img src="t.jpg" style="height:50px;width:50px;"/></a>
<a href="https://www.youtube.com/watch?v=E5AjQNlrQLw"><img src="y.jpg" style="height:50px;width:50px;"/></a>
<object align="left" style="color:black;padding:0px;">copyright &copy; all reserved</object>
 <p style="color:red;font-size:25px;float:right;">SGPGI LKO</p>
</div>
</div>
<!--footer endss here-->
</div>
</body>
</html>
print """