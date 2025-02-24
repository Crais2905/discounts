import './CategorySlider.css'
import Card from '../Card/Card'


export default function CategorySlider({ categories }) {
    return (
        <section className='category-section'>
           <h2>Product Category</h2>
           <div className='card-container'>
           {categories.map((category) => (
                    <Card key={category.id} title={category.title} />
                ))}
           </div>
            
        </section>
    )
}