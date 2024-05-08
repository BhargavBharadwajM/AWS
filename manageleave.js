
document.getElementById('manageLeaveForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form submission

    // Get form data
    var employeeId = document.getElementById('employeeId').value;
    var startDate = document.getElementById('startDate').value;
    var endDate = document.getElementById('endDate').value;

    // Prepare data object for Lambda function
    var requestData = {
        method: 'POST',
        body: JSON.stringify({
            employeeId: employeeId,
            startDate: startDate,
            endDate: endDate
        })
    };

    // Call Lambda function to manage leave
    fetch('YOUR_MANAGE_LEAVE_LAMBDA_ENDPOINT', requestData)
        .then(response => {
            if (response.ok) {
                alert('Leave request submitted successfully');
                // Redirect to home page or perform any other action
            } else {
                alert('Failed to submit leave request');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Failed to submit leave request');
        });
});
