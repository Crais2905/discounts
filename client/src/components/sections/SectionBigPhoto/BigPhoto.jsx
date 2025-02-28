import './BigPhoto.css'
import  Button  from '../../Button/Button'

export default function BigPhoto() {
    return (
        <section className='bigphoto-section'>
            <div className='text-block'>
                <h3>ШУКАЙТЕ АКЦІЙНІ ТОВАРИ ІЗ РІЗНИХ МАГАЗИНІВ ТУТ</h3>
                <Button>Акційні товари</Button>
            </div>
            <img src="bd_main.jpg" alt="" className='photo' />
        </section>
    )
}