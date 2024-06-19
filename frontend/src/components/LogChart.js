import React from 'react';
import { Bar } from 'react-chartjs-2';
import { Typography } from '@mui/material';

const LogChart = ({ logs }) => {
  console.log('LogChart logs:', logs);

  const logData = {
    labels: logs.map(log => log.timestamp),
    datasets: [
      {
        label: 'Log Count',
        data: logs.map(log => log.count),
        backgroundColor: 'rgba(75, 192, 192, 0.6)',
      },
    ],
  };

  return (
    <div>
      <Typography variant="h6" gutterBottom>
        Log Activity
      </Typography>
      <Bar data={logData} />
    </div>
  );
};

export default LogChart;
