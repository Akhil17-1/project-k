// src/HomeScreen.js
import React, { useState } from 'react';
import styled, { createGlobalStyle } from 'styled-components';
import Header from './components/Header';
import Sidebar from './components/Sidebar';
import Thumbnail from './components/Thumbnail';
import CVETicker from './components/CVETicker';

const GlobalStyle = createGlobalStyle`
  body {
    margin: 0;
    padding: 0;
    font-family: 'Arial', sans-serif;
    background-color: #141414;
    color: white;
  }
`;

const Container = styled.div`
  padding: 20px;
`;

const ThumbnailGrid = styled.div`
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
`;

const HomeScreen = () => {
  const [isSidebarOpen, setIsSidebarOpen] = useState(false);

  const toggleMenu = () => {
    setIsSidebarOpen(!isSidebarOpen);
  };

  const logTypes = [
    { title: 'Application Logs', image: 'app-logs.jpg' },
    { title: 'System Logs', image: 'system-logs.jpg' },
    { title: 'Security Logs', image: 'security-logs.jpg' },
    { title: 'User Logs', image: 'user-logs.jpg' },
    { title: 'Install Logs', image: 'install-logs.jpg' },
    { title: 'Network Logs', image: 'network-logs.jpg' },
    { title: 'Firewall Logs', image: 'firewall-logs.jpg' },
  ];

  return (
    <>
      <GlobalStyle />
      <Header toggleMenu={toggleMenu} />
      <Sidebar isOpen={isSidebarOpen} toggleMenu={toggleMenu} />
      <CVETicker />
      <Container>
        <h2>Logs</h2>
        <ThumbnailGrid>
          {logTypes.map((log, index) => (
            <Thumbnail key={index} title={log.title} image={`/images/${log.image}`} />
          ))}
        </ThumbnailGrid>
      </Container>
    </>
  );
};

export default HomeScreen;
