import React, { useEffect, useState } from 'react';

import CategorySlider from "../../sections/SectionCategory/CategorySlider";
import FirstProduct from "../../sections/SectionFirstProduct/FirstProduct";
import BigPhoto from '../../sections/SectionBigPhoto/BigPhoto'
import Header from '../../Header/Header'
// import './App.css'


// import CategorySlider from './components/SectionCategory/CategorySlider'
import axios from "axios"

export default function MainPage() {
    const [categories, setCategories] = useState([]);
    const [products, setProducts] = useState([])

    const fetchCategory = () => {
        axios.get('http://127.0.0.1:8000/categories/?limit=5').then(r => {
        const response = r.data;
        setCategories(response); // зберігаємо отримані дані в стейт
        });
    };

    const fetchProducts = () => {
        axios.get('http://127.0.0.1:8000/products/').then(r => {
        const response = r.data;
        setProducts(response)
        });
    };

    useEffect(() => {
        fetchCategory();
        fetchProducts();
    }, []);

    return (
        <>
        <Header/>
        <BigPhoto/>
        {/* <CategorySlider categories={categories}/> */}
        <FirstProduct products={products}/>
        </>
    );
}

