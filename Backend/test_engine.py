from engine import generate_workout

result = generate_workout(
    workout_type="Hypertrophy",
    days=2,
    age=22,
    duration=60,
    experience_level="Intermediate",
    available_equipment=[
        "Dumbbell",
        "Machine",
        "Cable",
        "Body Only"
    ],
    injury="None"
)

print("=" * 50)
print("Split:", result["split"])
print("=" * 50)

for day in result["weekly_plan"]:
    print(day)