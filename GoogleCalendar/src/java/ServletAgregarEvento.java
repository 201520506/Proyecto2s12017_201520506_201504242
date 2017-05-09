/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import com.squareup.okhttp.Response;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.HttpURLConnection;
import java.net.URL;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

/**
 *
 * @author p_ab1
 */
@WebServlet(urlPatterns = {"/ServletAgregarEvento"})
public class ServletAgregarEvento extends HttpServlet {
 private final String puerto ="http://127.0.0.1:8000/";
    Response respuesta;
    String imp;
    /**
     * Processes requests for both HTTP <code>GET</code> and <code>POST</code>
     * methods.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    protected void processRequest(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        response.setContentType("text/html;charset=UTF-8");
        
        if(request.getParameter("nombre")!=null 
                && request.getParameter("desc")!=null
                && request.getParameter("direc")!=null
                && request.getParameter("hora")!=null
                && request.getParameter("dia2")!=null
                && request.getParameter("mes2")!=null
                && request.getParameter("ano2")!=null){
        String nombre = request.getParameter("nombre");
        String desc = request.getParameter("desc");
        String direc= request.getParameter("direc");
        String hora =request.getParameter("hora");
        String dia = request.getParameter("dia2");
        String mes= request.getParameter("mes2");
        String ano = request.getParameter("ano2");
        HttpSession session  = request.getSession(true);
        String usuario = (String)session.getAttribute("usuario");
        String fecha = dia+"/"+mes+"/"+ano;
        String contra = (String)session.getAttribute("contra");
        
         try {
                sendGet(mes,ano,usuario,fecha,desc,nombre,direc,hora,contra,dia);
            } catch (Exception ex) {
                System.out.println(ex.getMessage());
            }
        }
        if(imp.equals("ok")){
            response.sendRedirect("principal.jsp");
        }else{
             response.sendRedirect("mala.jsp");
        }
        try (PrintWriter out = response.getWriter()) {
            /* TODO output your page here. You may use following sample code. */
            out.println("<!DOCTYPE html>");
            out.println("<html>");
            out.println("<head>");
            out.println("<title>Servlet ServletAgregarEvento</title>");            
            out.println("</head>");
            out.println("<body>");
            out.println("<h1>Servlet ServletAgregarEvento at " + request.getContextPath() + "</h1>");
            out.println("</body>");
            out.println("</html>");
        }
    }

    // <editor-fold defaultstate="collapsed" desc="HttpServlet methods. Click on the + sign on the left to edit the code.">
    /**
     * Handles the HTTP <code>GET</code> method.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        processRequest(request, response);
    }

    /**
     * Handles the HTTP <code>POST</code> method.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        processRequest(request, response);
    }

    /**
     * Returns a short description of the servlet.
     *
     * @return a String containing servlet description
     */
    @Override
    public String getServletInfo() {
        return "Short description";
    }// </editor-fold>
private void sendGet(String a,String b,String c,String d,String f
        ,String g,String h,String i,String contra,String dia) throws Exception {
		String url = puerto+"insertarEvento?mes="+a+"&&ano="+b+"&&usu="+c+"&&fecha="+d
                        +"&&desc="+f+"&&evento="+g+"&&direc="+h+
                        "&&hora="+i+"&&contra="+contra+"&&dia="+dia;
		URL obj = new URL(url);
		HttpURLConnection con = (HttpURLConnection) obj.openConnection();
		con.setRequestMethod("GET");
		con.setRequestProperty("User-Agent", "k");
		int responseCode = con.getResponseCode();
		System.out.println("\nSending 'GET' request to URL : " + url);
		System.out.println("Response Code : " + responseCode);
		BufferedReader in = new BufferedReader(
		        new InputStreamReader(con.getInputStream()));
		String inputLine;
		StringBuffer response = new StringBuffer();

		while ((inputLine = in.readLine()) != null) {
			response.append(inputLine);
		}
		in.close();
                imp=response.toString();
		//print result
		System.out.println(response.toString());

	}
}
