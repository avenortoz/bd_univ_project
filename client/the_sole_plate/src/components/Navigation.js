import { Navbar } from 'react-bootstrap'
const Navigation = () => {
    return (
        <Navbar bg='dark' variant='dark' expand='sm'>
            <div className='mx-auto text-center'>
                <a className='navbar-brand ms-3' href='/'>
                    The Sole Plate
                </a>
            </div>
        </Navbar>
    )
}

export default Navigation
