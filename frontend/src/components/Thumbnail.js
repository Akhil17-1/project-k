import React from 'react';
import { Link } from 'react-router-dom';
import './Thumbnail.css';

const Thumbnail = ({ logType, count, lastCollected }) => {
    return (
        <div className="thumbnail">
            <h3>{logType}</h3>
            <p>{count} logs</p>
            <p>Last collected: {lastCollected}</p>
            <Link to={`/${logType.toLowerCase().replace(' ', '-')}-logs`}>View Logs</Link>
        </div>
    );
};

export default Thumbnail;
