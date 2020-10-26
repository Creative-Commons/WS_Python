using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.Serialization;
using System.ServiceModel;
using System.ServiceModel.Web;
using System.Text;

namespace ArithmeticOperation
{
    [ServiceContract]
    public interface IService1
    {

        [OperationContract]
        int Sum(int val1, int val2);

        [OperationContract]
        int Multiply(int val1, int val2);

        // TODO: Add your service operations here
    }
}
