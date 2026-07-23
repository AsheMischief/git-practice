import json
import random
from datetime import datetime

# Fake "gathered" data
data = {
    "Passed": random.randint(50, 100),
    "Failed": random.randint(0, 20),
    "Blocked": random.randint(0, 10),
}

# Build a unique filename using the current date/time
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = f"dashboard_{timestamp}.html"

html = f"""<!DOCTYPE html>
<html>
<head>
  <title>UAT Practice Dashboard</title>
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body>
  <h1>UAT Status Dashboard</h1>
  <p>Generated: {timestamp}</p>
  <canvas id="myChart" width="400" height="200"></canvas>
  <script>
    const ctx = document.getElementById('myChart');
    new Chart(ctx, {{
      type: 'bar',
      data: {{
        labels: {json.dumps(list(data.keys()))},
        datasets: [{{
          label: 'Test Results',
          data: {json.dumps(list(data.values()))},
          backgroundColor: ['green', 'red', 'orange']
        }}]
      }}
    }});
  </script>
</body>
</html>
"""

with open(filename, "w") as f:
    f.write(html)

print(f"Dashboard generated: {filename}")