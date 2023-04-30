import React from 'react'
import { Nav, NavItem, NavLink } from 'react-bootstrap'
import { NavLink as RRNavLink, useLocation } from 'react-router-dom'
import './SideBar.css'
import {titles} from '../titles.js'

const SideBar = () => {
    const location = useLocation()

    return (
        <Nav className='flex-column'>
            <NavItem className={`sidebar__item ${ location.pathname === '/task1' ? 'active-sidebar-link' : '' } }`} >
                <NavLink href='/task1'>{titles[0]}</NavLink>
            </NavItem>
            <NavItem className={`sidebar__item ${ location.pathname === '/task2' ? 'active-sidebar-link' : '' } }`} >
                <NavLink href='/task2' >
                    {titles[1]}
                </NavLink>
            </NavItem>
            <NavItem className={`sidebar__item ${ location.pathname === '/task3' ? 'active-sidebar-link' : '' } }`} >
                <NavLink href='/task3' >
                    {titles[2]}
                </NavLink>
            </NavItem>
            <NavItem className={`sidebar__item ${ location.pathname === '/task4' ? 'active-sidebar-link' : '' } }`} >
                <NavLink href='/task4' >
                    {titles[3]}
                </NavLink>
            </NavItem>
            <NavItem className={`sidebar__item ${ location.pathname === '/task5' ? 'active-sidebar-link' : '' } }`} >
                <NavLink href='/task5' >
                    {titles[4]}
                </NavLink>
            </NavItem>
            <NavItem className={`sidebar__item ${ location.pathname === '/task6' ? 'active-sidebar-link' : '' } }`} >
                <NavLink href='/task6' >
                    {titles[5]}
                </NavLink>
            </NavItem>
            <NavItem className={`sidebar__item ${ location.pathname === '/task7' ? 'active-sidebar-link' : '' } }`} >
                <NavLink href='/task7' >
                    {titles[6]}
                </NavLink>
            </NavItem>
            <NavItem className={`sidebar__item ${ location.pathname === '/task8' ? 'active-sidebar-link' : '' } }`} >
                <NavLink href='/task8' >
                    {titles[7]}
                </NavLink>
            </NavItem>
            <NavItem className={`sidebar__item ${ location.pathname === '/task9' ? 'active-sidebar-link' : '' } }`} >
                <NavLink href='/task9' >
                    {titles[8]}
                </NavLink>
            </NavItem>
            <NavItem className={`sidebar__item ${ location.pathname === '/task10' ? 'active-sidebar-link' : '' } }`} >
                <NavLink href='/task10' >
                    {titles[9]}
                </NavLink>
            </NavItem>
            <NavItem className={`sidebar__item ${ location.pathname === '/task11' ? 'active-sidebar-link' : '' } }`} >
                <NavLink href='/task11' >
                    {titles[10]}
                </NavLink>
            </NavItem>
            <NavItem className={`sidebar__item ${ location.pathname === '/task12' ? 'active-sidebar-link' : '' } }`} >
                <NavLink href='/task12' >
                    {titles[11]}
                </NavLink>
            </NavItem>
            <NavItem className={`sidebar__item ${ location.pathname === '/task13' ? 'active-sidebar-link' : '' } }`} >
                <NavLink href='/task13' >
                    {titles[12]}
                </NavLink>
            </NavItem>
        </Nav>
    )
}
export default SideBar
