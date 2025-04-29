import subprocess
import json
import time
import os

print("Simulating NF-A: Requesting token from Fabric...")

token_id = "token999"
issuer_id = "nfA"
subject_id = "nfB"
validity_period = 3600  # 1 hour

current_time = int(time.time())

pwd = os.getcwd()

invoke_command = [
    "peer", "chaincode", "invoke",
    "-o", "localhost:7050",
    "--ordererTLSHostnameOverride", "orderer.example.com",
    "--tls", "--cafile",
    f"{pwd}/organizations/ordererOrganizations/example.com/orderers/orderer.example.com/tls/ca.crt",
    "--channelID", "mychannel",
    "--name", "tokenContract",
    "--peerAddresses", "localhost:7051",
    "--tlsRootCertFiles",
    f"{pwd}/organizations/peerOrganizations/org1.example.com/peers/peer0.org1.example.com/tls/ca.crt",
    "--peerAddresses", "localhost:9051",
    "--tlsRootCertFiles",
    f"{pwd}/organizations/peerOrganizations/org2.example.com/peers/peer0.org2.example.com/tls/ca.crt",
    "-c", json.dumps({
        "function": "IssueToken",
        "Args": [token_id, issuer_id, subject_id, str(validity_period)]
    })
]

# Execute the command
result = subprocess.run(invoke_command, capture_output=True, text=True)

if result.returncode == 0:
    print("Successfully invoked chaincode to issue token.")
else:
    print("Failed to invoke chaincode:", result.stderr)
