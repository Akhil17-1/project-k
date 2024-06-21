// src/components/UserLogs.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import LogChart from './LogChart';

const UserLogs = () => {
  const [logs, setLogs] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:5000/logs/user')
      .then(response => setLogs(response.data))
      .catch(error => console.error('Error fetching logs:', error));
  }, []);

  return (
    <div>
      <h2>User Logs</h2>
      <LogChart data={logs} />
      <ul>
        {logs.map(log => (
          <li key={log._id}>{log.Message}</li>
        ))}
      </ul>
    </div>
  );
};

export default UserLogs;
