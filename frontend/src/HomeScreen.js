// src/HomeScreen.js
import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { fetchStatus } from './logService';
import Header from './components/Header';
import './HomeScreen.css';

const HomeScreen = () => {
  const [status, setStatus] = useState({});

  useEffect(() => {
    const getStatus = async () => {
      try {
        const data = await fetchStatus();
        setStatus(data);
      } catch (error) {
        console.error("Error fetching status:", error);
      }
    };

    getStatus();
  }, []);

  return (
    <div className="home-screen">
      <Header />
      <h1>Project K Dashboard</h1>
      <div className="log-summary">
        <p>Total Logs Collected: {status.totalLogs}</p>
        <p>Last Log Collected Time: {status.lastLogCollected}</p>
        <p>Number of Error Logs: {status.errorLogs}</p>
        <p>Percentage of Successful Logs: {status.successPercentage}%</p>
      </div>
      <div className="log-thumbnails">
        <Link to="/application-logs">
          <div className="thumbnail">
            <h3>Application Logs</h3>
          </div>
        </Link>
        <Link to="/security-logs">
          <div className="thumbnail">
            <h3>Security Logs</h3>
          </div>
        </Link>
        <Link to="/system-logs">
          <div className="thumbnail">
            <h3>System Logs</h3>
          </div>
        </Link>
        <Link to="/network-logs">
          <div className="thumbnail">
            <h3>Network Logs</h3>
          </div>
        </Link>
        <Link to="/firewall-logs">
          <div className="thumbnail">
            <h3>Firewall Logs</h3>
          </div>
        </Link>
        <Link to="/install-logs">
          <div className="thumbnail">
            <h3>Install Logs</h3>
          </div>
        </Link>
        <Link to="/user-logs">
          <div className="thumbnail">
            <h3>User Logs</h3>
          </div>
        </Link>
      </div>
    </div>
  );
};

export default HomeScreen;
