#!C:\Python27\python.exe
print "content-type:text/html\n\n"
#print "editing.. is here"
print"""
<html>
<head>
<script>
function logout()
{
 window.history.forward();
 window.setTimeout(window.location.href='index.html',2000);
}
</script>
</head>
<body onload="logout()" bgcolor="black">
</body>
</html>
"""