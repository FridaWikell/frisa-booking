document.addEventListener('DOMContentLoaded', (event) => {
        
    let currentSessionId = null;
    var selectedSessionId = "";

    /* Add event listener to store id used for edit booking */
    document.addEventListener('click', function(e) {
        if (e.target && e.target.matches('.session-btn')) {
            selectedSessionId = e.target.getAttribute('data-session-id');
            var confirmationModal = new bootstrap.Modal(document.getElementById('confirmationModal'), {
                keyboard: false
            });
            confirmationModal.show();
        }
    });

    /* Submits the form in the pop up modal when editing booking */
    document.getElementById('confirmChange').addEventListener('click', function() {
        if (selectedSessionId) {
            document.getElementById('selectedSessionId').value = selectedSessionId; // Set the hidden input value
            document.getElementById('sessionForm').submit(); // Submit the form
        }
    });

 
    /* Add event listener to store id used for book session */
    document.querySelectorAll('.book-session-btn').forEach(button => {
        button.addEventListener('click', function() {
            currentSessionId = this.getAttribute('data-session-id'); // Get session ID when button is clicked
            console.log(currentSessionId);
        });
    });

    /* Submits the form in the pop up modal when making a new booking */
    document.getElementById('confirmBooking').addEventListener('click', function() {
        if (currentSessionId) {
            document.getElementById(`bookingForm-${currentSessionId}`).submit(); // Submit the form corresponding to the current session
        }
    });



    /* Expands the course description */
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