using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Services;

namespace Prac4
{
    /// <summary>
    /// Summary description for Operation
    /// </summary>
    [WebService(Namespace = "http://tempuri.org/")]
    [WebServiceBinding(ConformsTo = WsiProfiles.BasicProfile1_1)]
    [System.ComponentModel.ToolboxItem(false)]
    // To allow this Web Service to be called from script, using ASP.NET AJAX, uncomment the following line. 
    // [System.Web.Script.Services.ScriptService]
    public class Operation : System.Web.Services.WebService
    {
        [WebMethod]
        public double Add(double a, double b)
        {
            double sum = a + b;
            return sum;
        }
        [WebMethod]
        public double Multiply(double a, double b)
        {
            double mul = a * b;
            return mul;
        }
    }
}
