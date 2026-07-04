import pandas as pd
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
DATASET_PATH = BASE_DIR / "cleaneddataset.csv"

df = pd.read_csv(DATASET_PATH)

wosplit = {
    "Hypertrophy": {
        2: "Full Body",
        3: "Push Pull Legs",
        4: "Upper Lower",
        5: "Bro Split",
        6: "Push Pull Legs x2"
    },
    "Strength": {
        2: "Full Body Strength",
        3: "Full Body Strength*3",
        4: "Upper Lower Strength",
        5: "Strength + Accessories",
        6: "Strength PPL"
    }
}
trpro = {

    "Hypertrophy": {

        "Beginner": {
            "sets": 3,
            "rep_range": "10-12",
            "rest": 75,
            "time_per_rep": 4,
            "warmup": 5,
            "cooldown": 5,
            "transition": 30
        },

        "Intermediate": {
            "sets": 4,
            "rep_range": "8-12",
            "rest": 75,
            "time_per_rep": 4,
            "warmup": 7,
            "cooldown": 5,
            "transition": 30
        },

        "Advanced": {
            "sets": 4,
            "rep_range": "6-12",
            "rest": 90,
            "time_per_rep": 4,
            "warmup": 10,
            "cooldown": 5,
            "transition": 45
        }
    },


    "Strength": {

        "Beginner": {
            "sets": 4,
            "rep_range": "5-6",
            "rest": 180,
            "time_per_rep": 5,
            "warmup": 8,
            "cooldown": 5,
            "transition": 45
        },

        "Intermediate": {
            "sets": 5,
            "rep_range": "3-5",
            "rest": 210,
            "time_per_rep": 5,
            "warmup": 10,
            "cooldown": 5,
            "transition": 60
        },

        "Advanced": {
            "sets": 5,
            "rep_range": "1-5",
            "rest": 300,
            "time_per_rep": 5,
            "warmup": 12,
            "cooldown": 5,
            "transition": 60
        }
    }

}

def gtrpo(workout_type, experience_level):
    return trpro[workout_type][experience_level]

def agmsg(age):
    if age < 40:
        return "Normal workout volume is suitable."
    elif age <= 55:
        return "Use slightly reduced accessory volume and include a longer warm-up."
    else:
        return "Use lower volume, more recovery, and mobility work."

mgs = {
    "Full Body": {
        "Full Body Day": [
            "Chest",
            "Lats",
            "Shoulders",
            "Quadriceps",
            "Hamstrings",
            "Abdominals"
        ]
    },

    "Push Pull Legs": {
        "Push Day": [
            "Chest",
            "Shoulders",
            "Triceps"
        ],
        "Pull Day": [
            "Lats",
            "Middle Back",
            "Biceps"
        ],
        "Leg Day": [
            "Quadriceps",
            "Hamstrings",
            "Glutes",
            "Calves",
            "Abdominals"
        ]
    },

    "Upper Lower": {
        "Upper Day": [
            "Chest",
            "Lats",
            "Shoulders",
            "Biceps",
            "Triceps"
        ],
        "Lower Day": [
            "Quadriceps",
            "Hamstrings",
            "Glutes",
            "Calves",
            "Abdominals"
        ]
    },

    "Bro Split": {
        "Chest Day": [
            "Chest",
            "Triceps"
        ],
        "Back Day": [
            "Lats",
            "Middle Back",
            "Biceps"
        ],
        "Shoulder Day": [
            "Shoulders",
            "Traps"
        ],
        "Leg Day": [
            "Quadriceps",
            "Hamstrings",
            "Glutes",
            "Calves"
        ],
        "Arm Day": [
            "Biceps",
            "Triceps",
            "Forearms"
        ]
    },

    "Push Pull Legs x2": {
        "Push Day": [
            "Chest",
            "Shoulders",
            "Triceps"
        ],
        "Pull Day": [
            "Lats",
            "Middle Back",
            "Biceps"
        ],
        "Leg Day": [
            "Quadriceps",
            "Hamstrings",
            "Glutes",
            "Calves",
            "Abdominals"
        ]
    },
    "Full Body Strength*3": {
        "Full Body Day": [
            "Chest",
            "Lats",
            "Quadriceps",
            "Hamstrings",
            "Shoulders"
        ]
    },

    "Full Body Strength": {
        "Full Body Day": [
            "Chest",
            "Lats",
            "Quadriceps",
            "Hamstrings",
            "Shoulders"
        ]
    },

    "Upper Lower Strength": {
        "Upper Day": [
            "Chest",
            "Lats",
            "Shoulders",
            "Biceps",
            "Triceps"
        ],
        "Lower Day": [
            "Quadriceps",
            "Hamstrings",
            "Glutes",
            "Calves",
            "Abdominals"
        ]
    },

    "Strength + Accessories": {
        "Upper Strength Day": [
            "Chest",
            "Lats",
            "Shoulders",
            "Triceps"
        ],
        "Lower Strength Day": [
            "Quadriceps",
            "Hamstrings",
            "Glutes",
            "Calves"
        ],
        "Accessory Day": [
            "Biceps",
            "Triceps",
            "Abdominals",
            "Forearms"
        ]
    },

    "Strength PPL": {
        "Push Day": [
            "Chest",
            "Shoulders",
            "Triceps"
        ],
        "Pull Day": [
            "Lats",
            "Middle Back",
            "Biceps"
        ],
        "Leg Day": [
            "Quadriceps",
            "Hamstrings",
            "Glutes",
            "Calves",
            "Abdominals"
        ]
    }
}

