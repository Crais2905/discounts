import './FirstProduct.css'
import Card from '../../Card/Card'


export default function FirstProduct({ products }) {
    return (
        <section className='product-section'>
           <h2>Products</h2>
           <div className='card-container'>
           {products.slice(0, 4).map((product) => (
                    <Card 
                        key={product.id}
                        id={product.id} 
                        title={product.name}
                        image_url={product.image_url}
                        old_price = {product.old_price}
                        new_price = {product.new_price}
                        url_in_store = {product.url_in_store}
                     />
                ))}
           </div>
        </section>
    )
}
