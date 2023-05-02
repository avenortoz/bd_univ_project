import { useEffect, useState } from 'react'
import { Container } from 'react-bootstrap'
import Plot from 'react-plotly.js'
import { serverHost } from '../../api.js'

const colors = ['#BE6069', '#5D80AB', '#B38DAC', '#6b8e23', '#ff9933']

const GeneralTaskZeroParameter = ({
    title,
    api,
    xname,
    yname,
    plot_type = 'bar'
}) => {
    const color = colors[Math.floor(Math.random() * colors.length)]
    const [brands, setBrands] = useState([])
    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await fetch(`${serverHost}/${api}`)
                const data = await response.json()
                setBrands(
                    data.map((b) => {
                        return {
                            x: b[xname],
                            y: b[yname]
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
        let data
        if (plot_type === 'pie') {
            data = [
                {
                    labels: brands.map((b) => b.x),
                    values: brands.map((b) => b.y),
                    type: 'pie',
                    marker: {
                        color: color
                    }
                }
            ]
        } else {
            data = [
                {
                    x: brands.map((b) => b.x).sort(),
                    y: brands.map((b) => b.y).sort(),
                    type: plot_type,
                    marker: {
                        color: color
                    }
                }
            ]
        }

        const d = [
            {
                x: brands.map((b) => b.x).sort(),
                y: brands.map((b) => b.y).sort(),
                type: 'scatter',
                marker: {
                    color: color
                }
            }
        ]
        return (
            <>
                <Plot data={data} layout={layout} />
                <Plot data={d} layout={layout} />
            </>
        )
    }

    const layout = {
        xaxis: { title: xname },
        yaxis: { title: yname },
        plot_bgcolor: '#212529',
        paper_bgcolor: '#212529',
        font: {
            color: color
        },
        width: 1200,
        height: 800
    }
    return (
        <div style={{ textAlign: 'center', color: `${color}` }}>
            <h2>{title}</h2>
            <Container>{drawPlot()}</Container>
        </div>
    )
}

export default GeneralTaskZeroParameter
