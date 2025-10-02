from browser_history import get_history
import pandas as pd

# Get browser history
outputs = get_history()

# Inspect first entry to understand structure
print(outputs.histories[0])

# Create DataFrame with correct number of columns
history_df = pd.DataFrame(outputs.histories, columns=['timestamp', 'url', 'title'])

print(history_df.head(10))

# Save to CSV
history_df.to_csv('browser_history.csv', index=False)

print("Browser history extracted and saved to 'browser_history.csv'")
