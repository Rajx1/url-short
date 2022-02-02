import { useState} from 'react'
import { axios_helper as axios } from '../utils/axios_helper'

function Searchbar(props) {
	const [url, setUrl] = useState('')
	
	async function getShortUrl() {
		try {
			let { data } = await axios.post('/create', { long_url: url })
			props.setList(state => [
				{
					url: url,
					generated_url: data.url,
				},
				...state
			])

			setUrl('')
		} catch(e) {
				console.log(e.message)
			}
		}

	const handleFormSubmit = e => {
		e.preventDefault()
		getShortUrl()
	}

	const handleInput = e => {
		setUrl(e.target.value)
	}
	  
	return (
		<form className="w3-row" onSubmit={handleFormSubmit}>
			<div className="w3-panel w3-twothird">
				<input className="w3-input" type="url" name="url" value={url} onChange={handleInput} required />
			</div>
			<div className="w3-panel w3-third">
				<input className="w3-btn w3-round-large w3-amber" type="submit" value="Go"></input>
			</div>
		</form>
	)
}

export default Searchbar