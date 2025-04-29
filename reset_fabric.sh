#!/bin/bash

# Step 0: Go to fabric-samples
cd ~/fabric-samples || { echo "fabric-samples not found!"; exit 1; }

echo "🔴 Deleting old test-network..."
rm -rf test-network

echo "🔵 Downloading fresh test-network..."
git clone https://github.com/hyperledger/fabric-samples.git temp-fabric-samples
cp -r temp-fabric-samples/test-network ./
rm -rf temp-fabric-samples

echo "🧹 Cleaning up old Docker containers and networks..."
docker kill $(docker ps -q) 2>/dev/null || true
docker rm $(docker ps -a -q) 2>/dev/null || true
docker network prune -f
docker volume prune -f

echo "📦 Resetting Fabric binaries (bin/ and config/ folders)..."
curl -sSL https://bit.ly/2ysbOFE | bash -s

echo "✅ All clean! Now ready to use:"
echo "👉 cd ~/fabric-samples/test-network"
echo "👉 ./network.sh up"
