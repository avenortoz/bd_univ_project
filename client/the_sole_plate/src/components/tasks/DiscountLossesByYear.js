import { useEffect, useState, useRef } from 'react'
import { Container, Form, Button } from 'react-bootstrap'
import Plot from 'react-plotly.js'
import { serverHost } from '../../api.js'
import './options.css'

const DiscountLossesByYear = ({title}) => {
    const [data, setData] = useState([])
    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await fetch(
                    `${serverHost}/discount-losses-by-year`
                )
                const tmp_data = await response.json()
                setData(
                    tmp_data.map((b) => {
                        return {
                            x: b['Year'],
                            y: b['DiscountLosses']
                        }
                    })
                )
                console.log(tmp_data)
            } catch (error) {
                console.error(error)
            }
        }

        fetchData()
    }, [])

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
        xaxis: { title: 'Brand' },
        yaxis: { title: 'Number of Sales' },
        plot_bgcolor: '#212529',
        paper_bgcolor: '#212529',
        font: {
            color: '#6b8e23'
        },
        width: 1200,
        height: 800
    }

    return (
        <div className='task'>
            <div style={{ textAlign: 'center' }}>
                <h2>{title}</h2>
                <Container>{drawPlot()}</Container>
            </div>
        </div>
    )
}

export default DiscountLossesByYear
