<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="WebForm1.aspx.cs" Inherits="WebApplication1.WebForm1" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
    <script src="Scripts/jquery-3.5.1.js"></script>

    <script type="text/javascript">
        $(document).ready(function () {
            $("#btn").click(function () {
                var num1 = $("#txt1").val();
                var num2 = $("#txt2").val();

                $.ajax({
                    url: "Service1.svc/Sum",
                    type: "POST",
                    contentType: "application/json; charset=utf-8",
                    data: JSON.stringify({ a: num1, b: num2 }),
                    dataType: "json",
                    success: function (data) {
                        $("#txt3").val(data.d);
                    },
                    error: function (err) {
                        alert(err);
                    }
                });
            });
        });
    </script>
</head>
<body>
    <form id="form1" runat="server">
        <div>
            <input id="txt1" type="text" /> &nbsp;
            <input id="txt2" type="text" />&nbsp;
            <input id="btn" type="button"  value="Add numbers" /> <br /><br />
            <input id="txt3" type="text" /> <br />
        </div>
    </form>
</body>
</html>
