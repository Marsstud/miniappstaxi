// src/DataFormPage.js
import React, { useState } from 'react';

function DataFormPage() {
  const [data, setData] = useState('');

  const sendData = () => {
    window.Telegram.WebApp.sendData(data);
  };

  return (
    <div>
      <h1>Data Form</h1>
      <input 
        type="text" 
        value={data} 
        onChange={(e) => setData(e.target.value)} 
        placeholder="Enter data"
      />
      <button onClick={sendData}>Send</button>
    </div>
  );
}

export default DataFormPage;
