
package org.mul;

import javax.jws.WebMethod;
import javax.jws.WebParam;
import javax.jws.WebResult;
import javax.jws.WebService;
import javax.xml.bind.annotation.XmlSeeAlso;
import javax.xml.ws.Action;
import javax.xml.ws.RequestWrapper;
import javax.xml.ws.ResponseWrapper;


/**
 * This class was generated by the JAX-WS RI.
 * JAX-WS RI 2.2.6-1b01 
 * Generated source version: 2.2
 * 
 */
@WebService(name = "MulS", targetNamespace = "http://mul.org/")
@XmlSeeAlso({
    ObjectFactory.class
})
public interface MulS {


    /**
     * 
     * @param i
     * @param j
     * @return
     *     returns int
     */
    @WebMethod
    @WebResult(targetNamespace = "")
    @RequestWrapper(localName = "muxing", targetNamespace = "http://mul.org/", className = "org.mul.Muxing")
    @ResponseWrapper(localName = "muxingResponse", targetNamespace = "http://mul.org/", className = "org.mul.MuxingResponse")
    @Action(input = "http://mul.org/MulS/muxingRequest", output = "http://mul.org/MulS/muxingResponse")
    public int muxing(
        @WebParam(name = "i", targetNamespace = "")
        int i,
        @WebParam(name = "j", targetNamespace = "")
        int j);

}
