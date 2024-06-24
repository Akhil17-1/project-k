import React, { useEffect, useRef } from 'react';
import { Chart } from 'chart.js';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';

const LogChart = () => {
    const chartRef = useRef(null);
    const navigate = useNavigate();

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await axios.get('/api/logs');
                const data = response.data;

                const ctx = chartRef.current.getContext('2d');
                new Chart(ctx, {
                    type: 'line',
                    data: {
                        labels: data.map(log => log.timestamp),
                        datasets: [{
                            label: 'Logs',
                            data: data.map(log => log.value)
                        }]
                    }
                });
            } catch (error) {
                console.error('Error fetching log data:', error);
            }
        };

        fetchData();

        return () => {
            if (chartRef.current) {
                chartRef.current.destroy();
            }
        };
    }, []);

    return (
        <div>
            <button onClick={() => navigate(-1)}>Go Back</button>
            <button onClick={() => navigate('/')}>Go Home</button>
            <canvas ref={chartRef}></canvas>
        </div>
    );
};

export default LogChart;
