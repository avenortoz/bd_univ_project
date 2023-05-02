import React from 'react'
import { Nav, NavItem, NavLink } from 'react-bootstrap'
import { NavLink as RRNavLink, useLocation } from 'react-router-dom'
import './SideBar.css'
import { titles } from '../titles.js'

const SideBar = () => {
    const location = useLocation()
    const genNavItems = () => {
        const excluded = [25,24,23,22,21, 20, 19, 15]
        const navItems = []

        for (let i = 0; i <= 38; i++) {
            if (excluded.indexOf(i) !== -1) continue

            navItems.push(
                <NavItem
                    className={`sidebar__item ${
                        location.pathname === `/task${i}` ? 'active-sidebar-link' : ''
                    }`}
                >
                    <NavLink href={`/task${i}`}>{titles[i]}</NavLink>
                </NavItem>
            )
        }

        return navItems
    }
    return (
        <Nav className='flex-column'>
            {genNavItems()}
        </Nav>
    )
}
export default SideBar
