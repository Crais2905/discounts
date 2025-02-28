import './App.css'

import React, { useEffect, useState } from 'react';
import { Routes, Route } from 'react-router-dom';

import ProductPage from './components/pages/ProductDetailPage/ProductDetailPage';
import MainPage from './components/pages/MainPage/MainPage';


export default function App() {


  return (
    <>
      <Routes>
        <Route path="/" element={<MainPage/>} />
        <Route path="/product/:id" element={<ProductPage />} />
      </Routes>
    </>
  );
}

