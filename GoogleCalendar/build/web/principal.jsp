<%-- 
    Document   : principal
    Created on : May 6, 2017, 11:20:30 AM
    Author     : p_ab1
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>

<%@page import="javax.servlet.http.HttpSession"%>
<!DOCTYPE html>
<html lang="en">
<%
String ano="";
String mes ="";
HttpSession se  = request.getSession(true);
String usuario= (String)se.getAttribute("usuario");
String contra= (String)se.getAttribute("contra");
%>
<head>

    <title>GOOGLE CALENDAR</title>
    <link href="css/bootstrap.min.css" rel="stylesheet">
    <link href="css/small-business.css" rel="stylesheet">


</head>

<body>

    <!-- Navigation -->
    <nav class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
            <!-- Brand and toggle get grouped for better mobile display -->
            <div class="navbar-header">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
                    <span class="sr-only">prueba</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
            </div>
            <!-- Collect the nav links, forms, and other content for toggling -->
            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                <ul class="nav navbar-nav">
                    <li>
                        <font color="#ffff"><h1>Bienvenido : <%=usuario%></h1></font>
                    </li>
                    
                </ul>
            </div>
            <!-- /.navbar-collapse -->
        </div>
        <!-- /.container -->
    </nav>

    <!-- Page Content -->
    <div class="container">

        <!-- Heading Row -->
        <div class="row">
            <div class="col-md-8">
                <form id="loginform" action="principal.jsp" method="POST"> 
                    <table cellspacing='10' cellpadding=10 border="0" >
                        <tr >
                            <td>
                                <h3>MES:</h3>
                <select name="mes">
                    <option value="enero">enero</option>
                    <option value="febrero">febrero</option>
                    <option value="marzo">marzo</option>
                    <option value="abri">abri</option>                    
                    <option value="mayo">mayo</option>                    
                    <option value="junio">junio</option>                    
                    <option value="julio">julio</option>                    
                    <option value="agosto">agosto</option>                    
                    <option value="sepetiempre">septiembre</option>
                    <option value="octubre">octubre</option>
                    <option value="noviembre">noviembre</option>
                    <option value="diciembre">diciembre</option>
                  </select>
                
                            </td>
                            <td>
                                <h3>Año:</h3>
                <select name="ano">
                <%
                for(int i=10;i<17;i++){
                    out.print("<option value="+20+i+">20"+i+"</option>");
                }
                %>            
                </select>
                            </td>
                            <td><input type="submit" class="loginbutton" value="IR" /></td>
                        </tr>
                    </table>
                
                
                <br>                         
                
                </form>
        <%
        if( request.getParameter("ano")!=null &&  request.getParameter("ano")!=null){                    
         ano = request.getParameter("ano");
         mes = request.getParameter("mes");
         Object  matriz[][] = new Object[7][4];
        for (int x = 0; x <= 3; x++) {            
            for (int y = 0; y <= 6; y++) {
                matriz[y][x]= null;
            }
        }
        
         out.print("<table class=\"table table-sm\">");
        out.print("<thead>"+
            "<tr>"+
                "<th>Lunes</th>"+
                "<th>Martes</th>"+
                "<th>Miercoles</th>"+
                "<th>Jueves</th>"+
                "<th>Viernes</th>"+
                "<th>Sabado</th>"+
                "<th>Domingo</th>"+
            "</tr>"+
        "</thead>"+
        "<tbody>");
        int conta=0;
        for (int x = 0; x < 4; x++) {
            out.print("<tr>");
            
            for (int y = 0; y < 7; y++) {
                conta++;
                out.print("<td>"+conta+"</td>");
            }
            out.print("</td>");
            
        }
        out.print("</tbody>"+
       " </table >");
        }%>
            </div>
            <!-- /.col-md-8 -->
            <div class="col-md-4">
                <h1>Agregar Evento</h1>
                <form action="ServletAgregarEvento" method="POST">
                <p>
                    Dia:<select name="dia2">
                <%
                for(int i=1;i<30;i++){
                    out.print("<option value="+i+">"+i+"</option>");
                }
                %>            
                </select>                
                </p>
                <p>
                        Mes:<select name="mes2">
                    <option value="enero">enero</option>
                    <option value="febrero">febrero</option>
                    <option value="marzo">marzo</option>
                    <option value="abri">abri</option>                    
                    <option value="mayo">mayo</option>                    
                    <option value="junio">junio</option>                    
                    <option value="julio">julio</option>                    
                    <option value="agosto">agosto</option>                    
                    <option value="sepetiempre">septiembre</option>
                    <option value="octubre">octubre</option>
                    <option value="noviembre">noviembre</option>
                    <option value="diciembre">diciembre</option>
                  </select>
                </p>
                 <p>Año:<select name="ano2">
                <%
                for(int i=10;i<17;i++){
                    out.print("<option value="+20+i+">20"+i+"</option>");
                }
                %>            
                </select></p>
                <p>Nombre:<input type="text" name="nombre"/></p>
                <p>Descripcion:<input type="text" name="desc"/></p>
                <p>Direccion:<input type="text" name="direc"/></p>
                <p>Hora: <input type="text" name="hora"/></p>          
                <input class="btn btn-primary btn-l" type="submit" value="AGREGAR" />
               </form>
            </div>
            <!-- /.col-md-4 -->
        </div>
        <!-- /.row -->

        <hr>

        <!-- Call to Action Well -->
        <div class="row">
            <div class="col-lg-12">
                <div class="well text-center">
                    PROYECTO FINAL DE EDD - GOOGLE CALENDAR  - BIENVENIDO !!!!!
                     <form action="ServletModificarEvento" method="POST">
                <h2>Buscar un Evento</h2>
                <p>Nombre Evento:<input type="text" name="evento"/></p>
                <p>Fecha: <input type="text" name="fecha"/></p>
                <input class="btn btn-success" type="submit" value="Buscar" />
               </form>
                </div>
            </div>
            <!-- /.col-lg-12 -->
        </div>
        <!-- /.row -->

        <!-- Content Row -->
        <div class="row">
            <div class="col-md-4">
                <h2>Modificar Un Evento</h2>
                <%
                if(session.getAttribute("evento")!=null &&
                   session.getAttribute("dia")!=null &&
                   session.getAttribute("direccion")!=null &&
                   session.getAttribute("des")!=null &&
                   session.getAttribute("hora")!=null){                    
                    
                       boolean bandera =(Boolean)session.getAttribute("bandera");
                       System.out.println(bandera);
                       if(bandera==false){
                           
                       %>
                       <br>
                       <form action="ServletModEvento" method="POST">
                <p>Evento: <input type="text" name="Neve" value="<%=session.getAttribute("evento")%>"/></p>
                <p>Dia <input type="text" name="Ndia" value="<%=session.getAttribute("dia")%>"/></p>
                <p>Direccion: <input type="text" name="Ndir" value="<%=session.getAttribute("direccion")%>"/></p>
                <p>Descripcion: <input type="text" name="Ndes" value="<%=session.getAttribute("des")%>"/></p>
                <p>Hora: <input type="text" name="Nhor" value="<%=session.getAttribute("hora")%>"/></p>
                 <input class="btn btn-warning" type="submit" value="MODIFICAR" />
                       </form>
                <%
                       }else{
                       out.print("<h3>No se encontro</h3>");
                       }
                   
                }
                %>
            </div>
            <!-- /.col-md-4 -->
            <div class="col-md-4">
                <h2>Eliminar un Evento</h2>
                <%
                if(session.getAttribute("evento")!=null &&
                   session.getAttribute("dia")!=null &&
                   session.getAttribute("direccion")!=null &&
                   session.getAttribute("des")!=null &&
                   session.getAttribute("hora")!=null){                    
                    
                       boolean bandera =(Boolean)session.getAttribute("bandera");
                       System.out.println(bandera);
                       if(bandera==false){
                           
                       %>
                       <br>
                       <form action="servletEliminar" method="POST">
                <p>Evento: <input type="text" name="ev"  readonly=”readonly” value="<%=session.getAttribute("evento")%>"/></p>
                <p>Dia <input type="text" name="di" readonly=”readonly” value="<%=session.getAttribute("dia")%>"/></p>
                <p>Direccion: <input type="text" name="dr"  readonly=”readonly” value="<%=session.getAttribute("direccion")%>"/></p>
                <p>Descripcion: <input type="text" name="de" readonly=”readonly” value="<%=session.getAttribute("des")%>"/></p>
                <p>Hora: <input type="text" name="ho" readonly=”readonly” value="<%=session.getAttribute("hora")%>"/></p>
                 
                       <input class="btn btn-danger" type="submit" value="ELIMINAR" />
                       </form>
                <%
                       }else{
                       out.print("<h3>No se encontro</h3>");
                       }
                   
                }
                %>
                
            </div>
            <!-- /.col-md-4 -->
            <div class="col-md-4">
                <h2>Generacion de Codigo QR</h2>
                <IMG SRC="QRevento.png" WIDTH=180 HEIGHT=180>
            </div>
            <!-- /.col-md-4 -->
        </div>
        <!-- /.row -->

        <!-- Footer -->
        <footer>
            <div class="row">
                <div class="col-lg-12">
                    <p>Copyright &copy; Your Website 2014</p>
                </div>
            </div>
        </footer>

    </div>
    <!-- /.container -->

    <!-- jQuery -->
    <script src="js/jquery.js"></script>

    <!-- Bootstrap Core JavaScript -->
    <script src="js/bootstrap.min.js"></script>

</body>

</html>
