import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import HomeScreen from './HomeScreen';
import SecurityLogs from './components/SecurityLogs';
import SystemLogs from './components/SystemLogs';
import NetworkLogs from './components/NetworkLogs';
import FirewallLogs from './components/FirewallLogs';
import InstallLogs from './components/InstallLogs';
import UserLogs from './components/UserLogs';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomeScreen />} />
        <Route path="/security-logs" element={<SecurityLogs />} />
        <Route path="/system-logs" element={<SystemLogs />} />
        <Route path="/network-logs" element={<NetworkLogs />} />
        <Route path="/firewall-logs" element={<FirewallLogs />} />
        <Route path="/install-logs" element={<InstallLogs />} />
        <Route path="/user-logs" element={<UserLogs />} />
      </Routes>
    </Router>
  );
}

export default App;
