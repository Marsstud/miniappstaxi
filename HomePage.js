// src/HomePage.js
import React from 'react';
import { Link } from 'react-router-dom';

function HomePage() {
  return (
    <div>
      <h1>Привествуем вас в Taxi Kolesa</h1>
      <Link to="/form">
        <button>Go to Form</button>
      </Link>
    </div>
  );
}

export default HomePage;
