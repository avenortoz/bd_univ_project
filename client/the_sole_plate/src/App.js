import { BrowserRouter, Route, Routes } from 'react-router-dom'
import { Container, Row, Col } from 'react-bootstrap'
import Navigation from './components/Navigation'
import SideBar from './components/SideBar'
import 'bootstrap/dist/css/bootstrap.min.css'
import './style.css'
import './App.css'

function App() {
    return (
        <div>
            <Navigation />
            <div
                fluid
                className='bg-dark'
                style={{
                    'min-height': '100vh',
                    display: 'flex'
                }}
            >
                <Col
                    sm={12}
                    md={3}
                    lg={2}
                    className='bg-dark'
                    style={{
                        flex: 1,
                        'height': '100vh',
                        overflowY: 'scroll',
                        top: 0,
                        position: "sticky"
                    }}
                >
                    <SideBar/>
                </Col>
                <Col
                    sm={12}
                    md={9}
                    lg={10}
                    style={{ flex: 5, backgroundColor: "#e5e5e5" }}
                >
                    <div style={{position:'sticky'}}>Some wierd</div>
                    <div style={{ 'min-height': '200vh' }}></div>
                </Col>
            </div>
            <BrowserRouter>
                <div>
                    <Routes>
                        <Route path='/' element={<div></div>} />
                    </Routes>
                </div>
            </BrowserRouter>
        </div>
    )
}

export default App
