import './Navigation.css'
import { FaBeer } from "react-icons/fa";

export default function () {
    return (
        <nav>
            <ul>
                <li>Головна <i className='fa-solid fa-house'></i></li>
                <li>Продукти <i className='fa-solid fa-store'></i></li>
                <li>Контакти <i className='fa-solid fa-envelope'></i></li>
                <li>Обране <i className='fa-solid fa-bookmark'></i></li>
                <li>Профіль <i className='fa-solid fa-user'></i></li>
            </ul>
        </nav>
    )
}