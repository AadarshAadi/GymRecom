/**
 * Main application component that manages workout generation
 * and displays either the form or the generated workout plan.
 */
function App() {
    const [result, setResult] = useState(null);

    /**
     * Sends the workout request to the backend API.
     *
     * @param {Object} formData - User workout preferences.
     */
    const genwork = async (formData) => {
        try {
            const response = await api.post(
                "/recommend",
                formData
            );
            setResult(response.data);
        }
        catch (error) {
            console.error(error);
        }
    };

    /**
     * Returns the user to the workout input form.
     */
    const goBack = () => {
        setResult(null);
    };

    return (
        <div className="app-background">
            <div className={`main-card ${result ? "results-mode" : "form-mode"}`}>
                <h1>GYMY</h1>
                {!result ? (
                    <F onSubmit={genwork} />
                ) : (
                    <R result={result} onBack={goBack} />
                )}
            </div>
        </div>
    );
}

export default App;