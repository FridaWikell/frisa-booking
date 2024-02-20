document.addEventListener('DOMContentLoaded', (event) => {
    let sessionId = null;
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value; // CSRF token

    document.querySelectorAll('.book-session-btn').forEach(button => {
        button.addEventListener('click', function() {
            sessionId = this.getAttribute('data-session-id'); // Get session ID when button is clicked
        });
    });

    document.getElementById('confirmBooking').addEventListener('click', function() {
        let bookingFot = document.getElementById('bookingForm')
        console.log(bookingFot)
        document.getElementById('bookingForm').submit();

        /* const formData = new FormData();
        formData.append('session_id', sessionId); // Append the session_id or any other data you need to send

        fetch(`/book_session/${sessionId}/`, {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrfToken,
            },
            body: sessionId, // Pass the FormData object as the body of the request
            credentials: 'same-origin',
        }).then(response => {
            console.log(response);
            if (response.redirected) {
                window.location.href = response.url; // Redirect to the response URL if booking is successful
            }
        });

        
            const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
            let formData = new FormData();
            // Assuming your Django view doesn't require any additional data besides what's in the URL.
            // If needed, you can append key-value pairs to formData, e.g., formData.append('key', 'value');
            console.log(sessionId)
            fetch(`/book_session/${sessionId}/`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrfToken,
                    // 'Content-Type': 'application/json' is not needed when using FormData
                },
                body: formData,
                credentials: 'same-origin'
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.text(); // Assuming the response is plain text or HTML
            })
            .then(data => {
                // Handle your response here. Data is what your Django view returns.
                console.log(data); // For debugging
                // You can process the data as needed, e.g., display a message or redirect
            })
            .catch(error => console.error('Fetch error:', error));
        */
        
    });
});