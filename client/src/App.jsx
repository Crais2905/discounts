import React, { useEffect, useState } from 'react';
import Header from './components/Header/Header'
import BigPhoto from './components/SectionBigPhoto/BigPhoto'
import CategorySlider from './components/SectionCategory/CategorySlider'
import axios from "axios"

export default function App() {
  const [categories, setCategories] = useState([]);

  const fetchCategory = () => {
    axios.get('http://127.0.0.1:8000/categories/').then(r => {
      const response = r.data;
      setCategories(response); // зберігаємо отримані дані в стейт
    });
  };

  useEffect(() => {
    fetchCategory();
  }, []);

  return (
    <>
      <Header></Header>
      <BigPhoto/>
      <CategorySlider categories={categories}/>
    </>
  )
}

