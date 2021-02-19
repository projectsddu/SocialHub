

$(document).ready(function () {
    document.addEventListener('keyup', function (event) {

        var search_data = document.getElementById("search_query").value
        console.log(search_data)
        setTimeout(function () { }, 100);
        var myKeyVals = { 'data': search_data }
        var saveData = $.ajax({
            type: 'POST',
            url: "http://127.0.0.1:8000/search/search_result",
            data: JSON.stringify(myKeyVals),
            dataType: "text",

            success: function (resultData) {

                var len_data = resultData
                len_data = JSON.parse(resultData)['post']
                var populating_element = document.getElementById("search_res");
                populating_element.innerHTML = "";
                console.log(len_data)
                for (data in len_data) {
                    var search_username = len_data[data].username
                    var search_photo = "http://localhost:8000" + len_data[data].photo_url
                    // console.log(search_photo)
                    var elem = document.createElement("li")
                    elem.setAttribute("class", "list-group-item");
                    elem.innerHTML = "<img class='rounded-circle' style='width:60px;height:60px;border:1px solid black;border-radius: 50%;object-fit: cover;' src='" + search_photo + "'> <span style='font-size:20px;padding-left:20px'>" + search_username + "</span>";
                    populating_element.appendChild(elem);


                }



            }
        });


    })
}
)