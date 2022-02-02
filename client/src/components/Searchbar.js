import { useState} from 'react'

function Searchbar(props) {
	const [url, setUrl] = useState('')
	  
	const handleFormSubmit = e => {
		e.preventDefault()
		props.setList(state => [{ url: url, short: 'shortened'}, ...state])
		setUrl('')
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