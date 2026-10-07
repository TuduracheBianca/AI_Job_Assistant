def generate_cover_letter(profile_format, job_description):
    from google import genai
    import time
    from dotenv import load_dotenv
    import os
    load_dotenv()
    gemini_key = os.getenv("GEMINI_API_KEY")
    if not gemini_key:
        raise ValueError("GEMINI_API_KEY not set")
    max_tries = 4
    waiting_time = 2
    for i in range(max_tries):
        try:
            print(f"Trimit mesajul către Gemini, te rog așteaptă incercarea {i + 1}/{max_tries}")
            client = genai.Client(api_key=gemini_key)
            answer = client.models.generate_content(
                model='gemini-3.8-flash',
                contents=
                f"""
                Salut Gemini, acționează ca un expert în carieră.
                Te rog să îmi scrii un Cover Letter profesionist pentru acest job, bazat pe experiența mea.

                REGULI STRICTE DE OUTPUT:
                1. Generează EXCLUSIV scrisoarea de intenție, fără alte comentarii sau explicații.
                2. Nu include text conversațional adresat mie (fără "Sigur, iată scrisoarea"). Începe direct cu formula de adresare.
                3. Fără formatare Markdown (fără steluțe, bold sau linii). Folosește doar text simplu.
                4. Redactează scrisoarea în aceeași limbă în care este scrisă descrierea jobului.
                5. Fii concis: scrisoarea trebuie să aibă maxim 3-4 paragrafe de impact.
                6. Extrage numele companiei din descrierea jobului. Dacă lipsește, folosește "Hiring Team". Niciodată nu folosi placeholdere (precum [Nume Companie]).
                7. Înlocuiește datele necesare (nume, contact) exclusiv cu cele din profilul meu.

                Păstrează un ton profesional și pune-mi în valoare proiectele astfel încât să demonstrezi cum rezolv nevoile specifice din job.

                AICI ESTE DESCRIEREA JOBULUI:
                {job_description}

                AICI ESTE PROFILUL MEU:
                {profile_format}   
            """
            )
            print("\n--- Răspunsul AI-ului ---")
            return answer.text
        except Exception as e:
            print(f"Eroare întâmpinată: {e}")
            print(f"Server aglomerat. Aștept {waiting_time} secunde...")
            time.sleep(waiting_time)
            waiting_time *= 2
    else:
        print(f"Eroare întâmpinată de mai multe ori. Te rog să încerci din nou mai târziu.")
        exit()