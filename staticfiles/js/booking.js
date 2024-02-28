/* Variables */
let currentSessionId = null;
let modalElement = document.getElementById('bookingNotificationModal');
let alreadyBooked = modalElement.getAttribute('data-already-booked') === 'true';


/* Add event listener to store id used for book session */
document.querySelectorAll('.book-session-btn').forEach(button => {
    button.addEventListener('click', function() {
        currentSessionId = this.getAttribute('data-session-id'); // Get session ID when button is clicked
    });
});


/* Submits the form in the pop up modal when making a new booking */
document.getElementById('confirmBooking').addEventListener('click', function() {
    if (currentSessionId) {
        document.getElementById(`bookingForm-${currentSessionId}`).submit(); // Submit the form corresponding to the current session
    }
});


/* Trigger the already booked modal */
if (alreadyBooked) {
    // Logic to show the modal
    let bookingNotificationModal = new bootstrap.Modal(modalElement, {
        keyboard: true
    });
    bookingNotificationModal.show();
}


/* Redirect the user back to the booking page when they have tried 
to book a workshop they already have an active booking */
var closeButton = document.querySelector('#close-booking');
closeButton.addEventListener('click', function() {
    var bookingUrl = this.getAttribute('data-booking-url');
    window.location.href = bookingUrl;
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
            btnText.innerHTML = "Read more &#62;&#62;";
            moreText.style.display = "none";
        } else {
            dots.style.display = "none";
            btnText.innerHTML = "&#60;&#60; Read less";
            moreText.style.display = "inline";
        }
    });
});
