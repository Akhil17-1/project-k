#!/bin/bash

# Start MongoDB service
echo "Starting MongoDB service..."
net start MongoDB

# Wait for MongoDB to start
sleep 5

# Start log_collector.py in the background
echo "Starting log_collector.py..."
python log_collector.py &
LOG_COLLECTOR_PID=$!

# Wait for log_collector.py to start
sleep 5

# Start agent.py in the background
echo "Starting agent.py..."
python agent.py &
AGENT_PID=$!

# Wait for agent.py to start
sleep 5

# Function to stop all services
function stop_all {
    echo "Stopping all services..."
    net stop MongoDB
    kill $LOG_COLLECTOR_PID
    kill $AGENT_PID
    exit 0
}

# Trap any interrupt signal (Ctrl+C) and stop all services
trap stop_all INT

# Keep the script running to maintain the background processes
while true; do
    sleep 1
done
