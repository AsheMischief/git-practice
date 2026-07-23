import json
import random
from datetime import datetime
from collections import Counter

# Simulate a "raw feed" of individual test/defect records — 
# in real life, this list would come from an API or exported file,
# and each status is whatever the source system actually reports.
possible_statuses = ["Passed", "Failed", "Blocked", "In Progress"]
raw_results = [
    {"id": i, "status": random.choice(possible_statuses)}
    for i in range(random.randint(20, 60))
]

status_counts = Counter(result["status"] for result in raw_results)

# Fixed, known order and colors for statuses you expect and want stable
known_statuses = {
    "Passed": "#4caf50",
    "Failed": "#f44336",
    "Blocked": "#ff9800",
    "In Progress": "#2196f3",
}

labels = []
values = []
colors = []

# First, add known statuses in a fixed order — always present, even if count is 0
for status, color in known_statuses.items():
    labels.append(status)
    values.append(status_counts.get(status, 0))
    colors.append(color)

# Then, append any *unexpected* status that showed up but wasn't in known_statuses
for status, count in status_counts.items():
    if status not in known_statuses:
        labels.append(status)
        values.append(count)
        colors.append("#9e9e9e")

data = dict(zip(labels, values))

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
  <p>Total records: {len(raw_results)}</p>
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
          backgroundColor: {json.dumps(colors)}
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
print(f"Statuses found: {data}")