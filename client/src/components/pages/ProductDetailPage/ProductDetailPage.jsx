import { useParams } from 'react-router-dom';
import { useEffect, useState } from 'react';
import  Button  from '../../Button/Button'
import axios from 'axios';

export default function ProductPage() {
    const { id } = useParams();
    const [product, setProduct] = useState(null);

    useEffect(() => {
        axios.get(`http://127.0.0.1:8000/products/${id}/`)
            .then(r => setProduct(r.data))
            .catch(err => console.error('Error fetching product details:', err));
    }, [id]);

    if (!product) return <p>Loading...</p>;

    return (
        <div>
            <h2>{product.name}</h2>
            <s>{product.old_price}</s>
            <p>Price: <b>{product.new_price}</b></p>
            <Button>Go to market</Button>
        </div>
    );
}   