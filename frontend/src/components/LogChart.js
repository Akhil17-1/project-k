import React from 'react';
import { Bar } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
} from 'chart.js';

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
);

const LogChart = ({ data }) => {
  const chartData = {
    labels: data.map(log => new Date(log.timestamp).toLocaleString()),
    datasets: [
      {
        label: 'Log Events',
        data: data.map(log => log.value),
        backgroundColor: 'rgba(75,192,192,0.6)',
      },
    ],
  };

  return <Bar data={chartData} />;
};

export default LogChart;
