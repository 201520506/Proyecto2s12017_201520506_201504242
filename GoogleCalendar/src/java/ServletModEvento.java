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
@WebServlet(urlPatterns = {"/ServletModEvento"})
public class ServletModEvento extends HttpServlet {
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
        if(request.getParameter("Neve") != null &&
           request.getParameter("Ndia") != null &&
           request.getParameter("Ndir") != null &&
           request.getParameter("Ndes") != null &&
           request.getParameter("Nhor") != null){
           try {
            //datos anterirores
           String Eveeve = (String)session.getAttribute("evento");
           String Evedia = (String)session.getAttribute("dia");
           String Evedireccion = (String)session.getAttribute("direccion");
           String Evedes = (String)session.getAttribute("des");
           String Evehora = (String)session.getAttribute("hora");
           String EveBool = (String)session.getAttribute("bool");
           String mes =(String)session.getAttribute("mess");
           String ano = (String)session.getAttribute("anoo");
           //datos nuevos
           String Neve = (String)request.getParameter("Neve");
           String Ndia = (String)request.getParameter("Ndia");
           String Ndir = (String)request.getParameter("Ndir");
           String Ndes = (String)request.getParameter("Ndes");
           String Nhor = (String)request.getParameter("Nhor");
           String usuario = (String)session.getAttribute("usuario");
        
           sendGet(mes,ano,EveBool,usuario,Eveeve,Evedia,Evedireccion,Evedes,Evehora,Neve,Ndia,Ndir,Ndes,Nhor);
            } catch (Exception ex) {
                System.out.println(ex.getMessage());
                response.sendRedirect("index.jsp");
            }
           try (PrintWriter out = response.getWriter()) {
            if(imp.equals("pelado")){
                response.sendRedirect("principal.jsp");       
            }else{
                response.sendRedirect("index.jsp");           
            }
           }
        }
        
        try (PrintWriter out = response.getWriter()) {
            /* TODO output your page here. You may use following sample code. */
            out.println("<!DOCTYPE html>");
            out.println("<html>");
            out.println("<head>");
            out.println("<title>Servlet ServletModEvento</title>");            
            out.println("</head>");
            out.println("<body>");
            out.println("<h1>Servlet ServletModEvento No se capturaron todos los datos </h1>");
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
private void sendGet(String Evemes,String Eveano,String Evestado,String usua,String Eveeve, String Evedia, String Evedireccion, String Evedes, String Evehora, String Neve, String Ndia, String Ndir, String Ndes, String Nhor) throws Exception {
		String url = puerto+"modificarEvento?usu="+usua+"&&Aevento="+Eveeve+"&&Adia="+Evedia+
                        "&&Ames="+Evemes+"&&Aano="+Eveano+"&&Adirec="+Evedireccion+"&&Ahora="+Evehora+"&&Adesc="+Evedes
                        +"&&Aestado="+Evestado+"&&Nevento="+Neve+"&&Nfecha="+Ndia+"&&Ndirec="+Ndir+"&&Ndesc="+Ndes+"&&Nhora="+Nhor;
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
