// logService.js
import axios from 'axios';
import DOMPurify from 'dompurify';

const API_BASE_URL = 'http://127.0.0.1:5000';

export const fetchLogs = async (logType) => {
    logType = DOMPurify.sanitize(logType);
    const response = await axios.get(`${API_BASE_URL}/logs/${logType}`);
    return response.data;
};

export const fetchStatus = async () => {
    const response = await axios.get(`${API_BASE_URL}/status`);
    return response.data;
};

export const fetchTopCVEs = async () => {
    const response = await axios.get(`${API_BASE_URL}/cves`);
    return response.data;
};
