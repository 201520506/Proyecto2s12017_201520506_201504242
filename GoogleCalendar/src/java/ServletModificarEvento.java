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
@WebServlet(urlPatterns = {"/ServletModificarEvento"})
public class ServletModificarEvento extends HttpServlet {
    private final String puerto ="http://127.0.0.1:8000/";
    Response respuesta;
    String imp,qr;
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
        String usuario = (String)session.getAttribute("usuario");
        String evento = request.getParameter("evento");
        String fecha = request.getParameter("fecha");
        String a[]=fecha.split("/");  
        session.setAttribute("mess", a[1]);
        session.setAttribute("anoo", a[2]);
        try {
                sendGet(usuario,evento,a[0],a[1],a[2]);                 
            } catch (Exception ex) {
                System.out.println(ex.getMessage());
            }
        try {
            createQR(imp);
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
        
        if(!imp.equals("None")){
            String vector[] = imp.split(",");
            session.setAttribute("evento", vector[0]);
            session.setAttribute("dia", vector[1]);
            session.setAttribute("direccion", vector[2]);
            session.setAttribute("des", vector[3]);
            session.setAttribute("hora", vector[4]);
            session.setAttribute("bool", vector[5]);
            session.setAttribute("bandera",false );
            response.sendRedirect("principal.jsp");
            //out.println("<h1>"+imp+"</h1>");
            //response.sendRedirect("principal.jsp");     
        }else{
            /* TODO output your page here. You may use following sample code. */
            session.setAttribute("bandera",true );
            response.sendRedirect("principal.jsp");
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
private void sendGet(String usu,String evento,String dia,String mes,String ano) throws Exception {
		String url = puerto+"getNodoEvento?evento="+evento+"&&dia="+dia+"&&mes="+mes+
                        "&&ano="+ano+"&&usu="+usu;
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
private void createQR(String datos) throws Exception {
		String url = puerto+"crearQR?datos="+datos;
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
                qr=response.toString();
		//print result
		System.out.println(response.toString());

	}
}
