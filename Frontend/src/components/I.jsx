/**
 * Displays 3 workout choices generated based on the user's input from the form.
 * User can select one of the routines to view its detailed workout plan.
 */
function I({ routines, onSelect, onBack }) {
  if (!routines || routines.length === 0) return null;
  return (
    <div className="results-card">
        <button className="back-button" onClick={onBack}>
  ←
</button>
      <div className="summary">
        <h2>Select a Workout Routine</h2>
        <p>Choose one of the generated workout routines.</p>
      </div>
      <hr />
      <div className="days-grid">
        {routines.map((routine, index) => (
          <div key={index} className="day-card">
            <h3>Routine {index + 1}</h3>
            <p>
              <strong>Recommended Split:</strong> {routine.split}
            </p>
            <p>
              <strong>Exercises Per Day:</strong> {routine.execount}
            </p>
            <p>
              <strong>Age Recommendation:</strong> {routine.age_note}
            </p>
            <button onClick={() => onSelect(routine)}>View Routine</button>
          </div>
        ))}
      </div>
    </div>
  );
}
export default I;