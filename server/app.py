from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will allow CORS from all origins

@app.route('/calculate', methods=['POST'])
def calculate_water_usage():
    data = request.json

    # Extract data from JSON request
    daily_usages = {
        'Monday': data.get('monday', 0),
        'Tuesday': data.get('tuesday', 0),
        'Wednesday': data.get('wednesday', 0),
        'Thursday': data.get('thursday', 0),
        'Friday': data.get('friday', 0),
        'Saturday': data.get('saturday', 0),
        'Sunday': data.get('sunday', 0)
    }

    # Calculate total and average usage
    total_weekly_usage = sum(daily_usages.values())
    average_daily_usage = total_weekly_usage / 7

    # Provide feedback
    if average_daily_usage > 300:
        feedback = "Your water usage is higher than average. Consider checking for leaks or adopting water-saving habits."
    elif average_daily_usage < 150:
        feedback = "Great job! Your water usage is below average. Keep up the good work conserving water!"
    else:
        feedback = "Your water usage is within a typical range. Consider some additional water-saving measures if you’d like to reduce it further."

    # Return results as JSON
    return jsonify({
        'daily_usages': daily_usages,
        'total_weekly_usage': total_weekly_usage,
        'average_daily_usage': average_daily_usage,
        'feedback': feedback
    })

if __name__ == '__main__':
    app.run(debug=True)
