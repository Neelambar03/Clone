function updateDateTime() {
    const now = new Date();
    const dateTimeString = now.toLocaleString();
    document.getElementById('datetime').textContent = "Current Date & Time: " + dateTimeString;
}

updateDateTime();
setInterval(updateDateTime, 1000);
