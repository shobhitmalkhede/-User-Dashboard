from flask import Flask, render_template

app = Flask(__name__)

# Sample data for combined insights
combined_insights = {
    "user_id": "12345",
    "combined_feedback": [
        "Increase your daily steps by 10% to improve cardiovascular health.",
        "Your sleep is below the recommended 7 hours. Consider improving your bedtime routine.",
        "Your journal entries reflect stress. Try stress management techniques.",
        "Poor sleep and stress may affect your overall well-being. Consider practicing mindfulness or relaxation techniques."
    ]
}

@app.route('/')
def home():
    return render_template('index.html', insights=combined_insights)

if __name__ == "__main__":
    app.run(debug=True)
