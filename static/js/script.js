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