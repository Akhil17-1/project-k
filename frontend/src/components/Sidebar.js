// src/components/Sidebar.js
import React from 'react';
import { Link } from 'react-router-dom';
import './Sidebar.css';

const Sidebar = () => {
  return (
    <div className="sidebar">
      <h3>Log Types</h3>
      <ul>
        <li><Link to="/application-logs">Application Logs</Link></li>
        <li><Link to="/security-logs">Security Logs</Link></li>
        <li><Link to="/system-logs">System Logs</Link></li>
        <li><Link to="/network-logs">Network Logs</Link></li>
        <li><Link to="/firewall-logs">Firewall Logs</Link></li>
        <li><Link to="/install-logs">Install Logs</Link></li>
        <li><Link to="/user-logs">User Logs</Link></li>
      </ul>
    </div>
  );
};

export default Sidebar;
