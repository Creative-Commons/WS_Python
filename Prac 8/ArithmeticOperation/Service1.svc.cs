using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.Serialization;
using System.ServiceModel;
using System.ServiceModel.Web;
using System.Text;

namespace ArithmeticOperation
{
    public class Service1 : IService1
    {
        public int Sum(int val1, int val2)
        {
            return val1 + val2;
        }

        public int Multiply(int val1, int val2)
        {
            return val1 * val2;
        }
    }
}
