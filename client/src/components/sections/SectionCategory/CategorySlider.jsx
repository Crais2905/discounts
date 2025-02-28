import './CategorySlider.css'
import Card from '../../Card/Card'


export default function CategorySlider({ categories }) {
    return (
        <section className='category-section'>
           <h2>Product Category</h2>
           <div className='card-container'>
           {categories.slice(0, 5).map((category) => (
                    <Card key={category.id} id={category.id} title={category.title} />
                ))}
           </div>
        </section>
    )
}
