import React, { useState, useEffect } from 'react';
import { fetchLogs } from './logService';
import LogChart from './components/LogChart';

const Logs = ({ logType }) => {
    const [logs, setLogs] = useState([]);

    useEffect(() => {
        fetchLogs(logType).then(setLogs);
    }, [logType]);

    return (
        <div>
            <h1>{logType} Logs</h1>
            <ul>
                {logs.map((log, index) => (
                    <li key={index}>
                        <strong>Source:</strong> {log.SourceName}<br />
                        <strong>Timestamp:</strong> {log.TimeGenerated}<br />
                        <strong>Event Category:</strong> {log.EventCategory}<br />
                        <strong>Event ID:</strong> {log.EventID}<br />
                        <strong>Event Type:</strong> {log.EventType} ({log.EventTypeName})<br />
                        <strong>Message:</strong> {log.Message ? log.Message.join(' ') : ''}
                    </li>
                ))}
            </ul>
            <LogChart logs={logs} />
        </div>
    );
};

export default Logs;
