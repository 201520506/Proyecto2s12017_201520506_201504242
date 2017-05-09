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
@WebServlet(urlPatterns = {"/servletEliminar"})
public class servletEliminar extends HttpServlet {

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
         HttpSession session  = request.getSession(true);
        if(request.getParameter("ev") != null &&
           request.getParameter("di") != null &&
           request.getParameter("dr") != null &&
           request.getParameter("de") != null &&
           request.getParameter("ho") != null){
            try{
            String ev = request.getParameter("ev");
            String di =request.getParameter("di");
            String dr = request.getParameter("dr");
            String de =request.getParameter("de") ;
            String ho = request.getParameter("ho") ;
            String bol = (String)session.getAttribute("bool");
            String mes =(String)session.getAttribute("mess");
            String ano = (String)session.getAttribute("anoo");
            
            String usuario = (String)session.getAttribute("usuario");
            sendGet(ev,di,dr,de,ho,usuario,bol,mes,ano);
            } catch (Exception ex) {
                System.out.println(ex.getMessage());
                response.sendRedirect("index.jsp");
            }
            
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
private void sendGet(String ev, String di, String dr, String de, String ho, String usu, String bol, String mes, String ano) throws Exception {
		String url = puerto+"eliminarEvento?usu="+usu+"&&evento="+ev+"&&dia="+di+"&&mes="+mes+"&&ano="+ano+"&&direc="+dr+"&&desc="+de+"&&hora="+ho+"&&eli="+bol;
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
