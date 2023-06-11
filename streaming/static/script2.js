 $(document).ready(function() {

   function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
          var cookies = document.cookie.split(';');
          for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
            }
          }
        }
        return cookieValue;
      }

   var currentSource = null;

   $('#dataSource').on('change', function() {
    var source = $(this).val();
    
    if(source=="youtube"){
      $("#youtube-url").prop('disabled', false);
     }
     else{
      $("#youtube-url").prop('disabled', true);
     }
    
    // Call a function or execute code here
    // when the select option changes
  });

   $("#source").click(function() {
        var source = $("#dataSource").val()
        var sourceText = $('#dataSource option:selected').text();
        

        if(source=="none"){
         $("#sourceErr").text("     Please select one source     ")
        }
        else{
         currentSource = source
         if(currentSource!=null){
            // kill source
         }
         var csrfToken = getCookie('csrftoken');
         var postData = {
            "source": source
          }; 
          if(source=="youtube"){
            var url = $("#youtube-url").val()
            if (url == ""){
               $("#sourceErr").text("     Please add youtube url     ")
               return
            }
            else{
               postData.url = url

            }
          }
         $("#transcript").prepend("<p style='color: red;'> Source Changed to:" +sourceText +"</p>")

          $.ajax({
            type: "POST",
            url: "/add-source/",
            data: postData,
            beforeSend: function(xhr) {
              xhr.setRequestHeader("X-CSRFToken", csrfToken);
            },
            success: function(response) {
              console.log(response);
            },
            error: function(xhr, status, error) {
              console.log(xhr.responseText);
            }
          });
        }
   });

   $("#sourceStop").click(function() {
         if(currentSource!=null){
            // kill source

            var csrfToken = getCookie('csrftoken');
            var postData = {
               "source": currentSource
             }; 
             $.ajax({
               type: "POST",
               url: "/kill-source/",
               data: postData,
               beforeSend: function(xhr) {
                 xhr.setRequestHeader("X-CSRFToken", csrfToken);
               },
               success: function(response) {
                 $("#transcript").prepend("<p style='color: red;'> Source Stopped </p>")
                 console.log(response);
                 currentSource=null
               },
               error: function(xhr, status, error) {
                 console.log(xhr.responseText);
               }
             });
         }
    });


 })