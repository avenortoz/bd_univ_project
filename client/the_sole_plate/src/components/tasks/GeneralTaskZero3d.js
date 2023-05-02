
import { useEffect, useState } from 'react'
import { Container } from 'react-bootstrap'
import Plot from 'react-plotly.js'
import { serverHost } from '../../api.js'

const GeneralTaskZero3d = ({title, api, xname, yname, zname, plot_type="bar"}) => {
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
        const un = brands.map(b => b.z);
        const unique = [...new Set(un)];
        const d = unique.map(u => { 
            return {
                z: u,
                x: brands.filter(b => b.z === u).map((b) => b.x).sort(),
                y: brands.filter(b => b.z === u).map((b) => b.y).sort(),
                type: plot_type,
                name: u,
            }

        })
        return <Plot data={d} layout={layout}/>
    }

    const layout = {
        xaxis: { title: xname },
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

export default GeneralTaskZero3d  
