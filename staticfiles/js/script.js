document.addEventListener('DOMContentLoaded', (event) => {
        
    let currentSessionId = null;
    var selectedSessionId = "";


    document.addEventListener('click', function(e) {
        if (e.target && e.target.matches('.session-btn')) {
            selectedSessionId = e.target.getAttribute('data-session-id'); // Store the session ID
            // Show the confirmation modal
            var confirmationModal = new bootstrap.Modal(document.getElementById('confirmationModal'), {
                keyboard: false
            });
            confirmationModal.show();
        }
    });


    // Handle the confirmation button click in the modal
    document.getElementById('confirmChange').addEventListener('click', function() {
        if (selectedSessionId) {
            document.getElementById('selectedSessionId').value = selectedSessionId; // Set the hidden input value
            document.getElementById('sessionForm').submit(); // Submit the form
        }
    });

    

    document.querySelectorAll('.book-session-btn').forEach(button => {
        button.addEventListener('click', function() {
            currentSessionId = this.getAttribute('data-session-id'); // Get session ID when button is clicked
        });
    });
    
    document.getElementById('confirmBooking').addEventListener('click', function() {
        if (currentSessionId) {
            document.getElementById(`bookingForm-${currentSessionId}`).submit(); // Submit the form corresponding to the current session
        }
    });




    document.querySelectorAll('.read-more').forEach(item => {
        item.addEventListener('click', event => {
            // Use `event.currentTarget` to correctly refer to the button element
            var cardBody = event.currentTarget.closest('.card-body');
            var dots = cardBody.querySelector('.dots');
            var moreText = cardBody.querySelector('.more');
            var btnText = event.currentTarget; // Correct reference to the button

            if (dots.style.display === "none") {
                dots.style.display = "inline";
                btnText.innerHTML = "Read more";
                moreText.style.display = "none";
            } else {
                dots.style.display = "none";
                btnText.innerHTML = "Read less";
                moreText.style.display = "inline";
            }
        });
    });


    function confirmDelete() {
        return confirm('Are you sure you want to cancel this booking?');
    };

});