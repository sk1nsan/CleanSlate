document.getElementById('deleteForm').addEventListener('submit', function(event) {
    const errorMessage = document.getElementById('error-message');
    
    // Sample error checking (can be expanded based on logic)
    if (!confirm('Are you sure you want to delete these items?')) {
        event.preventDefault();
        errorMessage.innerText = 'Deletion cancelled by user.';
        errorMessage.style.display = 'block';
    }
});

