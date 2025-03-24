import './SectionProducts.css'
import ItemProduct from '../../ItemProduct/ItemProduct'


export default function SectionProducts({ products }) {
    return (
        <section className='product-section'>
           <h2>Акційні товари</h2>
           <div className='product-container'>
           {products.slice(0, 10).map((product) => (
                    <ItemProduct
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