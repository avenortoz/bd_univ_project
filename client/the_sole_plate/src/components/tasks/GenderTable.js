import { useEffect, useState } from 'react'
import { Container, Table } from 'react-bootstrap'
import { serverHost } from '../../api.js'
const GenderTable = ({ title, api }) => {
    const [data, setData] = useState([])
    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await fetch(`${serverHost}/${api}`)
                const tdata = await response.json()
                setData(tdata)
            } catch (error) {
                console.error(error)
            }
        }

        fetchData()
    }, [])
    return (
        <div className='container mt-5'>
            <h3>{title}</h3>
            <Table variant='dark'>
                <thead>
                    <tr>
                        <th>#</th>
                        <th>Brand</th>
                        <th>Category</th>
                        <th>Create Date</th>
                        <th>Price</th>
                        <th>Sex</th>
                        <th>Update Date</th>
                    </tr>
                </thead>
                <tbody>
                    {data.slice(0, 200).map((item, index) => (
                        <tr key={index}>
                            <td>{index + 1}</td>
                            <td>{item.Brand}</td>
                            <td>{item.Category}</td>
                            <td>{item.CreateDate}</td>
                            <td>{item.Price}</td>
                            <td>{item.Sex}</td>
                            <td>{item.UpdateDate}</td>
                        </tr>
                    ))}
                </tbody>
            </Table>
        </div>
    )
}
export default GenderTable
