<script>
        // Initialize usage and leak detection variables
        let totalUsage = 0;
        let averageUsage = 0;
        let monthUsage = 0;
        let leakThreshold = 8; // Example threshold for leak detection (L/min)

        function updateRealTimeData() {
            const usageElement = document.getElementById('usage');
            const leakStatusElement = document.getElementById('leak-status');
            const totalUsageElement = document.getElementById('total-usage');
            const averageUsageElement = document.getElementById('average-usage');
            const monthUsageElement = document.getElementById('month-usage');

            // Simulate real-time water usage data
            const currentUsage = Math.floor(Math.random() * 10) + 1; // Random value between 1 and 10 L/min
            usageElement.textContent = `${currentUsage} L/min`;

            // Update total and monthly usage
            totalUsage += currentUsage;
            monthUsage += currentUsage;

            // Update UI elements
            totalUsageElement.textContent = `${totalUsage.toFixed(2)} L`;
            averageUsage = totalUsage / (30 * 24); // Assuming 30 days and 24 hours in a month
            averageUsageElement.textContent = `${averageUsage.toFixed(2)} L/day`;
            monthUsageElement.textContent = `${monthUsage.toFixed(2)} L`;

            // Leak detection
            if (currentUsage > leakThreshold) {
                leakStatusElement.textContent = "Potential leak detected!";
                leakStatusElement.style.color = "red";
            } else {
                leakStatusElement.textContent = "No leaks detected";
                leakStatusElement.style.color = "green";
            }
        }

        // Update real-time data every 5 seconds
        setInterval(updateRealTimeData, 5000);
    </script>