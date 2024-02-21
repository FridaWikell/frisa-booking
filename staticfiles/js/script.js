let currentSessionId = null;

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

/* Delete confirmation */
document.querySelectorAll('.delete-btn').forEach(button => {
    button.addEventListener('click', function() {
        const bookingId = this.getAttribute('data-booking-id');
        const confirmDelete = confirm('Are you sure you want to delete this booking?');
        if (confirmDelete) {
            // Perform the delete action
            fetch(`/booking/delete/${bookingId}/`, { method: 'POST' })
                .then(response => {
                    if (response.ok) {
                        window.location.reload(); // Reload the page to update the list
                    }
                });
        }
    });
});