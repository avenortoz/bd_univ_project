import { useEffect, useState } from 'react'
import { Container } from 'react-bootstrap'
import Plot from 'react-plotly.js'
import { serverHost } from '../../api.js'

const GeneralTaskZeroParamPercentage = ({title, api, xname, yname}) => {
    const [brands, setBrands] = useState([])
    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await fetch(
                    `${serverHost}/${api}`
                )
                const data = await response.json()
                setBrands(
                    data.map((b) => {
                        return {
                            x: b[xname],
                            y: b[yname]
                        }
                    })
                )
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
        ];
        const data1 = [
            {
                labels: brands.map((b) => b.x),
                values: brands.map((b) => b.y),
                type: 'pie',
                marker: {
                    color: '#6b8e23'
                }
            }
        ]

        return <>
            <Plot data={data} layout={layout}/>
            <Plot data={data1} layout={layout}/>
            </>
    }

    const layout = {
        xaxis: { title: {xname} },
        yaxis: { title: {yname} },
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
            <h2>{title}</h2>
            <Container>{drawPlot()}</Container>
        </div>
    )
}

export default GeneralTaskZeroParamPercentage
