
package org.mul;

import javax.xml.bind.JAXBElement;
import javax.xml.bind.annotation.XmlElementDecl;
import javax.xml.bind.annotation.XmlRegistry;
import javax.xml.namespace.QName;


/**
 * This object contains factory methods for each 
 * Java content interface and Java element interface 
 * generated in the org.mul package. 
 * <p>An ObjectFactory allows you to programatically 
 * construct new instances of the Java representation 
 * for XML content. The Java representation of XML 
 * content can consist of schema derived interfaces 
 * and classes representing the binding of schema 
 * type definitions, element declarations and model 
 * groups.  Factory methods for each of these are 
 * provided in this class.
 * 
 */
@XmlRegistry
public class ObjectFactory {

    private final static QName _Muxing_QNAME = new QName("http://mul.org/", "muxing");
    private final static QName _MuxingResponse_QNAME = new QName("http://mul.org/", "muxingResponse");

    /**
     * Create a new ObjectFactory that can be used to create new instances of schema derived classes for package: org.mul
     * 
     */
    public ObjectFactory() {
    }

    /**
     * Create an instance of {@link Muxing }
     * 
     */
    public Muxing createMuxing() {
        return new Muxing();
    }

    /**
     * Create an instance of {@link MuxingResponse }
     * 
     */
    public MuxingResponse createMuxingResponse() {
        return new MuxingResponse();
    }

    /**
     * Create an instance of {@link JAXBElement }{@code <}{@link Muxing }{@code >}}
     * 
     */
    @XmlElementDecl(namespace = "http://mul.org/", name = "muxing")
    public JAXBElement<Muxing> createMuxing(Muxing value) {
        return new JAXBElement<Muxing>(_Muxing_QNAME, Muxing.class, null, value);
    }

    /**
     * Create an instance of {@link JAXBElement }{@code <}{@link MuxingResponse }{@code >}}
     * 
     */
    @XmlElementDecl(namespace = "http://mul.org/", name = "muxingResponse")
    public JAXBElement<MuxingResponse> createMuxingResponse(MuxingResponse value) {
        return new JAXBElement<MuxingResponse>(_MuxingResponse_QNAME, MuxingResponse.class, null, value);
    }

}
