// src/components/SecurityLogs.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import LogChart from './LogChart';

const SecurityLogs = () => {
  const [logs, setLogs] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:5000/logs/security')
      .then(response => setLogs(response.data))
      .catch(error => console.error('Error fetching logs:', error));
  }, []);

  return (
    <div>
      <h2>Security Logs</h2>
      <LogChart data={logs} />
      <ul>
        {logs.map(log => (
          <li key={log._id}>{log.Message}</li>
        ))}
      </ul>
    </div>
  );
};

export default SecurityLogs;
