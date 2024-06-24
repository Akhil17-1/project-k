import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './CVETicker.css';

const CVETicker = () => {
    const [cves, setCves] = useState([]);

    useEffect(() => {
        axios.get('https://cve.circl.lu/api/last')
            .then(response => setCves(response.data))
            .catch(error => console.error('Error fetching CVEs:', error));
    }, []);

    return (
        <div className="cve-ticker">
            <h2>Latest CVEs</h2>
            <ul>
                {cves.map((cve, index) => (
                    <li key={index}>
                        <a href={cve.href} target="_blank" rel="noopener noreferrer">
                            {cve.id}: {cve.summary}
                        </a>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default CVETicker;
