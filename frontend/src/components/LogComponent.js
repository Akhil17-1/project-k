// src/components/LogComponent.js
import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';

const LogComponent = ({ logType }) => {
    const [logs, setLogs] = useState([]);
    const navigate = useNavigate();

    useEffect(() => {
        const fetchLogs = async () => {
            try {
                const response = await axios.get(`http://127.0.0.1:5000/logs/${logType}`);
                console.log(`Fetched logs for ${logType}:`, response.data); // Debug log
                setLogs(response.data);
            } catch (error) {
                console.error(`Error fetching ${logType} logs:`, error);
            }
        };

        fetchLogs();
    }, [logType]);

    return (
        <div>
            <header>
                <h1 onClick={() => navigate('/')}>Home</h1>
            </header>
            <button onClick={() => navigate(-1)}>Go Back</button>
            <div>
                {logs.length > 0 ? (
                    logs.map((log, index) => (
                        <div key={index}>{JSON.stringify(log)}</div>
                    ))
                ) : (
                    <p>No logs available for {logType}</p>
                )}
            </div>
        </div>
    );
};

export default LogComponent;
