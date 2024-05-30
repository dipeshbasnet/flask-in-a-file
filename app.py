from flask import Flask, jsonify

app = Flask(__name__)

DEMO_JSON = {
    "item 1": 20,
    "item 2": 14,
    "item 3": 2,
    "item 4": 56,
    "item 5": 23,
    "item 6": 52,
    "item 7": 22,
    "item 8": 67,
}


# API route to get data
@app.route('/data')
def data():
    # You can use any API that gives you data for the charts/graphs
    return jsonify(DEMO_JSON)


# Home route
@app.route('/')
def home():
    # defining HTML for the home page
    html = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Flask app in a file</title>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.9.4/Chart.min.css">
        <style>
            {css}
        </style>
    </head>
    <body>
        <div class="chart-container">
            <h2>Bar Chart</h2>
            <canvas id="barChart"></canvas>
        </div>

        <div class="chart-container">
            <h2>Line Chart</h2>
            <canvas id="lineChart"></canvas>
        </div>

        <div class="chart-container">
            <h2>Pie Chart</h2>
            <canvas id="pieChart"></canvas>
        </div>

        <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.9.4/Chart.min.js"></script>
        <script>
            {js}
        </script>
    </body>
    </html>
    '''
    # defining CSS
    css = '''
    body {
        font-family: Arial, sans-serif;
        background-color: #f0f0f0;
        margin: 0;
        padding: 0;
        display: flex;
        flex-wrap: wrap;
        justify-content: space-around;
        align-items: flex-start;
        min-height: 100vh;
    }
    .chart-container {
        width: 30%;
        background-color: #fff;
        border-radius: 10px;
        padding: 20px;
        margin: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    '''
    # defining JS
    # HTTP GET request to the /data endpoint defined in data()
    js = '''
    document.addEventListener('DOMContentLoaded', function () {
        fetch('/data')
            .then(response => response.json())
            .then(data => {
                const labels = Object.keys(data);
                const values = Object.values(data);

                // Bar Chart
                var ctx1 = document.getElementById('barChart').getContext('2d');
                new Chart(ctx1, {
                    type: 'bar',
                    data: {
                        labels: labels,
                        datasets: [{
                            label: 'Data',
                            data: values,
                            backgroundColor: 'rgba(54, 162, 235, 0.6)',
                            borderColor: 'rgba(54, 162, 235, 1)',
                            borderWidth: 1
                        }]
                    }
                });

                // Line Chart
                var ctx2 = document.getElementById('lineChart').getContext('2d');
                new Chart(ctx2, {
                    type: 'line',
                    data: {
                        labels: labels,
                        datasets: [{
                            label: 'Data',
                            data: values,
                            backgroundColor: 'rgba(255, 99, 132, 0.6)',
                            borderColor: 'rgba(255, 99, 132, 1)',
                            borderWidth: 1
                        }]
                    }
                });

                // Pie Chart
                var ctx3 = document.getElementById('pieChart').getContext('2d');
                new Chart(ctx3, {
                    type: 'pie',
                    data: {
                        labels: labels,
                        datasets: [{
                            label: 'Data',
                            data: values,
                            backgroundColor: [
                                'rgba(255, 99, 132, 0.6)',
                                'rgba(54, 162, 235, 0.6)',
                                'rgba(255, 206, 86, 0.6)',
                                'rgba(75, 192, 192, 0.6)',
                                'rgba(153, 102, 255, 0.6)',
                                'rgba(255, 159, 64, 0.6)',
                                'rgba(201, 203, 207, 0.6)',
                                'rgba(75, 192, 192, 0.6)'
                            ],
                            borderColor: [
                                'rgba(255, 99, 132, 1)',
                                'rgba(54, 162, 235, 1)',
                                'rgba(255, 206, 86, 1)',
                                'rgba(75, 192, 192, 1)',
                                'rgba(153, 102, 255, 1)',
                                'rgba(255, 159, 64, 1)',
                                'rgba(201, 203, 207, 1)',
                                'rgba(75, 192, 192, 1)'
                            ],
                            borderWidth: 1
                        }]
                    }
                });
            });
    });
    '''

    return html.format(css=css, js=js)


if __name__ == '__main__':
    app.run(debug=True)
