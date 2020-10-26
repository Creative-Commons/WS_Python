using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace ArithmeticClient
{
    public partial class WebForm1 : System.Web.UI.Page
    { 
        protected void Button1_Click(object sender, EventArgs e)
        {
            ServiceReference1.IService1 ob = new ServiceReference1.Service1Client();
            int num1 = int.Parse(TextBox1.Text);
            int num2 = int.Parse(TextBox2.Text);

            TextBox3.Text = Convert.ToString(ob.Sum(num1, num2));
        }

        protected void Button2_Click(object sender, EventArgs e)
        {
            ServiceReference1.IService1 ob = new ServiceReference1.Service1Client();
            int num1 = int.Parse(TextBox1.Text);
            int num2 = int.Parse(TextBox2.Text);

            TextBox3.Text = Convert.ToString(ob.Multiply(num1, num2));
        }
    }
}