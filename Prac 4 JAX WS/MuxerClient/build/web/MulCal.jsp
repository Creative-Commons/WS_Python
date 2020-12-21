<%-- 
    Document   : MulCal
    Created on : 21-Dec-2020, 21:53:09
    Author     : nassqra
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>MuxerJSP</title>
    </head>
    <body>
        
    <%-- start web service invocation --%><hr/>
    <%
        int iv = Integer.parseInt(request.getParameter("txt1"));
        int jv = Integer.parseInt(request.getParameter("txt2"));
    try {
	org.mul.MulS_Service service = new org.mul.MulS_Service();
	org.mul.MulS port = service.getMulSPort();
	 // TODO initialize WS operation arguments here
	int i = iv;
	int j = jv;
	// TODO process result here
	int result = port.muxing(i, j);
	out.println("Multiplied = "+result);
    } catch (Exception ex) {
	// TODO handle custom exceptions here
    }
    %>
    <%-- end web service invocation --%><hr/>
    </body>
</html>
