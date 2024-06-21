import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import HomeScreen from './HomeScreen';
import ApplicationLogs from './components/ApplicationLogs';
import SystemLogs from './components/SystemLogs';
import SecurityLogs from './components/SecurityLogs';
import UserLogs from './components/UserLogs';
import InstallLogs from './components/InstallLogs';
import NetworkLogs from './components/NetworkLogs';
import FirewallLogs from './components/FirewallLogs';
import VerifyFile from './components/VerifyFile';

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/" element={<HomeScreen />} />
          <Route path="/logs/application" element={<ApplicationLogs />} />
          <Route path="/logs/system" element={<SystemLogs />} />
          <Route path="/logs/security" element={<SecurityLogs />} />
          <Route path="/logs/user" element={<UserLogs />} />
          <Route path="/logs/install" element={<InstallLogs />} />
          <Route path="/logs/network" element={<NetworkLogs />} />
          <Route path="/logs/firewall" element={<FirewallLogs />} />
          <Route path="/verify-file" element={<VerifyFile />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
