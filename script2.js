document.addEventListener('DOMContentLoaded', () => {
    let totalUsage = 0;
    let averageUsage = 0;
    let monthUsage = 0;

    function updateWaterUsage() {
        const usageElement = document.getElementById('usage');
        const usage = Math.floor(Math.random() * 10) + 1;
        usageElement.textContent = `${usage} L/min`;

        totalUsage += usage;
        monthUsage += usage;

        document.getElementById('total-usage').textContent = `${totalUsage} L`;
        document.getElementById('month-usage').textContent = `${monthUsage} L`;
        
        averageUsage = totalUsage / 30;
        document.getElementById('average-usage').textContent = `${averageUsage.toFixed(2)} L/day`;

        if (usage > 8) {
            document.getElementById('leak-status').textContent = "Potential leak detected!";
            document.getElementById('leak-status').style.color = "red";
        } else {
            document.getElementById('leak-status').textContent = "No leaks detected";
            document.getElementById('leak-status').style.color = "green";
        }
    }

    setInterval(updateWaterUsage, 5000);
});
