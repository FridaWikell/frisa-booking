let selectedSessionId = null;

/* Add event listener to store id used for edit booking */
document.addEventListener('click', function(e) {
    if (e.target && e.target.matches('.session-btn')) {
        selectedSessionId = e.target.getAttribute('data-session-id');
        
        var confirmationModal = new bootstrap.Modal(document.getElementById('confirmation-modal'), {
            keyboard: false
        });
        confirmationModal.show();
        
        let hiddenInput = document.getElementById('selected-session-id-' + selectedSessionId);
        if (hiddenInput) {
            hiddenInput.value = selectedSessionId;
        }
    }
});

/* Submits the form in the pop-up modal when confirming booking */
document.getElementById('confirm-change').addEventListener('click', function() {
    if (selectedSessionId) {
        let formId = 'session-form-' + selectedSessionId;
        let form = document.getElementById(formId);
        if (form) {
            form.submit();
        }
    }
});
