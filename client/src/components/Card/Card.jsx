import './Card.css';
import { Link } from 'react-router-dom';
import { useState } from "react";

export default function Card({ id, title, image_url, old_price, new_price, url_in_store }) {
    const likeButtons = document.querySelectorAll(".card__btn");
    const [isLiked, setIsLiked] = useState(false);

    likeButtons.forEach((likeButton) => {
    likeButton.addEventListener("click", () => {
        likeButton.classList.toggle("card__btn--like");
    });
    });

    const handleClick = (event, id, name ) => {
        event.stopPropagation(); 
        event.preventDefault(); 
        setIsLiked((prev) => !prev);

        if (!isLiked) {
            console.log(`Товар ${id} додано в обране`)
        } else {
            console.log(`Товар ${id} видалено з обраного`)
        }
    }
    
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
                        <button 
                            className={`card__btn ${isLiked ? "card__btn--like" : ""}`} 
                            onClick={(event) => handleClick(event, id, title)}
                            >
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