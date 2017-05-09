<%-- 
    Document   : registro
    Created on : May 8, 2017, 11:55:05 AM
    Author     : p_ab1
--%>

<%@page import="java.io.InputStreamReader"%>
<%@page import="java.io.BufferedReader"%>
<%@page import="java.net.HttpURLConnection"%>
<%@page import="java.net.URL"%>
<%@page contentType="text/html" pageEncoding="UTF-8"%>
<%@page import="javax.servlet.http.HttpSession"%>
<!DOCTYPE html>

<!--A Flat Design Login Page by Codelator.com-->
<html>
    <style type="text/css">        
body{
	background-color:#4aa2b0;
	color:#f5f5f5;
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
	<script type="text/javascript" src="tcal.js"></script> 
        <title>Registro</title>
    </head>
<body>
    
    <form id="loginform" method="GET" action="registro.jsp">
        <input type="text" name="usuR" class="input" placeholder="Usuario" /> 
        <input type="password" name="contraR" class="input" placeholder="Contrasena"/>        
        <input type="submit" class="loginbutton" value="REGISTRARSE" />
    </form>
    <%
    if(request.getParameter("contraR")!= null && request.getParameter("usuR")!= null){
        String contra =(String) request.getParameter("contraR");
        String usu =(String) request.getParameter("usuR");
        HttpSession s  = request.getSession(true);
        if(contra.length() >= 4){
            s.setAttribute("contra", contra);
            s.setAttribute("usu", usu);
                try {
                String puerto ="http://127.0.0.1:8000/";
                String imp;    
                String url = puerto+"registro?usu="+usu+"&&contra="+contra;
                URL obj = new URL(url);
                HttpURLConnection con = (HttpURLConnection) obj.openConnection();
                con.setRequestMethod("GET");
                con.setRequestProperty("User-Agent", "k");
                int responseCode = con.getResponseCode();
                System.out.println("\nSending 'GET' request to URL : " + url);
                System.out.println("Response Code : " + responseCode);
                BufferedReader in = new BufferedReader(new InputStreamReader(con.getInputStream()));
                String inputLine;
                StringBuffer a = new StringBuffer();
                while ((inputLine = in.readLine()) != null) {
                    a.append(inputLine);
                }
                in.close();
                imp=a.toString();
                //print result
                System.out.println(a.toString());
                if(!imp.equals("None")){
                     response.sendRedirect("principal.jsp");
                }else{
                    out.print("<h3>Ocurrion un Error</h3>");
                }
                } catch (Exception e) {
                    response.sendRedirect("login.jsp");
                }
        }else{
            out.print("<h3>Contraseña menor a 4 caracteres</h3>");
        }
    }
    %>
    <a href="login.jsp">Iniciar Sesion</a>    
</body>
<%

    
%>