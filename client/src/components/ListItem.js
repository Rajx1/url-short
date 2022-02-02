function ListItem(props) {

	async function copyToClipboard(text) {
		if ('clipboard' in navigator)
			await navigator.clipboard.writeText(text)
	}

	function handleClick() {
		copyToClipboard(props.data.short)
	}

	return(
		<div className="w3-panel w3-round-large w3-blue w3-row">
			<h3 className="w3-third">{props.data.url}</h3>
			<h3 className="w3-third anchor">
				<a href={props.data.url}>{props.data.short}</a>
			</h3>
			<h3 className="w3-third w3-hover-text-blue-grey copy" onClick={handleClick}><i className="bi bi-clipboard"></i></h3>
		</div>
	)
}

export default ListItem