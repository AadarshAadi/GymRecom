import pandas as pd
from pathlib import Path
import time
from sqlalchemy import create_engine
""" Connection to MySQL database using SQLAlchemy and PyMySQL."""
engine = create_engine("mysql+pymysql://workoutuser:workoutpass@mysql:3306/workoutdb")
df = None
def datalload():
    """ Load exercise data from the MySQL database."""
    global df
    for _ in range(20):
        try:
            df = pd.read_sql("SELECT * FROM exercises",engine)
            print("Database loaded successfully.")
            return
        except Exception:
            print("Waiting for MySQL...")
            time.sleep(2)
    raise RuntimeError("Could not connect to MySQL.")

wosplit = {
    """Workout Split"""
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
    """Training Profiles"""
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

def gtrpo(workcat, exper):
    """ Training profile based on workout category and experience level."""
    return trpro[workcat][exper]

def agmsg(age):
    """ Age-based guidance for workout volume and recovery recommendations. """
    if age < 40:
        return "Normal workout volume is suitable."
    elif age <= 55:
        return "Use slightly reduced accessory volume and include a longer warm-up."
    else:
        return "Use lower volume, more recovery, and mobility work."
    
mgs = {
    """ Muscle groups assigned for each workout split."""
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
    """ Weekly workout schedule templates."""
    "Full Body": [
        "Full Body Day",
        "Rest",
        "Rest",
        "Full Body Day",
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

def ssplit(workcat, days):
    """ Get workout split based on category and training days."""
    return wosplit[workcat][days]

def excoun(wortime,workcat,exper):
    """ Calculate the recommended number of exercises per workout."""
    profile = gtrpo(workcat,exper)
    tottime = wortime * 60
    revtime = (profile["warmup"] * 60 + profile["cooldown"] * 60)
    availtime = tottime - revtime
    average_reps = sum(map(int,profile["rep_range"].split("-"))) / 2
    atime = (profile["sets"] *average_reps *profile["time_per_rep"])
    rtime = ((profile["sets"] - 1) *profile["rest"])
    ttime = profile["transition"]
    ssexec = (atime +rtime +ttime)
    execount = int( availtime // ssexec)
    return max(3, execount)

def ale(exper):
    """ Allowed exercise levels for the selected experience."""
    if exper == "Beginner":
        return ["Beginner"]
    elif exper == "Intermediate":
        return ["Beginner", "Intermediate"]
    elif exper == "Advanced":
        return ["Beginner", "Intermediate", "Expert"]

def inbo(injury):
    """ Injury-specific exercise restrictions."""
    iirul = {
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
    return iirul.get(injury, [])

def seda(daymusc,df,workcat,daynum,exper,equipm,injury,execount):
    """ Select exercises for a workout day based on user preferences."""
    sexecs = []
    profile = gtrpo(workcat,exper)
    bbwo = [
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
    jinbb = inbo(injury)
    bbwords = bbwo + jinbb
    alllevels = ale(exper)
    for muscle in daymusc:
        mex = df[df["BodyPart"] == muscle]
        mex = mex[mex["Level"].isin(alllevels)]
        mex = mex[mex["Equipment"].isin(equipm)]
        goodmatch = mex[~mex["Title"].str.lower().str.contains("|".join(bbwords),na=False)]
        if len(goodmatch) == 0:
            continue
        exeid = daynum % len(goodmatch)
        exercise = goodmatch.iloc[exeid]
        sexecs.append({"Exercise": exercise["Title"],"Muscle": muscle,"Equipment": exercise["Equipment"],"Level": exercise["Level"],"Sets": profile["sets"],"Reps": profile["rep_range"],"Rest": f'{profile["rest"]} sec'})
    exindex = 0
    while len(sexecs) < execount:
        muscle = daymusc[exindex % len(daymusc)]
        mex = df[df["BodyPart"] == muscle]
        mex = mex[mex["Level"].isin(alllevels)]
        mex = mex[mex["Equipment"].isin(equipm)]
        goodmatch = mex[~mex["Title"].str.lower().str.contains("|".join(bbwords),na=False)]
        if len(goodmatch) > 0:
            exeid = (daynum + exindex + 1) % len(goodmatch)
            exercise = goodmatch.iloc[exeid]
            exename = exercise["Title"]
            ase = False
            for selected in sexecs:
                if selected["Exercise"] == exename:
                    ase = True
            if not ase:
                sexecs.append({"Exercise": exercise["Title"],"Muscle": muscle,"Equipment": exercise["Equipment"],"Level": exercise["Level"],"Sets": profile["sets"],"Reps": profile["rep_range"],"Rest": f'{profile["rest"]} sec'})
        exindex += 1
        if exindex > 50:
            break
    return sexecs[:execount]

def bwe(split,semuscles,df,workcat,exper,equipm,injury,execount):
    """ Build the complete weekly workout plan."""
    gymplan = {}
    template = wte[split]
    for daynum, day_type in enumerate(template, start=1):
        if day_type == "Rest":
            gymplan[f"Day {daynum}"] = "Rest"
        else:
            muscles = semuscles[day_type]
            exercises = seda(muscles,df,workcat,daynum,exper,equipm,injury,execount)
            gymplan[f"Day {daynum} - {day_type}"] = exercises
    return gymplan

def genwork(workcat,days,age,duration,exper,equipm,injury):
    """ Generate a personalized workout plan."""
    split = ssplit(workcat, days)
    execount = excoun(duration,workcat,exper)
    age_note = agmsg(age)
    semuscles = mgs[split]
    gymplan = bwe(split,semuscles,df,workcat,exper,equipm,injury,execount)
    return {"split": split,"execount": execount,"age_note": age_note,"gymplan": gymplan}