import React, { useState, useEffect } from 'react';
import LogChart from './LogChart';
import VulnerabilityList from './VulnerabilityList';
import { Container, Grid, Paper, Typography } from '@mui/material';

const Dashboard = () => {
  const [logs, setLogs] = useState([]);
  const [vulnerabilities, setVulnerabilities] = useState([]);

  useEffect(() => {
    // Mock data for initial rendering
    const mockLogs = [
      { timestamp: '2024-06-19T12:34:56Z', count: 5 },
      { timestamp: '2024-06-19T13:34:56Z', count: 3 },
      { timestamp: '2024-06-19T14:34:56Z', count: 8 },
    ];
    const mockVulnerabilities = [
      { cve: 'CVE-2023-1234', description: 'Sample vulnerability description 1' },
      { cve: 'CVE-2023-5678', description: 'Sample vulnerability description 2' },
    ];

    setLogs(mockLogs);
    setVulnerabilities(mockVulnerabilities);
  }, []);

  return (
    <Container maxWidth="lg">
      <Typography variant="h4" gutterBottom>
        Dashboard
      </Typography>
      <Grid container spacing={3}>
        <Grid item xs={12} md={6}>
          <Paper>
            <LogChart logs={logs} />
          </Paper>
        </Grid>
        <Grid item xs={12} md={6}>
          <Paper>
            <VulnerabilityList vulnerabilities={vulnerabilities} />
          </Paper>
        </Grid>
      </Grid>
    </Container>
  );
};

export default Dashboard;
