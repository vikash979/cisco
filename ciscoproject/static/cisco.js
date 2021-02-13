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
        var hostname = $('#hostname').val()
        var macadd = $('#macadd').val()
        
       // var datString = JSON.stringify({"username":username,"password":password})
        var urll= '/user/update_event/'
          $.ajax({
            url : urll, // the endpoint
            type : "GET", // http method
            data:'ip='+username+'&&hostname='+hostname+'&&macadd='+macadd,
            //data : { postpk : post_primary_key }, // data sent with the delete request
            success : function(json) {
              alert("Updated Successfully")
              window.location.href = "/user/tokenapp/";
            },
          })


}


function textsearch(id)
{
  var searchid = "#"+id
  var searchs = $(searchid).val()

  
  var datString = JSON.stringify({"search":searchs})
     var urll= '/user/toc_model/'
          $.ajax({
            url : urll, // the endpoint
            type : "GET", // http method
            data: {
              'search': searchs // from form
            },
            //data : { postpk : post_primary_key }, // data sent with the delete request
            success : function(response) {
              if (searchs.length>1)
              {
                $('#routerdata').empty()
                 for(var i = 0; i <response.length; i++)
                {
                   $('#routerdata').append(`<tr><td>${response[i]['ip']}</td><td>${response[i]['hostname']}</td><td><a href="/user/tokenupdate/?id=${response[i]['id']}" >Edit </a>|| <a href="#" id="delete_${response[i]['id']}" onclick="routerdelete(this.id)">Delete</a></td></tr>`)
       
                }

              }
              else{
                $('#routerdata').empty()
                for(var i = 0; i <response.length; i++)
                {
                   $('#routerdata').append(`<tr><td>${response[i]['ip']}</td><td>${response[i]['hostname']}</td><td><a href="/user/tokenupdate/?id=${response[i]['id']}" >Edit </a>|| <a href="#" id="delete_${response[i]['id']}" onclick="routerdelete(this.id)">Delete</a></td></tr>`)
       
                }
              }
              
             // window.location.href = "/user/tokenapp/";
            },
          })
}


function totaltimes()
{
  $('#nrouterdata').empty()
  var number  = $('#totl').val()
  for (i = 1; i <= number; i++) {
  $('#nrouterdata').append(`<tr><td><input type="text" class="form-control" id="sapid_${i}" placeholder="Enter sapid" name="sapid_${i}"></td>
    <td><input type="text" class="form-control" id="ip_${i}" placeholder="Enter loopback" name="ip_${i}"></td>
    <td><input type="text" class="form-control" id="hostname_${i}" placeholder="Enter Hostname" name="hostname_${i}"></td>
    
    <td><input type="text" class="form-control" id="mcadd_${i}" placeholder="Enter Mac Address" name="mcadd_${i}"></td></tr>`)
}
}




$(document).on('click', '#nsubmit', function(e) {
  var number  = $('#totl').val()
  ob = []
  
  for (i = 1; i <= number; i++) {
    var obj = {};
    var host = "#hostname_"+i
    var hostname = $(host).val()
    var ipp = $('#ip_'+i).val()
    var sapid = $('#sapid_'+i).val()
    obj['host']=$(host).val()
    obj['mcadd'] = $('#mcadd_'+i).val()
    var macadd = $('#mcadd_'+i).val()
    var sapid = $('#sapid_'+i).val()
     obj['ip']=ipp

     obj['sapid'] =sapid


    //var ee = 'ip='+ipp+'&&hostname='+hostname+'&&macadd='+macadd+'&&sapid='+sapid
    //alert(ee)
    ob.push(obj)
    var datString = JSON.stringify(obj)
   // alert(datString)
      $.ajax({
        url:  '/user/nrouter/',
        contentType : 'application/json',

        type: "GET",

        data:'ip='+ipp+'&&hostname='+hostname+'&&macadd='+macadd+'&&sapid='+sapid,
        beforeSend: function (xhr, settings) {
           xhr.setRequestHeader("X-CSRFToken", '{{ csrf_token }}');
       },
        success: function(response){
          window.location.href = "/user/tokenapp/";

        }
      })
  }


  })