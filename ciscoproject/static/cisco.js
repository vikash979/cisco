$(window).on('load',function(){
		  $.ajax({
      type: "GET",
      url: "/user/toc_model/",
      data: {
        'video': "kjk" // from form
      },
      success: function(response){
        //alert(JSON.stringify(response))
        for (var i =0; i<response.length;i++)
        {
           $('#routerdata').append(`<tr><td>${response[i]['ip']}</td><td>${response[i]['hostname']}</td><td><a href="/user/tokenupdate/?id=${response[i]['id']}" >Edit </a>|| <a href="#" id="delete_${response[i]['id']}" onclick="routerdelete(this.id)">Delete</a></td></tr>`)
        }
       
        //$('#message').html("<h2>Contact Form Submitted!</h2>")
      }
    });

})


function generateToken() {

  var username = document.getElementById("username").value
        var password =$('#password').val()
        var datString = JSON.stringify({"username":username,"password":password})
        var BASE_SITE_URL = "http://127.0.0.1:8000"
  var urll= BASE_SITE_URL + '/user/routerdata/'


  $.ajax({
      type: "POST",
     
     url:'/user/routerdata/',

    type: "POST",

    data:'ip='+username+'&&hostname='+password,
    
      // beforeSend: function (xhr, settings) {
      //                                           xhr.setRequestHeader("X-CSRFToken", '{{ csrf_token }}');
      //                                       },
      success: function(response){
        alert(response)
        //$('#message').html("<h2>Contact Form Submitted!</h2>")
      }
    });
}

function routerdelete(idd)
{
  var dataId= idd.split("_")
  var iddd = dataId[1]
  var BASE_SITE_URL = "http://127.0.0.1:8000"
  var urll= '/user/delete_event/'+iddd+"/"

$.ajax({
            url : urll, // the endpoint
            type : "GET", // http method
            //data : { postpk : post_primary_key }, // data sent with the delete request
            success : function(json) {
              window.location.href = "/user/tokenapp/";
                // hide the post
              //$('#post-'+post_primary_key).hide(); // hide the post on success
              console.log("post deletion successful");
            },
          })
}


function routerupdate()
{
  var username = document.getElementById("username").value
        var password =$('#password').val()
        var datString = JSON.stringify({"username":username,"password":password})
        var urll= '/user/update_event/'
          $.ajax({
            url : urll, // the endpoint
            type : "GET", // http method
            data:'ip='+username+'&&hostname='+password,
            //data : { postpk : post_primary_key }, // data sent with the delete request
            success : function(json) {
              alert("Updated Successfully")
              window.location.href = "/user/tokenapp/";
            },
          })


}