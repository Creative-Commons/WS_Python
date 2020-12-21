/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package org.mul;

import javax.jws.WebService;
import javax.jws.WebMethod;
import javax.jws.WebParam;
import javax.ejb.Stateless;

/**
 *
 * @author nassqra
 */
@WebService(serviceName = "MulS")
@Stateless()
public class MulS {

    /**
     * Web service operation
     */
    @WebMethod(operationName = "muxing")
    public int muxing(@WebParam(name = "i") int i, @WebParam(name = "j") int j) {
        //TODO write your implementation code here:
        return i * j;
    }
}
