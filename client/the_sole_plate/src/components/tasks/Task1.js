import { useEffect, useState } from 'react'
import { Container } from 'react-bootstrap'
import Plot from 'react-plotly.js'
import { serverHost } from '../../api.js'

const Task1 = () => {
    const [brands, setBrands] = useState([])
    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await fetch(
                    `${serverHost}/average-product-price-by-brand`
                )
                const data = await response.json()
                setBrands(
                    data.map((b) => {
                        return {
                            x: b['BrandName'],
                            y: b['AveragePrice']
                        }
                    })
                )
                console.log(data)
            } catch (error) {
                console.error(error)
            }
        }

        fetchData()
    }, [])

    const drawPlot = () => {
        const data = [
            {
                x: brands.map((b) => b.x),
                y: brands.map((b) => b.y),
                type: 'bar',
                marker: {
                    color: '#6b8e23'
                }
            }
        ]

        return <Plot data={data} layout={layout}/>
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
        <div style={{ textAlign: 'center' }}>
            <h2> Average products by price </h2>
            <Container>{drawPlot()}</Container>
        </div>
    )
}

export default Task1