wte = {
    "Full Body": [
        "Full Body Day",
        "Rest",
        "Full Body Day",
        "Rest",
        "Rest",
        "Rest",
        "Rest"
    ],

    "Push Pull Legs": [
        "Push Day",
        "Pull Day",
        "Leg Day",
        "Rest",
        "Rest",
        "Rest",
        "Rest"
    ],

    "Upper Lower": [
        "Upper Day",
        "Lower Day",
        "Rest",
        "Upper Day",
        "Lower Day",
        "Rest",
        "Rest"
    ],

    "Bro Split": [
        "Chest Day",
        "Back Day",
        "Shoulder Day",
        "Leg Day",
        "Arm Day",
        "Rest",
        "Rest"
    ],

    "Push Pull Legs x2": [
        "Push Day",
        "Pull Day",
        "Leg Day",
        "Push Day",
        "Pull Day",
        "Leg Day",
        "Rest"
    ],
    "Full Body Strength*3": [
        "Full Body Day",
        "Rest",
        "Full Body Day",
        "Rest",
        "Full Body Day",
        "Rest",
        "Rest"
    ],

    "Full Body Strength": [
        "Full Body Day",
        "Rest",
        "Rest",
        "Full Body Day",
        "Rest",
        "Rest",
        "Rest"
    ],

    "Upper Lower Strength": [
        "Upper Day",
        "Lower Day",
        "Rest",
        "Upper Day",
        "Lower Day",
        "Rest",
        "Rest"
    ],

    "Strength + Accessories": [
        "Upper Strength Day",
        "Lower Strength Day",
        "Rest",
        "Upper Strength Day",
        "Lower Strength Day",
        "Accessory Day",
        "Rest"
    ],

    "Strength PPL": [
        "Push Day",
        "Pull Day",
        "Leg Day",
        "Push Day",
        "Pull Day",
        "Leg Day",
        "Rest"
    ]
}

def ssplit(workout_type, days):
    return wosplit[workout_type][days]


def excoun(
        workout_duration,
        workout_type,
        experience_level
):

    profile = gtrpo(
        workout_type,
        experience_level
    )

    total_seconds = workout_duration * 60

    reserved_seconds = (
        profile["warmup"] * 60 +
        profile["cooldown"] * 60
    )

    available_seconds = total_seconds - reserved_seconds

    average_reps = sum(
        map(
            int,
            profile["rep_range"].split("-")
        )
    ) / 2

    active_time = (
        profile["sets"] *
        average_reps *
        profile["time_per_rep"]
    )

    resting_time = (
        (profile["sets"] - 1) *
        profile["rest"]
    )

    transition_time = profile["transition"]

    seconds_per_exercise = (
        active_time +
        resting_time +
        transition_time
    )

    exercise_count = int(
        available_seconds //
        seconds_per_exercise
    )

    return max(3, exercise_count)

def get_allowed_levels(experience_level):
    if experience_level == "Beginner":
        return ["Beginner"]
    elif experience_level == "Intermediate":
        return ["Beginner", "Intermediate"]
    elif experience_level == "Advanced":
        return ["Beginner", "Intermediate", "Expert"]


def get_injury_blocked_words(injury):
    injury_rules = {
        "None": [],
        "Knee Pain": [
            "jump",
            "lunge",
            "squat",
            "step-up",
            "leg press"
        ],
        "Lower Back Pain": [
            "deadlift",
            "good morning",
            "stiff-legged",
            "bent-over",
            "hyperextension"
        ],
        "Shoulder Pain": [
            "overhead",
            "shoulder press",
            "behind-the-neck",
            "upright row"
        ]
    }

    return injury_rules.get(injury, [])

