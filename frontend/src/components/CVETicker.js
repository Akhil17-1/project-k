// src/components/CVETicker.js
import React, { useEffect, useState } from 'react';
import styled from 'styled-components';
import axios from 'axios';

const TickerContainer = styled.div`
  width: 100%;
  background-color: #111;
  color: white;
  overflow: hidden;
  white-space: nowrap;
  box-sizing: border-box;
`;

const TickerContent = styled.div`
  display: inline-block;
  padding-left: 100%;
  animation: ticker 20s linear infinite;

  @keyframes ticker {
    0% { transform: translateX(100%); }
    100% { transform: translateX(-100%); }
  }
`;

const CVETicker = () => {
  const [cves, setCves] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:5000/cves')
      .then(response => {
        setCves(response.data);
      })
      .catch(error => {
        console.error('Error fetching CVEs:', error);
      });
  }, []);

  return (
    <TickerContainer>
      <TickerContent>
        {cves.map(cve => (
          <span key={cve.id}>{cve.id}: {cve.description} &nbsp;|&nbsp; </span>
        ))}
      </TickerContent>
    </TickerContainer>
  );
};

export default CVETicker;
