import { useEffect, useState, useRef } from 'react'
import { Container, Form } from 'react-bootstrap'
import Plot from 'react-plotly.js'
import { serverHost } from '../../api.js'
import './options.css'

const colors = ['#BE6069', '#5D80AB', '#B38DAC', '#6b8e23', '#ff9933']

const GeneralTaskOneParameter = ({
    title,
    api,
    param1,
    param1DefaultValue,
    xname,
    yname,
    plot_type = 'bar'
}) => {
    const color = colors[Math.floor(Math.random() * colors.length)]

    const [state1, setState1] = useState(param1DefaultValue)
    const [brands, setData] = useState([])
    const formRef = useRef(null)
    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await fetch(`${serverHost}/${api}/${state1}`)
                const tmp_data = await response.json()
                setData(
                    tmp_data.map((b) => {
                        return {
                            y: b[yname],
                            x: b[xname]
                        }
                    })
                )
            } catch (error) {
                console.error(error)
            }
        }

        fetchData()
    }, [state1])

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
                    x: brands.map((b) => b.x),
                    y: brands.map((b) => b.y),
                    type: plot_type,
                    marker: {
                        color: color
                    }
                }
            ]
        }

        const d = [
            {
                x: brands.map((b) => b.x),
                y: brands.map((b) => b.y),
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
        title: `${state1}`,
        xaxis: { title: xname },
        yaxis: { title: yname },
        plot_bgcolor: '#212529',
        paper_bgcolor: '#212529',
        font: {
            color: color
        },
        width: 1100,
        height: 800
    }

    const submit = (e) => {
        e.preventDefault()
        const form = formRef.current
        const tstate1 = parseInt(form.state1.value)
        setState1(tstate1)
    }
    return (
        <div className='task'>
            <div className='task__option'>
                <Form ref={formRef} onSubmit={(e) => submit(e)}>
                    <Form.Group className='ms-3 me-3'>
                        <Form.Label>{param1}:</Form.Label>
                        <Form.Control
                            type='text'
                            name='state1'
                            defaultValue={state1}
                            placeholder='Enter text'
                        />
                    </Form.Group>
                    <div style={{ textAlign: 'center', marginTop: '50px' }}>
                        <button type='submit'>Submit</button>
                    </div>
                </Form>
            </div>
            <div style={{ textAlign: 'center', color: `${color}` }}>
                <h2>{title}</h2>
                <Container>{drawPlot()}</Container>
            </div>
        </div>
    )
}

export default GeneralTaskOneParameter
