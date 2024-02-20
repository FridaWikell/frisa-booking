document.querySelectorAll('.book-session-btn').forEach(button => {
    button.addEventListener('click', function() {
        const sessionId = this.getAttribute('data-session-id');
        if (confirm('Are you sure you want to book this session?')) {
            fetch(`/book_session/${sessionId}/`, { method: 'POST',
                headers: {
                    'X-CSRFToken': '{{ csrf_token }}',
                    'Content-Type': 'application/json',
                },
                credentials: 'same-origin'
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert(data.message); // Or update the UI accordingly
                } else {
                    alert(data.message);
                }
            });
        }
    });
});