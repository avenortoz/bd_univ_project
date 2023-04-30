import { BrowserRouter, Route, Routes } from 'react-router-dom'
import { Container, Row, Col } from 'react-bootstrap'
import Navigation from './components/Navigation'
import SideBar from './components/SideBar'
import Task1 from './components/tasks/Task1'
import Task2 from './components/tasks/Task2'
import Task3 from './components/tasks/Task3'
import 'bootstrap/dist/css/bootstrap.min.css'
import './style.css'
import './App.css'

function App() {
    return (
        <div>
            <BrowserRouter>
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
                            height: '100vh',
                            overflowY: 'scroll',
                            top: 0,
                            position: 'sticky'
                        }}
                    >
                        <SideBar />
                    </Col>
                    <Col
                        sm={12}
                        md={9}
                        lg={10}
                        style={{ flex: 5/* , backgroundColor: '#e5e5e5'  */}}
                    >
                        <Container>
                            <div>
                                <Routes>
                                    <Route path='/' element={<div></div>} />
                                    <Route path='/task1' element={<Task1 />} />
                                    <Route path='/task2' element={<Task2 />} />
                                    <Route path='/task3' element={<Task3 />} />
                                </Routes>
                            </div>
                        </Container>
                    </Col>
                </div>
            </BrowserRouter>
        </div>
    )
}

export default App
