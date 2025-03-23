import './App.css'

import React, { useEffect, useState } from 'react';
import { Routes, Route } from 'react-router-dom';

import ProductPage from './components/pages/ProductDetailPage/ProductDetailPage';
import MainPage from './components/pages/MainPage/MainPage';
import ProductsPage from './components/pages/ProductsPage/ProductsPage'


export default function App() {


  return (
    <>
      <Routes>
        <Route path="/" element={<MainPage/>} />
        {/* <Route path="/product/:id" element={<ProductPage />} /> */}
        <Route path='/products' element={<ProductsPage/>} />
      </Routes>
    </>
  );
}

