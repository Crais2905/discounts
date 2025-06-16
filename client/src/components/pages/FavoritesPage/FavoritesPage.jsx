import { useState, useEffect } from "react";
import Cookies from 'js-cookie';
import axios from 'axios';

import Header from '../../Header/Header'
import SectionProducts from "../../sections/SectionProducts/SectionProducts";

export default function Favorites() {
    const [products, setProducts] = useState([])

    useEffect(() => {
        const fetchProducts = () => {
            const rawIds = Cookies.get('favorite');
            console.log(rawIds)
            if (!rawIds) return;

            const ids = rawIds.split(" "); 

           
           
            const requests = ids.map(id =>
                axios.get(`http://127.0.0.1:8000/products/${id}`)
                    .then(res => res.data)
                    .catch(() => null) // щоб не впав весь ланцюг
                    
            );
            console.log(requests)

            Promise.all(requests).then(results => {
                setProducts(results.filter(Boolean));
            });
            setProducts(requests.filter(Boolean));
        };

        fetchProducts();
    }, []); // пустий масив залежностей — лише 1 раз при монтуванні

    // console.log(products)

    return (
        <>
            <Header/>
            <SectionProducts products={products} title={'Обрані товари'} />
        </>
            
    );
}