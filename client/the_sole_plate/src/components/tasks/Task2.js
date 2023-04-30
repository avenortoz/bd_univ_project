import { useEffect, useState, useRef } from 'react'
import { Container, Form, Button } from 'react-bootstrap'
import Plot from 'react-plotly.js'
import { serverHost } from '../../api.js'
import './options.css'

const Task2 = () => {
    const [data, setData] = useState([])
    const [year, setYear] = useState(2020)
    const [month, setMonth] = useState(1)
    const formRef = useRef(null)
    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await fetch(
                    `${serverHost}/brand-sales-by-part-of-year/${month}/${year}`
                )
                const tmp_data = await response.json()
                setData(
                    tmp_data.map((b) => {
                        return {
                            x: b['BrandName'],
                            y: b['NumberOfPairsSold']
                        }
                    })
                )
                console.log(tmp_data)
            } catch (error) {
                console.error(error)
            }
        }

        fetchData()
    }, [year, month])

    const drawPlot = () => {
        const tmp_data = [
            {
                x: data.map((b) => b.x),
                y: data.map((b) => b.y),
                type: 'bar',
                marker: {
                    color: '#6b8e23'
                }
            }
        ]

        return <Plot data={tmp_data} layout={layout} />
    }

    const layout = {
        title: `${year}/${month}`,
        xaxis: { title: 'Brand' },
        yaxis: { title: 'Number of Sales' },
        plot_bgcolor: '#212529',
        paper_bgcolor: '#212529',
        font: {
            color: '#6b8e23'
        },
        width: 1100,
        height: 800
    }

    const submit = (e) => {
        e.preventDefault()
        const form = formRef.current
        const tyear = parseInt(form.year.value)
        const tmonth = parseInt(form.month.value)
        setYear(tyear)
        setMonth(tmonth)
    }
    return (
        <div className='task'>
            <div className='task__option'>
                <Form ref={formRef} onSubmit={(e) => submit(e)}>
                    <Form.Group className='ms-3 me-3'>
                        <Form.Label>Year:</Form.Label>
                        <Form.Control
                            type='text'
                            name='year'
                            defaultValue={year}
                            placeholder='Enter text'
                        />
                    </Form.Group>
                    <Form.Group className='ms-3 me-3'>
                        <Form.Label>Month:</Form.Label>
                        <Form.Control
                            type='text'
                            name='month'
                            defaultValue={month}
                            placeholder='Enter text'
                        />
                    </Form.Group>
                    <div style={{textAlign: "center", marginTop: "50px"}}>
                        <button type='submit'>
                            Submit
                        </button>
                    </div>
                </Form>
            </div>
            <div style={{ textAlign: 'center' }}>
                <h2> Brand sales by month </h2>
                <Container>{drawPlot()}</Container>
            </div>
        </div>
    )
}

export default Task2
