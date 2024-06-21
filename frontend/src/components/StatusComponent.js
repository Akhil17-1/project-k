import React, { useState, useEffect } from 'react';
import { fetchLogs } from '../logService';
import LogChart from './LogChart';

const ApplicationLogs = () => {
  const [logs, setLogs] = useState([]);

  useEffect(() => {
    const getLogs = async () => {
      const logsData = await fetchLogs('Application');
      setLogs(logsData);
    };

    getLogs();
  }, []);

  return (
    <div>
      <h2>Application Logs</h2>
      <LogChart data={logs} />
      <ul>
        {logs.map(log => (
          <li key={log._id}>{log.Message}</li>
        ))}
      </ul>
    </div>
  );
};

export default ApplicationLogs;
