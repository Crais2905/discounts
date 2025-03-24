import './Navigation.css'
import { FaBeer } from "react-icons/fa";
import { Link } from 'react-router-dom';

export default function () {
    return (
        <nav>
            <ul>
                <Link to={'/'}><li>Головна <i className='fa-solid fa-house'></i></li></Link>
                <Link to={ '/products'} ><li>Продукти <i className='fa-solid fa-store'></i></li></Link>
                <Link><li>Контакти <i className='fa-solid fa-envelope'></i></li></Link>
                <Link><li>Обране <i className='fa-solid fa-bookmark'></i></li></Link>
                <Link><li>Профіль <i className='fa-solid fa-user'></i></li></Link>
            </ul>
        </nav>
    )
}