import './Card.css';
import { Link } from 'react-router-dom';

export default function Card({ id, title, image_url, old_price, new_price, url_in_store }) {
    const likeButtons = document.querySelectorAll(".card__btn");

    likeButtons.forEach((likeButton) => {
    likeButton.addEventListener("click", () => {
        likeButton.classList.toggle("card__btn--like");
    });
    });
    
    return (
        <Link to={ url_in_store } className='card-wrapper'>
            <article className="card">
                <div className="card__preview">
                    <img src={ `${image_url}` } alt="Lakeview Elegance preview"/>
                </div>
                <div className="card__content">
                    <h2 className="card__title">{ title }</h2>
                    <p className="card__description">
                        Nestled along the tranquil shores of a pristine lake, Lakeview Lakeside offers an idyllic escape
                        into nature's embrace. This exquisite property combines rustic charm with modern luxury, featuring a spacious, elegantly
                        designed home with panoramic lake views. Each room is crafted to maximize the connection with the natural surroundings,
                        offering large windows and outdoor spaces that blend seamlessly with the serene lakeside setting.
                    </p>
                    <div className="card__bottom">
                        <div className="card__price">
                            <span className="card__price__span"><s>{ old_price }  </s></span>
                            <b>{ new_price } грн</b>
                        </div>
                        <button className="card__btn">
                            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"
                                strokeWidth="2" stroke="currentColor" fill="none" strokeLinecap="round"
                                strokeLinejoin="round">
                                <path stroke="none" d="M0 0h24v24H0z" fill="none" />
                                <path d="M19.5 12.572l-7.5 7.428l-7.5 -7.428a5 5 0 1 1 7.5 -6.566a5 5 0 1 1 7.5 6.572" />
                            </svg>
                        </button>
                    </div>
                </div>
            </article>
        </Link>
    );
}