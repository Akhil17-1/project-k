import React, { useState } from 'react';
import { verifyFile } from '../logService';

const VerifyFile = () => {
  const [fileUrl, setFileUrl] = useState('');
  const [result, setResult] = useState(null);

  const handleVerify = async () => {
    const response = await verifyFile(fileUrl);
    setResult(response.status);
  };

  return (
    <div>
      <h2>Verify File Integrity</h2>
      <input
        type="text"
        value={fileUrl}
        onChange={(e) => setFileUrl(e.target.value)}
        placeholder="Enter file URL"
      />
      <button onClick={handleVerify}>Verify</button>
      {result && <p>{result}</p>}
    </div>
  );
};

export default VerifyFile;
