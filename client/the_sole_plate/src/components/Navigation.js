import { Navbar, NavLink } from 'react-bootstrap'
const Navigation = () => {
    return (
        <Navbar bg='dark' variant='dark' expand='sm'>
            <div className="ms-5">
                <NavLink style={{"font-size": "24px"}} href='/'>
                    The Sole Plate
                </NavLink>
            </div>
        </Navbar>
    )
}

export default Navigation
