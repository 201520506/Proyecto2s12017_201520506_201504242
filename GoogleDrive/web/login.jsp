<%-- 
    Document   : login
    Created on : May 8, 2017, 11:49:40 AM
    Author     : p_ab1
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <style type="text/css">        
body{
	background-color:#4aa2b0;
	color:#a2b04a;
	text-align:center;
	font-family:"Lucida Grande", "Lucida Sans Unicode", "Lucida Sans", "DejaVu Sans", Verdana, sans-serif;
}
a{	color:#fff;
	text-decoration:none;
}	
#loginform{
  margin-top:150px;
  margin-left:auto;
  margin-right:auto;
 width:270px;
}
.input{
	width:270px;
    padding:15px 25px;
    font-family:"Lucida Grande", "Lucida Sans Unicode", "Lucida Sans", "DejaVu Sans", Verdana, sans-serif;
	background: #f5f5f5;
	border:none;
	border-radius: 5px;
	color: #333;
	font-size: 14px;
	margin-top:15px;
}
.loginbutton{
	background-color:#ffdd00;
	border-radius:5px/5px;
	-webkit-border-radius:5px/5px;
	-moz-border-radius:5px/5px;
	color:#333;
	display:inline-block;
	font-family:"Lucida Grande", "Lucida Sans Unicode", "Lucida Sans", "DejaVu Sans", Verdana, sans-serif;
	font-size:18px;
	font-weight:bold;
	width:320px;
	text-align:center;
	line-height:50px;
	text-decoration:none;
	height:50px;
	margin-top:20px;
	margin-bottom:20px;
	border:none;
	outline:0;
	cursor: pointer;
}
.loginbutton:active {
	position:relative;
	top:1px;
}
.loginbutton:hover{
	background-color:#e5bf05;
}

    </style>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">	
        <title>Index</title>
    </head>
<body>
    
    
    <form id="loginform" action="ServletLogin" method="GET">
        <input type="text" name="usuL" class="input" placeholder="Usuario" /> 
        <input type="password" name="contraL" class="input" placeholder="Contrasena" />        
        <input type="submit" class="loginbutton" value="INGRESAR" />
       
    </form>
    <a href="registro.jsp">Crear una Cuenta</a>    
    
    <form id="loginform" action="ServletCargar.jsp" method="POST">
        <input type="file" name="archivo" value="" />
        
        <input type="submit" value="Subir" />
    </form>
</body>

