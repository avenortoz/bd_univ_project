import { BrowserRouter, Route, Routes } from 'react-router-dom'
import { Container, Row, Col } from 'react-bootstrap'
import Navigation from './components/Navigation'
import SideBar from './components/SideBar'
import Task1 from './components/tasks/Task1'
import Task2 from './components/tasks/Task2'
import Task3 from './components/tasks/Task3'
import CostByMonth from './components/tasks/CostByMonth'
import CostByYear from './components/tasks/CostByYear'
import CompanyShoesDeliveres from './components/tasks/CompanyShoesDeliveres'
import DiscountLossesByMonth from './components/tasks/DiscountLossesByMonth'
import DiscountLossesByYear from './components/tasks/DiscountLossesByYear'
import ProfitByYear from './components/tasks/ProfitByYear'
import ProfitByMonth from './components/tasks/ProfitByMonth'
import ProfitBySeason from './components/tasks/ProfitBySeason'
import Top5ActiveCustomers from './components/tasks/Top5ActiveCustomers'
import Top5PopularProducts from './components/tasks/Top5PopularProducts'
import 'bootstrap/dist/css/bootstrap.min.css'
import './style.css'
import './App.css'
import {titles} from './titles.js'

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
                                    <Route path='/task1' element={<Task1 title={titles[0]} />} />
                                    <Route path='/task2' element={<Task2 title={titles[1]} />} />
                                    <Route path='/task3' element={<Task3 title={titles[2]} />} />
                                    <Route path='/task4' element={<CostByMonth title={titles[3]} />} />
                                    <Route path='/task5' element={<CostByYear title={titles[4]} />} />
                                    <Route path='/task6' element={<CompanyShoesDeliveres title={titles[5]} />} />
                                    <Route path='/task7' element={<DiscountLossesByMonth title={titles[6]} />} />
                                    <Route path='/task8' element={<DiscountLossesByYear title={titles[7]} />} />
                                    <Route path='/task9' element={<ProfitByMonth title={titles[8]} />} />
                                    <Route path='/task10' element={<ProfitByYear title={titles[9]} />} />
                                    <Route path='/task11' element={<ProfitBySeason title={titles[10]} />} />
                                    <Route path='/task12' element={<Top5ActiveCustomers title={titles[11]} />} />
                                    <Route path='/task13' element={<Top5PopularProducts title={titles[12]} />} />
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
