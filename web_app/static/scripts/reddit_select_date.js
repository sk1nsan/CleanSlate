document.getElementById('dateForm').addEventListener('submit', function(event) {
    const selectedDate = document.getElementById('selected_date').value;
    const errorMessage = document.getElementById('error-message');

    if (!selectedDate) {
        event.preventDefault();
        errorMessage.textContent = 'Please select a valid date.';
        return;
    }
});
