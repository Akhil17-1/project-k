import axios from 'axios';

const API_BASE_URL = 'http://localhost:5000';

export const fetchLogs = async (logType) => {
    const response = await axios.get(`${API_BASE_URL}/logs/${logType}`);
    return response.data;
};

export const fetchStatus = async () => {
    const response = await axios.get(`${API_BASE_URL}/status`);
    return response.data;
};

export const fetchTopCVEs = async () => {
    // Mocked top CVEs data, replace this with actual API call if available
    return [
        { id: 'CVE-2021-1234', description: 'Sample CVE 1' },
        { id: 'CVE-2021-5678', description: 'Sample CVE 2' },
        { id: 'CVE-2021-9102', description: 'Sample CVE 3' },
    ];
};
