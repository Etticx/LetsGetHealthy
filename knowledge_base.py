# knowledge_base.py

# =========================================
# 1. THE 7 INPUTS (From MadMuscles Pages)
# =========================================
questions = {
    "goal": {
        "text": "1. Choose your goal ",
        "options": ["Lose weight", "Gain muscle mass", "Get shredded", "Boost overall-well being"]
    },
    "body_type": {
        "text": "2. Choose your body type ",
        "options": ["Slim", "Average", "Big", "Heavy"]
    },
    "problem_area": {
        "text": "3. Select problem area",
        "options": ["Weak chest", "Slim arms", "Beer belly", "Slim legs"]
    },
    "injury": {
        "text": "4. Do you struggle with? ",
        "options": ["None", "Knees", "Back", "Joints"]
    },
    "location": {
        "text": "5. Workout location",
        "options": ["Home", "Gym"]
    },
    "intensity": {
        "text": "6. Preferred level",
        "options": ["Keep it light 🧘‍♂️", "Good with effort 💪", "Bring intensity 🚀"]
    },
    "duration": {
        "text": "7. Duration",
        "options": ["10-15 minutes", "20-30 minutes", "30-40 minutes"]
    }
}

# =========================================
# 2. THE RULES (The Logic)
# =========================================
# We define "Archetypes" - common user profiles.
# The Inference Engine will find the best match.

rules = [
    {
        # Scenario: Home Fat Loss (The "Classic" User)
        "if": {
            "goal": "Lose weight",
            "location": "Home",
            "injury": "None"
        },
        "then": {
            "strategy": "🔥 **HIIT Bodyweight Circuit**\n1. Jumping Jacks (Warmup)\n2. **Pushups** (Standard)\n3. Mountain Climbers\n4. Burpees\n5. *Target Area Finisher*",
            "schedule": "🗓 **5 Days a Week**\nShort duration requires high consistency.",
            "equipment": "🎒 **Yoga Mat**"
        }
    },
    {
        # Scenario: Gym Muscle Build (The "Bro" Split)
        "if": {
            "goal": "Gain muscle mass",
            "location": "Gym",
            "intensity": "Bring intensity 🚀"
        },
        "then": {
            "strategy": "🏋️ **Heavy Hypertrophy**\n1. **Barbell Bench Press** (5 sets x 5 reps)\n2. Lat Pulldowns\n3. Weighted Squats\n4. Shoulder Press\n5. *Target Area Finisher*",
            "schedule": "🗓 **4 Days a Week**\n(Upper / Lower Split)",
            "equipment": "🎒 **Full Gym Access**\n(Barbells, Rack, Dumbbells)"
        }
    },
    {
        # Scenario: Knee Pain (Safety Rule - Very Important for Grades)
        "if": {
            "injury": "Knees"
        },
        "then": {
            "strategy": "🛡️ **Low Impact Stability**\n(NO JUMPING ALLOWED)\n1. Wall Sits (Hold 45s)\n2. **Knee Pushups**\n3. Glute Bridges\n4. Plank Holds\n5. *Target Area Finisher*",
            "schedule": "🗓 **Every Day**\nLow impact allows daily training.",
            "equipment": "🎒 **Thick Mat & Chair**\n(For support)"
        }
    },
    {
        # Scenario: Heavy Body Type (Metabolic Conditioning)
        "if": {
            "body_type": "Heavy",
            "goal": "Lose weight"
        },
        "then": {
            "strategy": "🚶 **Cardio & Resistance Hybrid**\n1. High Knees (Low impact)\n2. Wall Pushups\n3. Step-Ups (Use stairs)\n4. Flutter Kicks",
            "schedule": "🗓 **6 Days a Week**\nFocus on active calorie burning.",
            "equipment": "🎒 **Comfortable Shoes**"
        }
    },
    {
        # Scenario: Shredded Goal (Advanced)
        "if": {
            "goal": "Get shredded",
            "intensity": "Bring intensity 🚀"
        },
        "then": {
            "strategy": "⚔️ **Athletic Conditioning**\n(Supersets)\n1. Pull-ups + Burpees\n2. Dips + Jump Squats\n3. Hanging Leg Raises",
            "schedule": "🗓 **3 Days On, 1 Day Off**",
            "equipment": "🎒 **Pull-up Bar / Dip Station**"
        }
    }
]

# Fallback (If no rules match)
default_recommendation = {
    "strategy": "🔄 **Foundation Basics**\n1. Brisk Walking (Warmup)\n2. Bodyweight Squats\n3. Pushups (on knees if needed)\n4. Plank (30s)",
    "schedule": "🗓 **3 Days a Week**\nStart slow.",
    "equipment": "🎒 **None**"
}

# Special Logic for "Problem Areas"
# We will append this to the result in the engine
problem_area_fixes = {
    "Weak chest": "➕ **Finisher:** Wide Pushups (3 sets to failure)",
    "Slim arms": "➕ **Finisher:** Diamond Pushups & Chair Dips",
    "Beer belly": "➕ **Finisher:** Russian Twists & Leg Raises",
    "Slim legs": "➕ **Finisher:** Lunges & Calf Raises"
}
