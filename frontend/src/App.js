import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import HomeScreen from './HomeScreen';
import Logs from './Logs'; // Assuming you will use the Logs component for different log types

function App() {
    return (
        <Router>
            <div className="App">
                <Routes>
                    <Route path="/" element={<HomeScreen />} />
                    <Route path="/logs/application" element={<Logs logType="Application" />} />
                    <Route path="/logs/system" element={<Logs logType="System" />} />
                    <Route path="/logs/security" element={<Logs logType="Security" />} />
                    <Route path="/logs/user" element={<Logs logType="User" />} />
                    <Route path="/logs/install" element={<Logs logType="Install" />} />
                    <Route path="/logs/network" element={<Logs logType="Network" />} />
                    <Route path="/logs/firewall" element={<Logs logType="Firewall" />} />
                </Routes>
            </div>
        </Router>
    );
}

export default App;
