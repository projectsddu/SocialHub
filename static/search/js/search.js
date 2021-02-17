

$(document).ready(function () {
    document.addEventListener('keyup', function (event) {

        var search_data = document.getElementById("search_query")
        console.log(search_data.value)


        // var myKeyVals={'search_query': search_data};
        // var saveData = $.ajax({
        //     type: 'POST',
        //     url: "http://localhost:8000/search/search_result",
        //     data: myKeyVals,
        //     dataType: "text",
        //     success: function (resultData) {
        //         console.log("keval");
        //         // input.value=""

        //         //Task remaining make a element of li and then append it befor 1 elem of list
        //     }
        // });
        // saveData.error(function () { alert("Oops wait for the server to start"); });


        // $.post("http://localhost:8000/search/search_result",
        //     {
        //         search_query: search_data
        //     },
        //     function (data, status) {
        //         alert("Data: " + data + "\nStatus: " + status);
        //     });

        var submitData = {search_query: search_data}
        $.ajax({
            type: 'post', 
            url: 'http://localhost:8000/search/search_result', 
            data: JSON.stringify(submitData), // stringyfy before passing
            dataType: 'json', // payload is json
            contentType : 'application/json',
            success: function (data) {
                console.log(data);
                }
            });

    })
}
)