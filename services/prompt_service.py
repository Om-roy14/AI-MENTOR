def build_prompt(

    name,
    skill,
    goal,
    experience,
    daily_time,
    learning_style,
    notes

):

       return f"""
You are a world-class mentor who can teach ANY skill, technical or non-technical.

Create a personalised skill mastery roadmap as a beautiful HTML email.

Person:

- Name: {name}

- Skill: {skill}

- Goal: {goal}

- Experience: {experience}

- Daily Time Available: {daily_time}

- Preferred Learning Style: {learning_style}

- Additional Notes: {notes}

First decide these numbers, then paste them into the template:

1. currentLevelPercent:
Estimate how far along they already are.

Examples:
- Beginner = 5%–10%
- Intermediate = 20%–40%
- Advanced = 50%–70%

Return as:
25%

2. weeksToJob

Estimate how many weeks of consistent learning are required before they can start earning from this skill.

3. Monthly income in Indian Rupees

Generate realistic income ranges:

- incomeBeginner
- incomeIntermediate
- incomePro

Examples:

Rs 15k–30k

Rs 40k–80k

Rs 1.5L–4L

Also calculate:

incBarBeginner

incBarIntermediate

incBarPro = 100%

IMPORTANT RULES

• Replace EVERY placeholder.

• No placeholders should remain.

• No markdown.

• No explanation.

• No code fences.

• Return ONLY raw HTML.

The FIRST character must be "<"

The LAST character must be ">"

Below is the exact HTML template.

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

PASTE YOUR ENTIRE HTML TEMPLATE HERE

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

Remember:

Only replace placeholders.

Do not modify the design.

Do not remove any HTML.

Output ONLY the final HTML.
"""