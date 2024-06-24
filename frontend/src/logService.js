import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:5000';

export const fetchLogs = async (logType) => {
    try {
        const response = await axios.get(`${API_BASE_URL}/logs/${logType}`);
        return response.data;
    } catch (error) {
        console.error("Error fetching logs:", error);
        return null;  // Return null or handle it appropriately in the calling code
    }
};

export const fetchStatus = async () => {
    try {
        const response = await axios.get(`${API_BASE_URL}/status`);
        return response.data;
    } catch (error) {
        console.error("Error fetching status:", error);
        return null;  // Return null or handle it appropriately in the calling code
    }
};

export const fetchTopCVEs = async () => {
    try {
        const response = await axios.get(`${API_BASE_URL}/cves`);
        return response.data;
    } catch (error) {
        console.error("Error fetching CVEs:", error);
        return null;  // Return null or handle it appropriately in the calling code
    }
};

export const verifyFile = async (fileUrl) => {
    try {
        const response = await axios.post(`${API_BASE_URL}/verify-file`, { file_url: fileUrl });
        return response.data;
    } catch (error) {
        console.error("Error verifying file:", error);
        return null;  // Return null or handle it appropriately in the calling code
    }
};
