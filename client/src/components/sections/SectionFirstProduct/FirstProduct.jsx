import './FirstProduct.css'
import Card from '../../Card/Card'


export default function FirstProduct({ products }) {
    return (
        <section className='product-section'>
           <h2>Products</h2>
           <div className='card-container'>
           {products.slice(0, 5).map((product) => (
                    <Card key={product.id} id={product.id} title={product.name} />
                ))}
           </div>
        </section>
    )
}
