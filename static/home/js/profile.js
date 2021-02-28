
$(document).ready(function() {
    $("#fr_button").click(function() {
        // console.log("click")

        var element = document.getElementById("fr_button");
        var text = element.innerText
        // console.log(text)
        if(text == "Send Friend Request") {
            element.innerText = "Friend Request Sent"
            element.setAttribute("class","sent")

            // var myKeyVals = {'destination_user': "jenilgandhi"}//document.getElementById("cur_user").innerText}

            // var saveData = $.ajax({
            //     type: 'POST',
            //     url: 'http://127.0.0.1:8000/home/add_friend/',
            //     data: myKeyVals,
            //     dataType: 'text',
            //     success: function () { 
            //         // console.log(JSON.parse(resultData)['comments']);
            //         // var commentdata=JSON.parse(resultData)['comments']
            //         console.log("success")
                    
            //     }
            //   });
            // saveData.error(function () { alert("Something went wrong"); });

            var saveData = $.ajax({
                type: 'POST',
                url: "http://127.0.0.1:8000/home/add_friend/",
                data: {'destination_user' : document.getElementById("cur_user").innerText, 'sender_username' : document.getElementById("loginuser").innerText,'option':'friend'},
                dataType: "text",
    
                success: function () {
                        console.log("Success")
                    }
            });
            saveData.error=function(){
                alert("kxcksncks");
            }
        }
        else if(element.innerText=="Followed")
        {
            var saveData = $.ajax({
                type: 'POST',
                url: "http://127.0.0.1:8000/home/add_friend/",
                data: {'destination_user' : document.getElementById("cur_user").innerText, 'sender_username' : document.getElementById("loginuser").innerText,'option':'unfriend'},
                dataType: "text",
    
                success: function () {
                        console.log("Success")
                    }
            });
            saveData.error=function(){
                alert("kxcksncks");
            }
            element.innerText="Send Friend Request"
        }
        else {
            var saveData = $.ajax({
                type: 'POST',
                url: "http://127.0.0.1:8000/home/add_friend/",
                data: {'destination_user' : document.getElementById("cur_user").innerText, 'sender_username' : document.getElementById("loginuser").innerText,'option':'unfriend'},
                dataType: "text",
    
                success: function () {
                        console.log("Success")
                    }
            });
            saveData.error=function(){
                alert("kxcksncks");
            }
            
            element.innerText = "Send Friend Request"
            element.setAttribute("class","send")   
        }
    })
})