import { useParams } from 'react-router-dom';
import { useEffect, useState } from 'react';
import  Button  from '../../Button/Button'
import axios from 'axios';

import Header from '../../Header/Header'
import SectionProducts from "../../sections/SectionProducts/SectionProducts";

export default function ProductPage() {
    const { id } = useParams();
    const [products, setProducts] = useState([])

    const fetchProducts = () => {
            axios.get('http://127.0.0.1:8000/products/').then(r => {
            const response = r.data;
            setProducts(response)
            });
        };

     useEffect(() => {
            fetchProducts();
        }, []);
    
    if (!products) return <p>Loading...</p>;

    return (
        <>
            <Header></Header>      
            <SectionProducts  products={products}/>
        </>

    );
}   