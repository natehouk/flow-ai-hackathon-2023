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

      function pollData() {
          var source = $("#dataSource").val()
            if(source=="none"){
            } else{
              $.get('/latest-data-api/', function(data) {
                var info = data.data;
                if (info != false) {
                    $("#transcript").prepend("<p>" + info + "</p>")
                }
            });
            }
          setTimeout(pollData, 200);
      }

      function pollSummary() {
        var source = $("#dataSource").val()

          if(source=="none"){
            } else{
              $.get('/latest-summary-api/', function(data) {
                var info = data.data;
                // add to markdown
                if (info != false) {
                    $("#summary").prepend("<p>" + info + "</p>")
                }
            });
            }
        }
        setTimeout(pollSummary, 100);  // Poll every 5 seconds

      }

      $("#prompt").click(function() {
          var postData = {
            input: $("#prompt-input").val()
          }; 
          var csrfToken = getCookie('csrftoken');
          $.ajax({
            type: "POST",
            url: "/post-prompt/",
            data: postData,
            beforeSend: function(xhr) {
              xhr.setRequestHeader("X-CSRFToken", csrfToken);
            },
            success: function(response) {
              console.log(response);
              $("#summary").prepend("<p style='color: red;'> Prompt is: " + response.data + "</p>")
              // Perform additional actions or logic
            },
            error: function(xhr, status, error) {
              console.log(xhr.responseText);
              // Handle error
            }
          });

    });
      pollData();
      pollSummary();
  });