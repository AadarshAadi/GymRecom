/**
 * Displays the generated workout recommendation and exercise plan.
 *
 * Shows the recommended workout split, exercise count, age recommendation,
 * and a day-by-day workout schedule. If no workout result is provided,
 * the component renders nothing.
 */
function R({ result, onBack }) {
  if (!result) return null;
  return (
    <div className="results-card">
      <button className="back-button" onClick={onBack}>←</button>
      <div className="summary">
        <h2>Workout Recommendation</h2>
        <p><strong>Recommended Split:</strong> {result.split}</p>
        <p><strong>Exercises Per Day:</strong> {result.execount}</p>
        <p><strong>Age Recommendation:</strong> {result.age_note}</p>
      </div>
      <hr />
      <div className="days-grid">
        {Object.entries(result.gymplan).map(([day, plan]) => (
          <div key={day} className="day-card">
            <h3>{day}</h3>
            {plan === "Rest" ? (
              <p className="rest-day">💤 Rest Day</p>
            ) : (
              plan.map((exercise, index) => (
                <div key={index} className="exercise-card">
                  <h4>{exercise.Exercise}</h4>
                  <p>Muscle: {exercise.Muscle}</p>
                  <p>Equipment: {exercise.Equipment}</p>
                  <p>Level: {exercise.Level}</p>
                  <p>{exercise.Sets} Sets • {exercise.Reps} Reps</p>
                  <p>Rest: {exercise.Rest}</p>
                </div>
              ))
            )}
          </div>
        ))}
      </div>
    </div>
  );
}
export default R;