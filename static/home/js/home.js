//Jquery Here
$(document).ready(function () {
    
    $(".notification").click(function(){
        var id=this.id;
        console.log("id:"+id);
        var saveData = $.ajax({
            type: 'POST',
            url: "http://localhost:8000/home/remove_notification",
            data: {'notif_id' : id},
            dataType: "text",

            success: function () {
                console.log("success");
                }
        });
        saveData.error=function(){
            alert("kxcksncks");
        }

    })
    $('.fr_accept').click(function(){
        console.log("accept")
        //call accept function
        var id=this.id
        console.log(id)
        var element=document.getElementById(id);
        console.log(element);
        var parent_id=id.slice(6,id.length);
        var parent_elem=document.getElementById(parent_id);
        console.log(parent_elem);
        
        // Ajax call to add friend request object status to true
        var saveData = $.ajax({
            type: 'POST',
            url: "http://127.0.0.1:8000/home/add_friend_status/",
            data: {'sender_username' : parent_id, 'rec_name' : document.getElementById("loginuser").innerText,'option':'accept'},
            dataType: "text",

            success: function () {
                parent_elem.remove();
                }
        });
        saveData.error=function(){
            alert("kxcksncks");
        }
    })
    $('.fr_reject').click(function(){
        console.log("reject")
        var id=this.id
        console.log(id)
        var element=document.getElementById(id);
        console.log(element);
        var parent_id=id.slice(6,id.length);
        var parent_elem=document.getElementById(parent_id);
        console.log(parent_elem);
        console.log("popopo")
        var saveData = $.ajax({
            type: 'POST',
            url: "http://127.0.0.1:8000/home/add_friend_status/",
            data: {'sender_username' : parent_id, 'rec_name' : document.getElementById("loginuser").innerText,'option':'reject'},
            dataType: "text",

            success: function () {
                console.log("Success deleting")
                parent_elem.remove();
                }
        });
        saveData.error=function(){
            alert("kxcksncks");
        }
    })
    $('.commentsslide').slideUp(1)
    $('.comment').click(
        function () {
            var id = this.id
            id = String(id)
            var final_id = id.match(/\d+/g);
            
            var myKeyVals = { 'post_id': this.id }

            $('#' + 'comment' + final_id[0]).slideToggle(400)
            
        }
    )

    $('.heart_target').click(function () {
        //toggling the heart button
        if (this.classList.contains('far')) {
            this.classList.remove('far')
            this.classList.add('fas')
            console.log(this.id)
            const todo = {
                title: 'Some really important work to finish'
            };
            var hid=this.id;
            var dat=hid.match(/\d+/g)[0]
            var target_post=document.getElementById("pid"+dat)
            console.log(target_post);
            var author_name=target_post.children[0].children[1].children[0].children[0].innerText
            console.log(author_name);
            var liker=document.getElementById("usnm").innerText
            console.log(liker);
            //send a fetch api request saying user having userid = this has liked the post
            var myKeyVals = { 'author_name':author_name, 'liker_name': liker, 'time_liked': Date.now(), 'post_liked': dat }



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
            var hid=this.id;
            var dat=hid.match(/\d+/g)[0]
            var target_post=document.getElementById("pid"+dat)
            console.log(target_post);
            var auth_name=target_post.children[0].children[1].children[0].children[0].innerText
            console.log(auth_name);
            var unliker=document.getElementById("usnm").innerText
            console.log(unliker);
            var myKeyVals = { 'author_name': auth_name, 'unliker_name': unliker, 'time_unliked': Date.now(), 'post_unliked': dat }
            


            var saveData = $.ajax({
                type: 'POST',
                url: "http://127.0.0.1:8000/home/unlike/",
                data: myKeyVals,
                dataType: "text",
                success: function (resultData) {
                    console.log("Post unliked");

                }
            });
            saveData.error(function () { alert("Something went wrong"); });

            //send a fetch api request saying user has disliked the post 
        }
    })
    $('.send_icon').click(function(event){
        var send_icon_id=this.id
        console.log(send_icon_id);
        var id=send_icon_id.match(/\d+/g)[0]
        console.log(id);
        var input=document.getElementById('addcomment'+id)
        console.log(input.value);
        // cmtr=document.getElementById('pid'+id).children[0].children[1].children[0].children[0].innerText
        var liker=document.getElementById("usnm").innerText
        console.log("HASO AUR HASO"+liker);
        event.preventDefault();
        //here need to change and get the owner and  commentor's name
        var myKeyVals={'comentr':liker,'comment':input.value,'post_id':id};
        var saveData = $.ajax({
            type: 'POST',
            url: "http://127.0.0.1:8000/home/add_comment/",
            data: myKeyVals,
            dataType: "text",
            success: function (resultData) {
                console.log("Added comment to post");
                input.value=""
                
                //Task remaining make a element of li and then append it befor 1 elem of list
            }
        });
        saveData.error(function () { alert("Oops wait for the server to start"); });
        
    })
}
)




// var myKeyVals = { 'author_name': 'authors_name', 'liker_name': 'liker', 'time_liked': Date.now(), 'post_liked': 'id_of_post' }



//             var saveData = $.ajax({
//                 type: 'POST',
//                 url: "http://127.0.0.1:8000/home/like/",
//                 data: myKeyVals,
//                 dataType: "text",
//                 success: function (resultData) { console.log("Post liked"); }
//             });
//             saveData.error(function () { alert("Something went wrong"); });