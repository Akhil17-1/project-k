import React from 'react';
import { Bar } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
);

const LogChart = ({ logs }) => {
  const logCounts = logs.reduce((acc, log) => {
    const logType = log.source;
    if (!acc[logType]) {
      acc[logType] = 0;
    }
    acc[logType]++;
    return acc;
  }, {});

  const data = {
    labels: Object.keys(logCounts),
    datasets: [
      {
        label: 'Log Count',
        data: Object.values(logCounts),
        backgroundColor: 'rgba(75, 192, 192, 0.6)',
      },
    ],
  };

  return (
    <div>
      <h2>Log Counts</h2>
      <Bar
        data={data}
        options={{
          maintainAspectRatio: false,
          scales: {
            y: {
              beginAtZero: true,
            },
          },
        }}
      />
    </div>
  );
};

export default LogChart;
