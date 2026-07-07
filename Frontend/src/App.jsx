import { useState } from "react";
import F from "./components/F";
import R from "./components/R";
import I from "./components/I";
import api from "./services/api";
import "./styles/App.css";
function App() {
    const [routines, setRoutines] = useState([]);
    const [selectedRoutine, setSelectedRoutine] = useState(null);
    const genwork = async (formData) => {
        try {
            const response = await api.post(
                "/recommend",
                formData
            );
            setRoutines(response.data);
            setSelectedRoutine(null);
        }
        catch (error) {
            console.error(error);
        }
    };
    /**
     * Returns the user to the workout input form.
     */
    const goBack = () => {
    setSelectedRoutine(null);
    };

    return (
        <div className="app-background">
            <div
  className={`main-card ${
    routines.length === 0 ? "form-mode" : "results-mode"
  }`}
>
                <h1>GYMY</h1>
                {routines.length === 0 ? (
  <F onSubmit={genwork} />
) : selectedRoutine ? (
  <R
    result={selectedRoutine}
    onBack={goBack}
  />
) : (
<I
  routines={routines}
  onSelect={setSelectedRoutine}
  onBack={() => {
    setRoutines([]);
    setSelectedRoutine(null);
  }}
/>
)}
            </div>
        </div>
    );
}

export default App;