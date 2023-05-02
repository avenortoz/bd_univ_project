
import { useEffect, useState } from 'react'
import { Container } from 'react-bootstrap'
import Plot from 'react-plotly.js'
import { serverHost } from '../../api.js'

const GenderMonthSale = ({title, api, xname, yname, zname}) => {
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
                            y: b[yname],
                            z: b[zname]
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
                x: 'female',
                y: brands.filter(b => b.x === 'female').map((b) => b.y),
                z: brands.filter(b => b.x === 'female').map((b) => b.z),
                type: 'scatter',
                name: 'female',
                marker: {
                    color: '#B48EAD'
                }
            },
            {
                x: 'male',
                y: brands.filter(b => b.x === 'male').map((b) => b.y),
                z: brands.filter(b => b.x === 'male').map((b) => b.z),
                type: 'scatter',
                name: 'male',
                marker: {
                    color: '#6b8e23'
                }
            }
        ]
            console.log(brands)

        return <Plot data={data} layout={layout}/>
    }

    const layout = {
        xaxis: { title: zname },
        yaxis: { title: yname },
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

export default GenderMonthSale  
