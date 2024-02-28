/* Submits the deletion form when user has confirmed it in the modal */
document.querySelectorAll('.delete-booking').forEach(button => {
    button.addEventListener('click', function() {
        let bookingId = this.getAttribute('data-booking-id');
        let form = document.getElementById('deleteForm');
        form.action = `/booking/delete_booking/${bookingId}/`;
    });
});