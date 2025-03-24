import './BigPhoto.css'
import Button from '../../Button/Button'
import { Link } from 'react-router-dom';

export default function BigPhoto() {
    return (
        <section className='bigphoto-section'>
            <div className='text-block'>
                <h1>ШУКАЙТЕ АКЦІЙНІ ТОВАРИ ІЗ РІЗНИХ МАГАЗИНІВ ТУТ</h1>
                <Link to={ '/products'} ><Button >Акційні товари</Button></Link>
            </div>
            <img src="bd_main.jpg" alt="" className='photo' />
        </section>
    )
}