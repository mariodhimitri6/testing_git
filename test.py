from fpdf import FPDF

# Create a PDF document
pdf = FPDF(hi)
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

pdf.set_font("Helvetica", 'B', 16)  # Using Helvetica for better Unicode support
pdf.cell(200, 10, txt="High-Volume Cutting Plan with Recall Day (4-Day Split)", ln=True, align="C")
pdf.ln(10)
#daje
def clean_text(text):
    return text.replace("–", "-").replace("’", "'")  # Replace en dash with regular dash and fix apostrophe
print("Bugfix 2")
print("fix")
pdf.set_font("Helvetica", size=12)
pdf.cell(200, 10, txt="Weekly Workout Structure:", ln=True)
pdf.ln(5)
weekly_structure = """
| Day       | Focus                                |
|-----------|--------------------------------------|
| Monday    | Chest & Triceps (High Volume)       |
| Wednesday | Back & Biceps (High Volume)         |
| Friday    | Legs & Recall (Chest, Back, Arms)  |
| Saturday  | Shoulders & Abs                     |
"""
pdf.multi_cell(0, 10, clean_text(weekly_structure))
pdf.ln(10)

# Day 1 - Chest & Triceps
pdf.set_font("Helvetica", 'B', 14)
pdf.cell(200, 10, txt="Day 1 - Chest & Triceps", ln=True)
pdf.set_font("Helvetica", size=12)
chest_triceps = """
1. Barbell Bench Press - 4 sets (15-12-10-8)
2. Incline Dumbbell Press - 4 sets (15-12-10-8)
3. Machine Chest Press - 3 sets (12-10-10)
4. Cable or Pec Deck Flyes - 3 sets (15-12-12)
5. Dips - 3 sets (10-10-8)
6. Skullcrushers - 3 sets (12-10-8)
7. Triceps Pushdowns - 3 sets (15-12-10)
8. Pushups to failure - 2 sets
"""
pdf.multi_cell(0, 10, clean_text(chest_triceps))
pdf.ln(10)

# Day 2 - Back & Biceps
pdf.set_font("Helvetica", 'B', 14)
pdf.cell(200, 10, txt="Day 2 - Back & Biceps", ln=True)
pdf.set_font("Helvetica", size=12)
back_biceps = """
1. Pull-Ups - 4 sets (10-10-8-8)
2. Barbell Rows - 4 sets (15-12-10-8)
3. Lat Pulldowns - 3 sets (12-10-10)
4. Seated Cable Rows - 3 sets (12-10-10)
5. Face Pulls - 3 sets (15-12-12)
6. Barbell Curls - 3 sets (15-12-10)
7. Incline DB or Preacher Curls - 3 sets (12-10-8)
8. Hammer Curls superset Band Curls - 2 sets
"""
pdf.multi_cell(0, 10, clean_text(back_biceps))
pdf.ln(10)

# Day 3 - Legs & Recall (Chest, Back, Arms)
pdf.set_font("Helvetica", 'B', 14)
pdf.cell(200, 10, txt="Day 3 - Legs & Recall (Chest, Back, Arms)", ln=True)
pdf.set_font("Helvetica", size=12)
legs_recall = """
2. Walking Lunges (DB or BB) - 3 sets (12-12-10 per leg)
5. Bulgarian Split Squats (Bodyweight or DBs) - 3 sets (12-12-10 per leg)
6. Standing Calf Raises - 4 sets (15-15-12-12)
7. Seated Calf Raises - 3 sets (15-12-12)

**Recall (Chest, Back, Arms):**
- Chest:
- Back:
  1. Lat Pulldowns - 3 sets (12-10-10)
- Arms:
"""
pdf.multi_cell(0, 10, clean_text(legs_recall))
pdf.ln(10)


pdf.multi_cell(0, 10, clean_text(shoulders_abs))
pdf.ln(10)

diet_plan = """


**Meal 3 (Lunch):**
- Grilled chicken breast (6 oz)
- 1 cup of quinoa or brown rice
- Steamed veggies (broccoli, spinach, etc.)
- Olive oil dressing (for the salad or veggies)

**Meal 4 (Snack):**
- Handful of almonds or walnuts
- 1 apple or banana
- 1 serving of casein protein (if you have it)

**Meal 5 (Dinner):**
- Grilled salmon or lean beef (6 oz)
- Roasted sweet potatoes or steamed asparagus
- Mixed green salad (with olive oil or balsamic vinegar dressing)

"""
pdf.multi_cell(0, 10, clean_text(diet_plan))
pdf.ln(10)
"""
Cardio is essential during a cutting phase to help burn additional calories. Here’s a recommended weekly cardio plan:

**Frequency:** 3-5 cardio sessions per week.

**1. Steady-State Cardio:**
   - **Duration:** 30-45 minutes per session.
   - **Intensity:** Moderate (60-70% of max heart rate).
   - **Example:** Walking, cycling, or light jogging.

**2. HIIT (High-Intensity Interval Training):**
   - **Duration:** 15-25 minutes per session.
   - **Intensity:** High-intensity sprints or intervals.
   - **Example:** Sprints, jump rope, burpees.

**Sample Weekly Cardio Plan:**
- **Tuesday:** Rest or light walking.
- **Wednesday:** 20-30 minutes steady-state cardio or 15-20 minutes HIIT.
- **Thursday:** Rest or active recovery.
- **Friday:** 20-30 minutes steady-state cardio.
- **Saturday:** 20-25 minutes HIIT.
- **Sunday:** Rest or active recovery.
"""
pdf.multi_cell(0, 10, clean_text(cardio_plan))
pdf.ln(10)

# Save the PDF
pdf_output_path = "High_Volume_Cutting_Plan_4Day_with_Diet_and_Cardio.pdf"
pdf.output(pdf_output_path)

pdf_output_path
