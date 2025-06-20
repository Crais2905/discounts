import './ItemProduct.css';
import { Link } from 'react-router-dom';

export default function Card({ id, title, image_url, old_price, new_price, url_in_store }) {
    const likeButtons = document.querySelectorAll(".card__btn");

    // likeButtons.forEach((likeButton) => {
    // likeButton.addEventListener("click", () => {
    //     likeButton.classList.toggle("card__btn--like");
    // });
    // });
    
    return (
        <Link to={ url_in_store } className='item-wrapper' key={ id }>
            <article className="item" >
                <div className='item-image'>
                    <img src={ `${image_url}` } alt="" />
                </div>
                <div className='item-content'>
                    <h3>{ title }</h3>
                </div>
            </article>
        </Link>
    );
}