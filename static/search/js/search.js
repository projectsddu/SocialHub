

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
                console.log(typeof (len_data.length))
                if (len_data.length == 0) {
                    var elem = document.createElement("li")
                    elem.setAttribute("class", "list-group-item");
                    elem.innerHTML = "<h3>Sorry no results found</h3>"
                    populating_element.appendChild(elem);
                }
                for (data in len_data) {
                    var search_username = len_data[data].username
                    // console.log(search_username + "keval")
                    var search_photo = "http://localhost:8000" + len_data[data].photo_url
                    // console.log(search_photo)
                    var elem = document.createElement("li")
                    elem.setAttribute("class", "list-group-item");
                    elem.innerHTML = "<img class='rounded-circle user_img'  src='" + search_photo + "'>  <span style='font-size:20px;padding-left:20px' class='custom_text'><a style='text-decoration:none;color:black' href='http://localhost:8000/home/users/" + search_username + "' >" + search_username + "</a></span>";
                    populating_element.appendChild(elem);

                }



            }

        });

        saveData.error(function () {
            var populating_element = document.getElementById("search_res");
            var elem = document.createElement("li")
            populating_element.innerHTML = "";
            elem.setAttribute("class", "list-group-item");
            elem.innerHTML = "<h3>Sorry no results found</h3>"
            populating_element.appendChild(elem);
        })
    })
}
)