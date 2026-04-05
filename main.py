# Step 1: read file
with open("Projects/ai-log-analyzer/log.txt", "r") as file:
    log_data = file.read()

# Step 2: detect issue
if "ERROR" in log_data:
    issue = "ERROR found"
else:
    issue = "No error"

# Step 3: extract job name
if "Job:" in log_data:
    job = log_data.split("Job:")[1].strip()
else:
    job = "Unknown"

# Step 4: detect status
if "status = 1" in log_data:
    status = "Failed"
else:
    status = "Success"

# Step 5: detect root cause (NEW)
if "does not exist" in log_data:
    root_cause = "Missing file/path"
else:
    root_cause = "Unknown"

# Step 6: print structured output
print("Issue:", issue)
print("Job:", job)
print("Status:", status)
print("Root Cause:", root_cause)
