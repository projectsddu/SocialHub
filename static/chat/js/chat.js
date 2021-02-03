
document.querySelector("#msg_area").onkeyup = function (event) {
    if (event.keyCode == 13) {
        document.querySelector("#send_icon").click();
    }
}
document.querySelector("#send_icon").onclick = function (e) {
    const msg_dom = document.querySelector("#msg_area")
    const msg = msg_dom.value

    ws.send(JSON.stringify({
        'message': msg
    }))
    msg_dom.value = ""


}
var ws = new WebSocket('ws://localhost:8000/ws/chat/jenil_keval')
ws.onopen = function (event) {
    alert("connection successful!")

}
ws.onmessage = function (event) {
    var today = new Date();
    var time = today.getHours() + ":" + today.getMinutes();


    var recdata = JSON.parse(event.data)
    var msgdom = document.getElementById("chat");
    console.log(msgdom);
    var newelement = document.createElement('li');
    var att = document.createAttribute("class")
    var name = recdata['sender']
    var color = "#ff725d";
    var color_name = "orange"
    var ourname = document.getElementById("cur_user").innerText;
    console.log(ourname);
    if (name == ourname) {
        att.value = "me"
        color = "#6fbced"
        color_name = "blue"
        newelement.innerHTML = '<div class="entete"><h2 style="color:' + color + '">' + name +
            '</h2><h3>. ' + time + '</h3><span class="status ' + color_name +
            '"></span></div><div class="message"><pre>' + recdata['message'] + '</pre></div>';
    } else {
        att.value = "you"
        newelement.innerHTML = '<div class="entete"><span class="status ' + color_name +
            '"></span><h2 style="color:' + color + '">' + name +
            ' </h2><h3>. ' + time + ' </h3></div><div class="message"><pre>' + recdata['message'] +
            '</pre></div>';

    }
    newelement.setAttributeNode(att);

    msgdom.appendChild(newelement);
    var chat_elem = document.getElementById("chat")
    chat_elem.scrollTop = chat_elem.scrollHeight;
}
