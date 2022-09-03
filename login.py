#!c:\python27\python.exe
print "content-type:text/html\n\n"
print "check.."
print """
<html>
<head>
<style>
#login
{
hight:300px;
width:400px;
#border:5px solid;
background-color:#54a7ab;
}
</style>
</head>
<body>
<div id="login">
<form action ="logcode.py" method="post">
<table cellpadding="5" cellspacing="6">
<tr>
<td><input type="email" name=email class="c" placeholder="Email" required="true"/></td>
</tr>
<tr>
<td><input type="password" name="password" class="c"placeholder="password" required="true"/></td>
</tr>
<tr>
<td><input type="submit" value="login" class="a"/></td>
<td><p><a href="register.py">Not Registerd?</a></p></td>
</tr>
</table>
</form>
</div>
</body>
</html>
"""