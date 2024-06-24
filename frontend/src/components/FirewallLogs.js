import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';

const FirewallLogs = () => {
    const [logs, setLogs] = useState([]);
    const navigate = useNavigate();

    useEffect(() => {
        const fetchLogs = async () => {
            try {
                const response = await axios.get('http://127.0.0.1:5000/logs/Firewall');
                setLogs(response.data);
            } catch (error) {
                console.error('Error fetching logs:', error);
            }
        };

        fetchLogs();
    }, []);

    return (
        <div>
            <header>
                <h1 onClick={() => navigate('/')}>Home</h1>
            </header>
            <button onClick={() => navigate(-1)}>Go Back</button>
            <div>
                {logs.map((log, index) => (
                    <div key={index}>{JSON.stringify(log)}</div>
                ))}
            </div>
        </div>
    );
};

export default FirewallLogs;
