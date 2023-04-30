import React from 'react'
import { Nav, NavItem, NavLink } from 'react-bootstrap'
import { NavLink as RRNavLink, useLocation } from 'react-router-dom'
import './SideBar.css'

const SideBar = () => {
    const location = useLocation()

    return (
        <Nav className='flex-column'>
            <NavItem className={`sidebar__item ${ location.pathname === '/task1' ? 'active-sidebar-link' : '' } }`} >
                <NavLink href='/task1'>Average Product Price by Brand</NavLink>
            </NavItem>
            <NavItem className={`sidebar__item ${ location.pathname === '/task2' ? 'active-sidebar-link' : '' } }`} >
                <NavLink href='/task2' >
                    Кількість проданих пар для бренду поквартально
                </NavLink>
            </NavItem>
            <NavItem className={`sidebar__item ${ location.pathname === '/task3' ? 'active-sidebar-link' : '' } }`} >
                <NavLink href='/task3' >
                    Кількість проданих пар для бренду за рік
                </NavLink>
            </NavItem>
            <NavItem className={`sidebar__item ${ location.pathname === '/task4' ? 'active-sidebar-link' : '' } }`} >
                <NavLink href='/task4' >
                    Витрати за місяць
                </NavLink>
            </NavItem>

            <NavItem className={`sidebar__item ${ location.pathname === '/task5' ? 'active-sidebar-link' : '' } }`} >
                <NavLink href='/task5' >
                    Витрати за роках
                </NavLink>
            </NavItem>
        </Nav>
    )
}
export default SideBar

// import { Nav, NavItem } from 'react-bootstrap'
// import React from 'react'
//
//
// const SideBar = () => {
//     return (
//         <Nav className='flex-column'>
//             <div className='sidebar__item'>
//                 <NavItem>
//                     <Nav.Link href='/task1'>Task 1</Nav.Link>
//                 </NavItem>
//             </div>
//             <div className='sidebar__item'>
//                 <NavItem>
//                     <Nav.Link href='/task2'>Task 2</Nav.Link>
//                 </NavItem>
//             </div>
//             <div className='sidebar__item'>
//                 <NavItem>
//                     <Nav.Link href='/task3'>Task 3</Nav.Link>
//                 </NavItem>
//             </div>
//         </Nav>
//     )
// }
//
// export default SideBar
