import { Nav, NavItem } from 'react-bootstrap'
import React from 'react'

const SideBar = () => {
    return (
        <Nav className='flex-column'>
            <div className='sidebar__item'>
                <NavItem>
                    <Nav.Link href='/option1'>Option 1</Nav.Link>
                </NavItem>
            </div>
            <div className='sidebar__item'>
                <NavItem>
                    <Nav.Link href='/option2'>Option 2</Nav.Link>
                </NavItem>
            </div>
            <div className='sidebar__item'>
                <NavItem>
                    <Nav.Link href='/option3'>Option 3</Nav.Link>
                </NavItem>
            </div>
        </Nav>
    )
}

export default SideBar