def select_exercises_from_dataset(
    day_muscles,
    df,
    workout_type,
    day_number,
    experience_level,
    available_equipment,
    injury,
    exercise_count
):
    selected_exercises = []
    profile = gtrpo(
    workout_type,
    experience_level
)

    base_blocked_words = [
        "clean",
        "snatch",
        "jerk",
        "power",
        "blocks",
        "behind-the-neck",
        "push-press",
        "kick-back",
        "kickback",
        "jump",
        "high knees",
        "quad touch",
        "holman",
        "floor press",
        "fyr2",
        "chains",
        "single-arm push-up",
        "pistol",
        "hip adduction",
        "neck bridge",
        "judo flip"
        "Push-Up"
    ]

    injury_blocked_words = get_injury_blocked_words(injury)
    blocked_words = base_blocked_words + injury_blocked_words

    allowed_levels = get_allowed_levels(experience_level)

    for muscle in day_muscles:
        matching_exercises = df[df["BodyPart"] == muscle]

        matching_exercises = matching_exercises[
            matching_exercises["Level"].isin(allowed_levels)
        ]

        matching_exercises = matching_exercises[
            matching_exercises["Equipment"].isin(available_equipment)
        ]

        safe_matches = matching_exercises[
            ~matching_exercises["Title"].str.lower().str.contains(
                "|".join(blocked_words),
                na=False
            )
        ]

        if len(safe_matches) == 0:
            continue

        exercise_index = day_number % len(safe_matches)
        exercise = safe_matches.iloc[exercise_index]

        selected_exercises.append({
            "Exercise": exercise["Title"],
            "Muscle": muscle,
            "Equipment": exercise["Equipment"],
            "Level": exercise["Level"],
            "Sets": profile["sets"],
            "Reps": profile["rep_range"],
            "Rest": f'{profile["rest"]} sec'
        })

    extra_index = 0

    while len(selected_exercises) < exercise_count:
        muscle = day_muscles[extra_index % len(day_muscles)]

        matching_exercises = df[df["BodyPart"] == muscle]

        matching_exercises = matching_exercises[
            matching_exercises["Level"].isin(allowed_levels)
        ]

        matching_exercises = matching_exercises[
            matching_exercises["Equipment"].isin(available_equipment)
        ]

        safe_matches = matching_exercises[
            ~matching_exercises["Title"].str.lower().str.contains(
                "|".join(blocked_words),
                na=False
            )
        ]

        if len(safe_matches) > 0:
            exercise_index = (day_number + extra_index + 1) % len(safe_matches)
            exercise = safe_matches.iloc[exercise_index]

            exercise_name = exercise["Title"]

            already_selected = False
            for selected in selected_exercises:
                if selected["Exercise"] == exercise_name:
                    already_selected = True

            if not already_selected:
                selected_exercises.append({
                    "Exercise": exercise["Title"],
                    "Muscle": muscle,
                    "Equipment": exercise["Equipment"],
                    "Level": exercise["Level"],
                    "Sets": profile["sets"],
                    "Reps": profile["rep_range"],
                    "Rest": f'{profile["rest"]} sec'
                })

        extra_index += 1

        if extra_index > 50:
            break

    return selected_exercises[:exercise_count]

def build_weekly_plan_from_dataset(
    split,
    selected_muscle_groups,
    df,
    workout_type,
    experience_level,
    available_equipment,
    injury,
    exercise_count
):
    weekly_plan = {}
    template = wte[split]

    for day_number, day_type in enumerate(template, start=1):
        if day_type == "Rest":
            weekly_plan[f"Day {day_number}"] = "Rest"
        else:
            muscles = selected_muscle_groups[day_type]

            exercises = select_exercises_from_dataset(
                muscles,
                df,
                workout_type,
                day_number,
                experience_level,
                available_equipment,
                injury,
                exercise_count
            )

            weekly_plan[f"Day {day_number} - {day_type}"] = exercises

    return weekly_plan

def generate_workout(
    workout_type,
    days,
    age,
    duration,
    experience_level,
    available_equipment,
    injury
):

    split = ssplit(workout_type, days)

    exercise_count = excoun(
        duration,
        workout_type,
        experience_level
    )

    age_note = agmsg(age)

    selected_muscle_groups = mgs[split]

    weekly_plan = build_weekly_plan_from_dataset(
        split,
        selected_muscle_groups,
        df,
        workout_type,
        experience_level,
        available_equipment,
        injury,
        exercise_count
    )

    return {
        "split": split,
        "exercise_count": exercise_count,
        "age_note": age_note,
        "weekly_plan": weekly_plan
    }