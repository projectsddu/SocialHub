$(document).ready(function () {
    $('.commentsslide').slideUp(1)
    $('.comment').click(
        function () {
            var myKeyVals = { 'post_id':this.id}

            $('.commentsslide').slideToggle(400)
            var saveData = $.ajax({
                type: 'POST',
                url: "http://127.0.0.1:8000/home/comments/",
                data: myKeyVals,
                dataType: "text",
                success: function (resultData) { console.log(JSON.parse(resultData)['comments'][0]); }
            });
            saveData.error(function () { alert("Something went wrong"); });
        }
    )
    for (let i = 0; i < 3; i++) {
        $('#p' + i).click(function () {
            //toggling the heart button
            if (this.classList.contains('far')) {
                this.classList.remove('far')
                this.classList.add('fas')
                console.log(this.id)
                const todo = {
                    title: 'Some really important work to finish'
                };

                //send a fetch api request saying user having userid = this has liked the post
                var myKeyVals = { 'author_name': 'authors_name', 'liker_name': 'liker', 'time_liked': Date.now(), 'post_liked': 'id_of_post' }



                var saveData = $.ajax({
                    type: 'POST',
                    url: "http://127.0.0.1:8000/home/like/",
                    data: myKeyVals,
                    dataType: "text",
                    success: function (resultData) { console.log("Post liked"); }
                });
                saveData.error(function () { alert("Something went wrong"); });
            }
            else {
                this.classList.remove('fas')
                this.classList.add('far')
                var myKeyVals = { 'author_name': 'authors_name', 'unliker_name': 'liker', 'time_liked': Date.now(), 'post_unliked': 'id_of_post' }



                var saveData = $.ajax({
                    type: 'POST',
                    url: "http://127.0.0.1:8000/home/unlike/",
                    data: myKeyVals,
                    dataType: "text",
                    success: function (resultData) { console.log("Post unliked"); }
                });
                saveData.error(function () { alert("Something went wrong"); });

                //send a fetch api request saying user has disliked the post 
            }
        })
    }
})




// var myKeyVals = { 'author_name': 'authors_name', 'liker_name': 'liker', 'time_liked': Date.now(), 'post_liked': 'id_of_post' }



//             var saveData = $.ajax({
//                 type: 'POST',
//                 url: "http://127.0.0.1:8000/home/like/",
//                 data: myKeyVals,
//                 dataType: "text",
//                 success: function (resultData) { console.log("Post liked"); }
//             });
//             saveData.error(function () { alert("Something went wrong"); });