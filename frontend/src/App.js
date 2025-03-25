import './App.css';
import {Routes, Route} from 'react-router-dom';
import Home from './Componentes/Home';
import Create from './Componentes/Create';
import NavBar from './Componentes/NavBar';

function App() {
  const myWidth = 220
  return (
    <div className="App">
      <NavBar 
            drawerWidth={myWidth}
            content ={
              <Routes>
                <Route path="" element={<Home />} />
                <Route path="/create" element={<Create />} />
              </Routes>
            }    
      /> 
    </div>
  );
}

export default App;
