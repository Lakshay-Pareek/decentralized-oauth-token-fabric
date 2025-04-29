import subprocess
import json
import time

print("Simulating NF-B: Validating received token from Fabric...")

# Set the token ID you want to validate
token_id = "token999"

# Build the chaincode query command
query_cmd = [
    "peer", "chaincode", "query",
    "-C", "mychannel",
    "-n", "tokenContract",
    "-c", json.dumps({
        "function": "GetToken",
        "Args": [token_id]
    })
]

# Set the environment variable for peer address
import os
os.environ['CORE_PEER_ADDRESS'] = 'localhost:7051'

# Execute the command
try:
    result = subprocess.check_output(query_cmd, stderr=subprocess.STDOUT)
    token_data = json.loads(result.decode("utf-8"))
except subprocess.CalledProcessError as e:
    print("Failed to fetch token from Fabric:", e.output.decode())
    exit(1)

# Validate the token
if token_data["revoked"]:
    print("Token is revoked. Access denied.")
else:
    current_time = int(time.time())
    if current_time > token_data["expiresAt"]:
        print("Token has expired. Access denied.")
    else:
        print("Token is valid. Access granted.")

print("\nToken details:")
print(json.dumps(token_data, indent=2))
