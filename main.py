# Step 1: open file
with open("Projects/ai-log-analyzer/log.txt", "r") as file:
    log_data = file.read()

# Step 2: print log
print("Log Data:")
print(log_data)