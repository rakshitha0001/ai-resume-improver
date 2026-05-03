from openai import OpenAI


import os
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def improve_resume(text, tone):
    if tone == "2":
        tone_instruction = "Make it highly impactful with strong achievements and powerful action verbs."
    else:
        tone_instruction = "Keep it formal, clean, and professional."

    prompt = f"""
You are an expert HR recruiter with 10+ years of experience.

TASK:
Improve the resume content below.

INPUT:
{text}

INSTRUCTIONS:
- Make it ATS-friendly
- Use strong action verbs
- Keep it concise and clear
- Highlight impact and results
- Avoid unnecessary words
- Use bullet-style phrasing if needed
- {tone_instruction}

OUTPUT:
Return only the improved version.
"""

    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful HR assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content



def main():
    print("=== AI Resume Improver ===\n")

    text = input("Enter your resume content:\n")

    print("\nChoose Tone:")
    print("1. Formal & Professional")
    print("2. Strong Impact (Recommended)")

    tone = input("Enter choice (1 or 2): ")

    print("\n Improving your resume...\n")

    result = improve_resume(text, tone)

    print(" Improved Version:\n")
    print(result)


if __name__ == "__main__":
    main()