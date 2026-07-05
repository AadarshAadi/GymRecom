import { useState } from "react";

function F({ onSubmit }) {
  const [formData, setFormData] = useState({
    workcat: "Strength",
    days: 5,
    age: 22,
    duration: 60,
    exper: "Beginner",
    equipm: ["Dumbbell", "Machine"],
    injury: "None"
  });

  const hanchang = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const equichange = (e) => {
    const { value, checked } = e.target;
    const upequip = checked
      ? [...formData.equipm, value]
      : formData.equipm.filter((item) => item !== value);

    setFormData({ ...formData, equipm: upequip });
  };

  const submitfo = (e) => {
    e.preventDefault();
    onSubmit(formData);
  };

  return (
    <div className="form-card">
      <form onSubmit={submitfo}>
        <h2>Workout Details</h2>

        <label>Workout Goal</label>
        <select name="workcat" value={formData.workcat} onChange={hanchang}>
          <option>Strength</option>
          <option>Hypertrophy</option>
        </select>

        <label>Days Per Week</label>
        <input type="number" name="days" min="2" max="6" value={formData.days} onChange={hanchang} />

        <label>Workout Duration (minutes)</label>
        <input type="number" name="duration" value={formData.duration} onChange={hanchang} />

        <label>Age</label>
        <input type="number" name="age" value={formData.age} onChange={hanchang} />

        <label>Experience</label>
        <select name="exper" value={formData.exper} onChange={hanchang}>
          <option>Beginner</option>
          <option>Intermediate</option>
          <option>Advanced</option>
        </select>

        <label>Available Equipment</label>
        {["Dumbbell", "Machine", "Cable", "Body Only"].map((equipment) => (
          <div key={equipment}>
            <input
              type="checkbox"
              value={equipment}
              checked={formData.equipm.includes(equipment)}
              onChange={equichange}
            />
            {equipment}
          </div>
        ))}

        <label>Injury</label>
        <select name="injury" value={formData.injury} onChange={hanchang}>
          <option>None</option>
          <option>Knee Pain</option>
          <option>Lower Back Pain</option>
          <option>Shoulder Pain</option>
        </select>

        <button type="submit">Generate Workout</button>
      </form>
    </div>
  );
}

export default F;