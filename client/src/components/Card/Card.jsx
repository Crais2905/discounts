import './Card.css';

import { Link } from 'react-router-dom';

export default function Card({ id, title, image_url, old_price, new_price, url_in_store }) {
   
    return (
        <Link to={ url_in_store } className='card-wrapper'>
            <article className="card">
                <div className="card__preview">
                    <img src={ `${image_url}` } alt="Lakeview Elegance preview"/>
                </div>
                <div className="card__content">
                    <h3 className="card__title"> {title.length > 50 ? title.slice(0, 50) + "..." : title}</h3>
                    <div className="card__bottom">
                        <div className="card__price">
                            <span className="card__price__span"><s>{ old_price }  </s></span>
                            <b>{ new_price } грн</b>
                        </div>
                    </div>
                </div>
            </article>
        </Link>
    );
}