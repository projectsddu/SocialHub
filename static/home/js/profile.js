
$(document).ready(function() {
    $("#fr_button").click(function() {
        // console.log("click")

        var element = document.getElementById("fr_button");
        var text = element.innerText
        // console.log(text)
        if(text == "Send Friend Request") {
            element.innerText = "Friend Request Sent"
            element.setAttribute("class","sent")   
        }
        else {
            element.innerText = "Send Friend Request"
            element.setAttribute("class","send")   
        }
    })
})