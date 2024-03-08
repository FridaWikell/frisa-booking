let selectedSessionId = null;

/* Add event listener to store id used for edit booking */
document.addEventListener('click', function(e) {
    if (e.target && e.target.matches('.session-btn')) {
        selectedSessionId = e.target.getAttribute('data-session-id');
        
        var confirmationModal = new bootstrap.Modal(document.getElementById('confirmationModal'), {
            keyboard: false
        });
        confirmationModal.show();
        
        let hiddenInput = document.getElementById('selectedSessionId-' + selectedSessionId);
        if (hiddenInput) {
            hiddenInput.value = selectedSessionId;
        }
    }
});

/* Submits the form in the pop-up modal when confirming booking */
document.getElementById('confirmChange').addEventListener('click', function() {
    if (selectedSessionId) {
        let formId = 'sessionForm-' + selectedSessionId;
        let form = document.getElementById(formId);
        if (form) {
            form.submit();
        }
    }
});
