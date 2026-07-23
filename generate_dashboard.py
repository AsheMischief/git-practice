import json
import random

# Step 2 equivalent: fake "gathered" data (in real life, this would come from an API or file)
data = {
    "Passed": random.randint(50, 100),
    "Failed": random.randint(0, 20),
    "Blocked": random.randint(0, 10),
}

# Step 3: build an HTML page with a chart, embedding the data directly
html = f"""<!DOCTYPE html>
<html>
<head>
  <title>UAT Practice Dashboard</title>
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body>
  <h1>UAT Status Dashboard</h1>
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

with open("index.html", "w") as f:
    f.write(html)

print("Dashboard generated with data:", data)