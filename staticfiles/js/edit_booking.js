let selectedSessionId = null;

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