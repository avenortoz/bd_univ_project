import { BrowserRouter, MemoryRouter, Route, Routes } from 'react-router-dom'
import { Container, Row, Col } from 'react-bootstrap'
import Navigation from './components/Navigation'
import SideBar from './components/SideBar'
import Task2 from './components/tasks/Task2'
import GeneralTaskZeroParameter from './components/tasks/GeneralTaskZeroParameter'
import GeneralTaskZeroParam3d from './components/tasks/GeneralTaskZeroParam3d'
import GeneralTaskZero3d from './components/tasks/GeneralTaskZero3d'
import GeneralTaskZeroParamPercentage from './components/tasks/GeneralTaskZeroParamPercentage'
import GenderTable from './components/tasks/GenderTable'
import GeneralTaskOneParameter from './components/tasks/GeneralTaskOneParameter'

import 'bootstrap/dist/css/bootstrap.min.css'
import './style.css'
import './App.css'
import { titles } from './titles.js'

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
                        style={{ flex: 5 /* , backgroundColor: '#e5e5e5'  */ }}
                    >
                        <Container>
                            <div>
                                <Routes>
                                    <Route path='/' element={<div></div>} />
                                    <Route
                                        path='task0'
                                        element={
                                            <GeneralTaskZeroParameter
                                                title={titles[0]}
                                                api={'average-product-price-by-brand'}
                                                xname={'BrandName'}
                                                yname={'AveragePrice'}
                                            />
                                        }
                                    />
                                    <Route
                                        path='/task1'
                                        element={<Task2 title={titles[1]} />}
                                    />

                                    <Route
                                        path='/task2'
                                        element={
                                            <GeneralTaskOneParameter
                                                title={titles[2]}
                                                api={'brand-sales-by-year'}
                                                param1={'year'}
                                                param1DefaultValue={2020}
                                                xname={'BrandName'}
                                                yname={'NumberOfPairsSold'}
                                            />
                                        }
                                    />
                                    <Route
                                        path='/task3'
                                        element={
                                            <GeneralTaskOneParameter
                                                title={titles[3]}
                                                api={'costs-by-month'}
                                                param1={'year'}
                                                param1DefaultValue={2020}
                                                xname={'Month'}
                                                yname={'Costs'}
                                            />
                                        }
                                    />
                                    <Route
                                        path='/task4'
                                        element={
                                            <GeneralTaskZeroParameter
                                                title={titles[4]}
                                                api={'costs-by-year'}
                                                xname={'Year'}
                                                yname={'Costs'}
                                            />
                                        }
                                    />
                                    <Route
                                        path='/task5'
                                        element={
                                            <GeneralTaskZeroParameter
                                                title={titles[5]}
                                                api={'company-shoe-deliveries'}
                                                xname={'CompanyName'}
                                                yname={'NumberOfPairs'}
                                            />
                                        }
                                    />
                                    <Route
                                        path='/task6'
                                        element={
                                            <GeneralTaskOneParameter
                                                title={titles[6]}
                                                api={'discount-losses-by-month'}
                                                param1={'year'}
                                                param1DefaultValue={2020}
                                                xname={'Month'}
                                                yname={'DiscountLosses'}
                                            />
                                        }
                                    />
                                    <Route
                                        path='/task7'
                                        element={
                                            <GeneralTaskZeroParameter
                                                title={titles[7]}
                                                api={'discount-losses-by-year'}
                                                xname={'Year'}
                                                yname={'DiscountLosses'}
                                            />
                                        }
                                    />
                                    <Route
                                        path='/task8'
                                        element={
                                            <GeneralTaskOneParameter
                                                title={titles[8]}
                                                api={'profit-by-month'}
                                                param1={'year'}
                                                param1DefaultValue={2020}
                                                xname={'Month'}
                                                yname={'Profit'}
                                            />
                                        }
                                    />
                                    <Route
                                        path='/task9'
                                        element={
                                            <GeneralTaskZeroParameter
                                                title={titles[9]}
                                                api={'profit-by-year'}
                                                xname={'Year'}
                                                yname={'Profi'}
                                            />
                                        }
                                    />
                                    <Route
                                        path='/task10'
                                        element={
                                            <GeneralTaskOneParameter
                                                title={titles[10]}
                                                api={'profit-by-season'}
                                                param1={'year'}
                                                param1DefaultValue={2020}
                                                xname={'Season'}
                                                yname={'Profit'}
                                            />
                                        }
                                    />
                                    <Route
                                        path='/task11'
                                        element={
                                            <GeneralTaskZeroParameter
                                                title={titles[11]}
                                                api={'top-5-active-customers'}
                                                xname={'CustomerName'}
                                                yname={'TotalOrders'}
                                                plot_type="pie"
                                            />
                                        }
                                    />
                                    <Route
                                        path='/task12'
                                        element={
                                            <GeneralTaskZeroParameter
                                                title={titles[12]}
                                                api={'top-5-popular-products'}
                                                xname={'ProductName'}
                                                yname={'TotalSold'}
                                                plot_type="pie"
                                            />
                                        }
                                    />
                                    <Route
                                        path='/task13'
                                        element={
                                            <GeneralTaskOneParameter
                                                title={titles[13]}
                                                api={'costs-by-part-of-year'}
                                                param1={'year'}
                                                param1DefaultValue={2020}
                                                xname={'PartOfYear'}
                                                yname={'Costs'}
                                                plot_type='pie'
                                            />
                                        }
                                    />

                                    <Route
                                        path='/task14'
                                        element={
                                            <GeneralTaskOneParameter
                                                title={titles[14]}
                                                api={'discount-losses-by-part-of-year'}
                                                param1={'year'}
                                                param1DefaultValue={2020}
                                                xname={'PartOfYear'}
                                                yname={'DiscountLosses'}
                                            />
                                        }
                                    />
                                    <Route
                                        path='/task16'
                                        element={
                                            <GeneralTaskOneParameter
                                                title={titles[16]}
                                                api={'income-by-every-month'}
                                                param1={'year'}
                                                param1DefaultValue={2020}
                                                xname={'Month'}
                                                yname={'Income'}
                                            />
                                        }
                                    />
                                    <Route
                                        path='/task17'
                                        element={
                                            <GeneralTaskZeroParameter
                                                title={titles[17]}
                                                api={'income-by-year'}
                                                xname={'Year'}
                                                yname={'Income'}
                                            />
                                        }
                                    />

                                    <Route
                                        path='/task18'
                                        element={
                                            <GeneralTaskZeroParameter
                                                title={titles[18]}
                                                api={'job-title-and-salary'}
                                                xname={'JobTitle'}
                                                yname={'AverageSalary'}
                                            />
                                        }
                                    />
                                    <Route
                                        path='/task26'
                                        element={
                                            // <GeneralTaskZeroParameter
                                            //     title={titles[26]}
                                            //     api={'purchased-shoe-sizes'}
                                            //     xname={'ShoeName'}
                                            //     yname={'NumberOfPairsPurchased'}
                                            // />
                                            <GeneralTaskZero3d
                                                title={titles[26]}
                                                api={'purchased-shoe-sizes'}
                                                xname={'ShoeName'}
                                                yname={'NumberOfPairsPurchased'}
                                                zname={'ShoeSize'}
                                            />
                                        }
                                    />
                                    <Route
                                        path='/task27'
                                        element={
                                            <GeneralTaskZeroParamPercentage
                                                title={titles[27]}
                                                api={
                                                    'sales-percentage-by-material'
                                                }
                                                xname={'MaterialName'}
                                                yname={'TotalSold'}
                                            />
                                        }
                                    />
                                    <Route
                                        path='/task28'
                                        element={
                                            <GeneralTaskZeroParamPercentage
                                                title={titles[28]}
                                                api={'shoe-type-percentage'}
                                                xname={'Category'}
                                                yname={'NumberOfShoes'}
                                            />
                                        }
                                    />
                                    <Route
                                        path='/task29'
                                        element={
                                            <GeneralTaskZeroParamPercentage
                                                title={titles[29]}
                                                api={
                                                    'shoe-type-percentage-by-brand'
                                                }
                                                xname={'Name'}
                                                yname={'NumberOfShoes'}
                                            />
                                        }
                                    />
                                    <Route
                                        path='/task30'
                                        element={
                                            <GeneralTaskZeroParamPercentage
                                                title={titles[30]}
                                                api={
                                                    'shoe-type-percentage-by-company'
                                                }
                                                xname={'Name'}
                                                yname={'NumberOfShoes'}
                                            />
                                        }
                                    />
                                    <Route
                                        path='/task31'
                                        element={
                                            <GeneralTaskZeroParameter
                                                title={titles[31]}
                                                api={'customers-by-sex'}
                                                xname={'Sex'}
                                                yname={'NumberOfCustomers'}
                                                plot_type='pie'
                                            />
                                        }
                                    />
                                    <Route
                                        path='/task32'
                                        element={
                                            <GeneralTaskZeroParam3d
                                                title={titles[32]}
                                                api={'monthly-sales-by-sex'}
                                                xname={'Sex'}
                                                yname={'NumberOfPairsSold'}
                                                zname={'Month'}
                                            />
                                        }
                                    />
                                    <Route
                                        path='/task33'
                                        element={
                                            <GeneralTaskZeroParamPercentage
                                                title={titles[33]}
                                                api={
                                                    'supplier-pairs-percentage'
                                                }
                                                xname={'Supplier'}
                                                yname={'NumberOfPairs'}
                                            />
                                        }
                                    />
                                    <Route
                                        path='/task34'
                                        element={
                                            <GeneralTaskZero3d
                                                title={titles[34]}
                                                api={'shoe-type-sales-by-year'}
                                                xname={'Category'}
                                                yname={'NumberOfPairsSold'}
                                                zname={'Year'}
                                                plot_type="bar"
                                            />
                                        }
                                    />

                                    <Route
                                        path='/task35'
                                        element={
                                            <GeneralTaskOneParameter
                                                title={titles[35]}
                                                api={'shoe-type-sales-by-month'}
                                                param1={'year'}
                                                param1DefaultValue={2020}
                                                xname={'Month'}
                                                yname={'NumberOfPairsSold'}
                                            />
                                        }
                                    />
                                    <Route
                                        path='/task36'
                                        element={
                                            <GeneralTaskOneParameter
                                                title={titles[36]}
                                                api={
                                                    'shoe-type-sales-by-season'
                                                }
                                                param1={'year'}
                                                param1DefaultValue={2020}
                                                xname={'Category'}
                                                yname={'NumberOfPairsSold'}
                                            />
                                        }
                                    />

                                    <Route
                                        path='/task37'
                                        element={
                                            <GenderTable
                                                title={titles[37]}
                                                api={'customers/sex/m'}
                                            />
                                        }
                                    />
                                    <Route
                                        path='/task38'
                                        element={
                                            <GenderTable
                                                title={titles[38]}
                                                api={'customers/sex/w'}
                                            />
                                        }
                                    />
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
