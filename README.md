# Decentralized OAuth 2.0 Token Issuer for Simulated Network Functions (NFs)

## Overview
This project demonstrates a decentralized mechanism for OAuth 2.0 token issuance and validation using Hyperledger Fabric. It simulates communication between Network Functions (NFs), where tokens are required for secure interaction. The system mimics the behavior of a 5G core's access control logic without fully integrating with a 5G network.

The primary objective is to decentralize trust from a centralized OAuth server by leveraging blockchain technology to provide transparent, immutable, and verifiable token lifecycle management.

---

## Objectives

### 1. Fabric Network Setup
- **Organization**: 1
- **Peers**: 2
- **Certificate Authority**: Basic CA setup

### 2. Chaincode (Smart Contract)
Implements four core functionalities:
- **NF Registration**: On-chain storage of NF metadata (identifiers, roles, public keys).
- **Token Lifecycle Management**: Issue, store, and manage OAuth 2.0-like tokens.
- **Token Validation**: On-chain logic to verify authenticity and integrity of tokens.
- **Token Expiry & Revocation**: Tokens can be set to expire or revoked manually.

### 3. Simulated Network Functions
- **NF-A**: Simulated service to request access tokens.
- **NF-B**: Simulated service to validate access tokens.

### 4. OAuth 2.0 Integration
- Tokens requested with `Client ID` and `Secret`.
- Tokens modeled as JWTs and signed using ledger-backed credentials.
- Verifiability is anchored in blockchain data, making tokens tamper-evident.

### 5. Demonstration Flow
- NF-A requests a token.
- NF-B validates token received from NF-A.
- Token authenticity, expiry, and revocation status are validated against blockchain records.

---

## Architecture Diagram
```
+----------------+      request token     +-------------------+
|     NF-A       |----------------------->| Hyperledger Fabric|
| (Token Issuer) |                        |   Smart Contract  |
+----------------+                        +-------------------+
       |                                              ^
       | send token                                   |
       v                                              |
+----------------+      validate token     +-------------------+
|     NF-B       |<-----------------------| Hyperledger Fabric|
| (Token Verifier)|                        |   Smart Contract  |
+----------------+                        +-------------------+
```

---

## Project Structure
```
.
├── chaincode/                # Chaincode for NF management and token lifecycle
│   └── token_manager.go      # Core logic for registration, issuance, validation
├── nf_a.py                   # Simulated NF-A (token requester)
├── nf_b.py                   # Simulated NF-B (token validator)
├── README.md                 # Project description and setup instructions
```

---

## How to Run

### 1. Start Fabric Network
```bash
cd fabric-samples/test-network
./network.sh up createChannel -ca
./network.sh deployCC -ccn tokenmanager -ccp ../chaincode/ -ccl go
```

### 2. Run Simulated NFs
#### Request a Token (NF-A)
```bash
python3 nf_a.py
```
#### Validate a Token (NF-B)
```bash
python3 nf_b.py
```

---

## How OAuth 2.0 Was Implemented
- Token issuance mimics OAuth 2.0's client credentials grant type.
- Tokens are structured as JSON Web Tokens (JWT)-like objects.
- Client credentials are verified, and token metadata is stored on-chain.
- Validation includes signature checking, expiry, and revocation.

---

## How Fabric is Used to Decentralize Trust
- Tokens and NF data are stored and validated using a permissioned blockchain ledger.
- Chaincode logic ensures that no single central authority controls access verification.
- All token operations are immutably recorded and verifiable by all peers.

---

## Security Considerations
- **Spoofing Protection**: Token issuance tied to cryptographic credentials.
- **Tampering Prevention**: All data changes require consensus on the Fabric network.
- **Revocation Control**: Admins can revoke tokens early to respond to threats.

---

## License
This project is provided for academic and research purposes.

---

## Author
**Lakshay Pareek**  
Linux Foundation Mentorship Program - Blockchain

---

## Repository
[GitHub Link](https://github.com/Lakshay-Pareek/decentralized-oauth-token-fabric)

