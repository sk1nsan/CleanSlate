document.getElementById('dateForm').addEventListener('submit', function(event) {
    const selectedDate = document.getElementById('selected_date').value;
    const errorMessage = document.getElementById('error-message');

    if (!selectedDate) {
        event.preventDefault();
        errorMessage.textContent = 'Please select a valid date.';
        return;
    }

    const currentDate = new Date();
    const inputDate = new Date(selectedDate);

    if (inputDate > currentDate) {
        event.preventDefault();
        errorMessage.textContent = 'Selected date cannot be in the future.';
    } else {
        errorMessage.textContent = '';
    }
});
