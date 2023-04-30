
import { useEffect, useState, useRef } from 'react'
import { Container, Form, Button } from 'react-bootstrap'
import Plot from 'react-plotly.js'
import { serverHost } from '../../api.js'
import './options.css'

const ProfitByMonth = ({title}) => {
    const [data, setData] = useState([])
    const [year, setYear] = useState(2020)
    const formRef = useRef(null)
    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await fetch(
                    `${serverHost}/profit-by-month/${year}`
                )
                const tmp_data = await response.json()
                setData(
                    tmp_data.map((b) => {
                        return {
                            y: b['Profit'],
                            x: b['Month']
                        }
                    })
                )
                console.log(tmp_data)
            } catch (error) {
                console.error(error)
            }
        }

        fetchData()
    }, [year])

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
        title: `${year}`,
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
        setYear(tyear)
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
                    <div style={{textAlign: "center", marginTop: "50px"}}>
                        <button type='submit'>
                            Submit
                        </button>
                    </div>
                </Form>
            </div>
            <div style={{ textAlign: 'center' }}>
                <h2>{title}</h2>
                <Container>{drawPlot()}</Container>
            </div>
        </div>
    )
}

export default ProfitByMonth
