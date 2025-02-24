import './Card.css'


export default function Card({ title })  {
    return (
        <div className='card-wrapper'>
            <h3>{title}</h3>
        </div>
    )
}