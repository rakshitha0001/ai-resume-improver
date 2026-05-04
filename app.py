import requests

API_KEY = "YOUR_API_KEY"

def improve_resume(text, tone):
    if tone == "2":
        tone_instruction = "Make it highly impactful with strong achievements and action verbs."
    else:
        tone_instruction = "Keep it formal, clear, and professional."

    prompt = f"""
You are an expert HR recruiter.

Improve the resume content below:

{text}

Instructions:
- Make it ATS-friendly
- Use strong action verbs
- Keep it concise
- Highlight impact and results
- {tone_instruction}

Return only improved version.
"""

    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "openai/gpt-3.5-turbo",
            "messages": [{"role": "user", "content": prompt}]
        }
    )

    data = response.json()
    return data["choices"][0]["message"]["content"]


def main():
    print("--- AI Resume Improver ---\n")

    text = input("Enter your resume content:\n")

    print("\nChoose Tone:")
    print("1. Formal & Professional")
    print("2. Strong Impact")

    tone = input("Enter choice (1 or 2): ")

    print("\n Improving your resume...\n")

    result = improve_resume(text, tone)

    print(" Improved Version:\n")
    print(result)


if __name__ == "__main__":
    main()
