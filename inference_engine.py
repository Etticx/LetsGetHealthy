# inference_engine.py
from knowledge_base import rules, default_recommendation, problem_area_fixes

def run_inference(user_inputs):
    """
    1. Finds the best matching rule.
    2. Modifies the result based on 'Problem Area'.
    """
    
    best_match = None
    highest_match_count = 0

    # --- STEP 1: Find the Main Workout ---
    for rule in rules:
        conditions = rule["if"]
        match = True
        
        # Check if user inputs match the rule conditions
        for key, value in conditions.items():
            if user_inputs.get(key) != value:
                match = False
                break
        
        if match:
            # Score logic: More specific rules override general ones
            if len(conditions) > highest_match_count:
                highest_match_count = len(conditions)
                best_match = rule["then"].copy() # Copy so we don't modify the original

    # Use default if no rule matched
    final_result = best_match if best_match else default_recommendation.copy()

    # --- STEP 2: Apply the "Problem Area" Modifier ---
    # This replaces the text "*Target Area Finisher*" with the specific exercise
    user_problem = user_inputs.get("problem_area")
    
    if user_problem in problem_area_fixes:
        fix_text = problem_area_fixes[user_problem]
        
        # We append the finisher to the strategy string
        final_result["strategy"] += f"\n\n{fix_text}"

    return final_result