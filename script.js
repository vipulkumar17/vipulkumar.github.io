function summarizeText() {
    // Get the input text from the textarea
    const inputText = document.getElementById("inputText").value;
    
    // Send the text to the backend using an AJAX POST request
    $.ajax({
      url: '/summarize',
      type: 'POST',
      contentType: 'application/json',
      data: JSON.stringify({ text: inputText }),
      success: function(response) {
        // Display the summary in the "summary" div
        document.getElementById("summary").innerText = response.summary;
      },
      error: function() {
        alert("An error occurred while summarizing.");
      }
    });
  }
  