import { useState } from 'react';
import Searchbar from './components/Searchbar';
import ListItem from './components/ListItem';
import './App.css';

function App() {
	const [list, setList] = useState('')

	return (
   	<div>
      	<header className="w3-center w3-padding-48">
    			<h2 className="w3-text-dark-grey">URL Short</h2>
      	</header>
      	<main className="w3-content w3-container">
        		<Searchbar setList={setList}/>
        		<div className="w3-padding-48"></div>
          		{ list &&
            		<div className="w3-container">
              			{list.map((e, i)=> <ListItem key={`url${i}`} data={e} />)}
            		</div>
          		}
      	</main>
    	</div>
  )
}

export default App;
