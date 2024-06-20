import React, { useState, useEffect } from 'react';
import { fetchStatus, fetchTopCVEs } from './logService';
import './HomeScreen.css'; // Create a CSS file for styling

const HomeScreen = () => {
    const [status, setStatus] = useState([]);
    const [topCVEs, setTopCVEs] = useState([]);
    const [successRate, setSuccessRate] = useState(0);

    useEffect(() => {
        fetchStatus().then(setStatus);
        fetchTopCVEs().then(setTopCVEs);
    }, []);

    useEffect(() => {
        if (status.length > 0) {
            calculateSuccessRate();
        }
    }, [status]);

    const calculateSuccessRate = () => {
        const totalLogs = status.reduce((acc, stat) => acc + (stat.count || 0), 0);
        const errorLogs = status.reduce((acc, stat) => acc + (stat.errorCount || 0), 0);
        const successRate = ((totalLogs - errorLogs) / totalLogs) * 100;
        setSuccessRate(successRate);
    };

    const getTheme = () => {
        return successRate > 50 ? 'happy-theme' : 'sad-theme';
    };

    return (
        <div className={`home-screen ${getTheme()}`}>
            <h1>Project K Dashboard</h1>
            <div className="summary">
                <h2>Log Success Rate: {successRate.toFixed(2)}%</h2>
            </div>
            <div className="top-cves">
                <h2>Top CVEs</h2>
                <ul>
                    {topCVEs.map(cve => (
                        <li key={cve.id}>
                            {cve.id}: {cve.description}
                        </li>
                    ))}
                </ul>
            </div>
            <div className="log-types">
                <h2>Select Log Type</h2>
                <ul>
                    <li><a href="/logs/application">Application Logs</a></li>
                    <li><a href="/logs/system">System Logs</a></li>
                    <li><a href="/logs/security">Security Logs</a></li>
                    <li><a href="/logs/user">User Logs</a></li>
                    <li><a href="/logs/install">Install Logs</a></li>
                    <li><a href="/logs/network">Network Logs</a></li>
                    <li><a href="/logs/firewall">Firewall Logs</a></li>
                </ul>
            </div>
        </div>
    );
};

export default HomeScreen;
