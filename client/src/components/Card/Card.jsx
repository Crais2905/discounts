// import './Card.css'


// export default function Card({ title })  {
//     return (
//         <div className='card-wrapper'>
//             <h3>{title}</h3>
//         </div>
//     )
// }

import './Card.css';
import { Link } from 'react-router-dom';

export default function Card({ id, title }) {
    return (
        <Link to={`/product/${id}`} className='card-wrapper'>
            <h3>{title}</h3>
        </Link>
    );
}