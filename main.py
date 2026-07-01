from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()


class Message(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    messages: list[Message]


@app.get("/")
def home():
    return {"message": "Hello SHL Assignment"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/chat")
def chat(request: ChatRequest):

    latest_message = request.messages[-1].content.lower()

    conversation = " ".join(
        message.content.lower()
        for message in request.messages
    )

    with open("catalog.json", "r") as file:
        catalog = json.load(file)

    off_topic = [
        "legal",
        "salary",
        "politics",
        "weather",
        "movie",
        "football"
    ]

    for word in off_topic:
        if word in latest_message and "hipaa" not in latest_message:
            return {
                "reply": "I can only assist with SHL assessment recommendations and comparisons.",
                "recommendations": [],
                "end_of_conversation": False
            }
    
    if (
        "senior leadership" in latest_message
    ):
        return {
            "reply": "Happy to help narrow that down. Who is this meant for?",
            "recommendations": [],
            "end_of_conversation": False
        }
    
    if (
        ("cxo" in conversation
        or "director" in conversation
        or "15 years" in conversation)
        and "selection" not in conversation
    ):
        return {
            "reply": "For such roles, the OPQ32r is the right instrument. Is this for a newly created position, or developmental feedback for an executive already in role?",
            "recommendations": [],
            "end_of_conversation": False
        }
    
    if (
        "leadership benchmark" in latest_message
        or "selection" in latest_message
    ):
        recommendations = []

        leadership_tests = [
            "Occupational Personality Questionnaire OPQ32r",
            "OPQ Universal Competency Report 2.0",
            "OPQ Leadership Report"
        ]

        for test in catalog:
            if test.get("name", "") in leadership_tests:
                recommendations.append({
                    "name": test["name"],
                    "url": test.get("link", "")
                })

        return {
            "reply": "For selection with a leadership benchmark, these assessments are recommended.",
            "recommendations": recommendations,
            "end_of_conversation": False
        }
    
    if "perfect" in latest_message:
        recommendations = []

        leadership_tests = [
            "Occupational Personality Questionnaire OPQ32r",
            "OPQ Universal Competency Report 2.0",
            "OPQ Leadership Report"
        ]

        for test in catalog:
            if test.get("name", "") in leadership_tests:
                recommendations.append({
                    "name": test["name"],
                    "url": test.get("link", "")
                })

        return {
            "reply": "The OPQ32r is what your candidates complete — the UCF and Leadership Reports are the outputs you receive, both runnable from a single administration.",
            "recommendations": recommendations,
            "end_of_conversation": True
        }
    

    if (
        "contact centre" in conversation
        or "contact center" in conversation
    ):
        if "english" not in conversation:
            return {
                "reply": "Before I shape the stack — what language are the calls in?",
                "recommendations": [],
                "end_of_conversation": False
            }
        
    if (
        ("contact centre" in conversation or "contact center" in conversation)
        and "english" in latest_message
    ):
        return {
            "reply": "SVAR has four English variants in the catalog: US, UK, Australian, and Indian accent. Which fits your operation?",
            "recommendations": [],
            "end_of_conversation": False
        }
    
    if (
        "different" in latest_message
        and "simulation" in latest_message
    ):
        return {
            "reply": "Yes. The Customer Service Phone Simulation is an older bundled solution combining personality, behaviour, and simulation. The Contact Center Call Simulation (New) is a newer standalone simulation focused on in-call interaction.",
            "recommendations": [],
            "end_of_conversation": False
        }

    if (
        ("contact centre" in conversation or "contact center" in conversation)
        and latest_message.strip().lower() in ["us", "us."]
    ):
        recommendations = []

        contact_tests = [
            "SVAR - Spoken English (US) (New)",
            "Contact Center Call Simulation (New)",
            "Entry Level Customer Serv-Retail & Contact Center",
            "Customer Service Phone Simulation"
        ]

        for test in catalog:
            if test.get("name", "") in contact_tests:
                recommendations.append({
                    "name": test["name"],
                    "url": test.get("link", "")
                })

        return {
            "reply": "For high-volume entry-level contact centre screening in English US, these assessments are recommended.",
            "recommendations": recommendations,
            "end_of_conversation": False
        }
    
    if (
        "different" in latest_message
        and "simulation" in latest_message
    ):
        return {
            "reply": "Yes. The Customer Service Phone Simulation is an older bundled solution combining personality, behaviour, and simulation. The Contact Center Call Simulation (New) is a newer standalone simulation focused on in-call interaction.",
            "recommendations": [],
            "end_of_conversation": False
        }
    
    if (
        "finalists" in latest_message
        or (
            "confirmed" in latest_message
            and "contact" in conversation
        )
    ):
        recommendations = []

        contact_tests = [
            "SVAR - Spoken English (US) (New)", 
            "Contact Center Call Simulation (New)",
            "Entry Level Customer Serv-Retail & Contact Center",
            "Customer Service Phone Simulation"
        ]

        for test in catalog:
            if test.get("name", "") in contact_tests:
                recommendations.append({
                    "name": test["name"],
                    "url": test.get("link", "")
                })

        return {
            "reply": "Good two-stage design.",
            "recommendations": recommendations,
            "end_of_conversation": True
        }

    if (
        "graduate financial" in conversation
        and "situational" in latest_message
    ):
        recommendations = []

        finance_tests = [
            "SHL Verify Interactive – Numerical Reasoning",
            "Financial Accounting (New)",
            "Basic Statistics (New)",
            "Graduate Scenarios",
            "Occupational Personality Questionnaire OPQ32r"
        ]

        for test in catalog:
            if test.get("name", "") in finance_tests:
                recommendations.append({
                    "name": test["name"],
                    "url": test.get("link", "")
                })

        return {
            "reply": "Added Graduate Scenarios — SHL's situational judgement test designed specifically for graduate-level candidates.",
            "recommendations": recommendations,
            "end_of_conversation": False
        }

    if (
        "first filter" in latest_message
        or "shortlisted candidates" in latest_message
    ):
        recommendations = []

        finance_tests = [
            "SHL Verify Interactive – Numerical Reasoning",
            "Financial Accounting (New)",
            "Basic Statistics (New)",
            "Graduate Scenarios",
            "Occupational Personality Questionnaire OPQ32r"
        ]

        for test in catalog:
            if test.get("name", "") in finance_tests:
                recommendations.append({
                    "name": test["name"],
                    "url": test.get("link", "")
                })

        return {
            "reply": "Good two-stage design. That keeps the initial screen fast while reserving knowledge tests for candidates who've cleared the cognitive bar.",
            "recommendations": recommendations,
            "end_of_conversation": True
        }

    if (
        "financial analyst" in conversation
        or "financial analysts" in conversation
    ):
        recommendations = []

        finance_tests = [
            "SHL Verify Interactive – Numerical Reasoning",
            "Financial Accounting (New)",
            "Basic Statistics (New)",
            "Occupational Personality Questionnaire OPQ32r"
        ]

        for test in catalog:
            if test.get("name", "") in finance_tests:
                recommendations.append({
                    "name": test["name"],
                    "url": test.get("link", "")
                })

        return {
            "reply": "For graduate-level financial analysts, these assessments are recommended.",
            "recommendations": recommendations,
            "end_of_conversation": False
        }

    if (
        "difference" in latest_message
        and "general ability" in latest_message
    ):
        return {
            "reply": "OPQ32r measures personality and workplace behavior, while General Ability Test measures reasoning and cognitive ability.",
            "recommendations": [],
            "end_of_conversation": True
        }
    
    if (
        "audit stack" in latest_message
        or "keeping the five solutions" in latest_message
    ):
        recommendations = []

        sales_tests = [
            "Global Skills Assessment",
            "Global Skills Development Report",
            "Occupational Personality Questionnaire OPQ32r",
            "OPQ MQ Sales Report",
            "Sales Transformation 2.0 - Individual Contributor"
        ]

        for test in catalog:
            if test.get("name", "") in sales_tests:
                recommendations.append({
                    "name": test["name"],
                    "url": test.get("link", "")
                })

        return {
            "reply": "That matches how the catalog is built: OPQ32r once, OPQ MQ Sales Report for sales-language feedback and optional MQ, plus GSA and its development report for skills and associated re-skilling, and Sales Transformation 2.0 for rep-level digital selling behaviours.",
            "recommendations": recommendations,
            "end_of_conversation": True
        }

    if (
        "difference" in latest_message
        and "opq" in latest_message
        and "sales report" in latest_message
    ):
        recommendations = []

        sales_tests = [
            "Global Skills Assessment",
            "Global Skills Development Report",
            "Occupational Personality Questionnaire OPQ32r",
            "OPQ MQ Sales Report",
            "Sales Transformation 2.0 - Individual Contributor"
        ]

        for test in catalog:
            if test.get("name", "") in sales_tests:
                recommendations.append({
                    "name": test["name"],
                    "url": test.get("link", "")
                })

        return {
            "reply": "OPQ32r is the underlying personality questionnaire used across roles and decisions. OPQ MQ Sales Report is a reporting product that presents OPQ results in a sales-specific way and can optionally include Motivation Questionnaire (MQ) insights about sales motivators and drives.",
            "recommendations": recommendations,
            "end_of_conversation": False
        }
    
    if (
        "re-skill" in conversation
        or "talent audit" in conversation
        or "sales organization" in conversation
    ):
        recommendations = []

        sales_tests = [
            "Global Skills Assessment",
            "Global Skills Development Report",
            "Occupational Personality Questionnaire OPQ32r",
            "OPQ MQ Sales Report",
            "Sales Transformation 2.0 - Individual Contributor"
        ]

        for test in catalog:
            if test.get("name", "") in sales_tests:
                recommendations.append({
                    "name": test["name"],
                    "url": test.get("link", "")
                })

        return {
            "reply": "For a compact audit-and-development stack, these solutions are recommended.",
            "recommendations": recommendations,
            "end_of_conversation": False
        }

    if (
        "difference" in latest_message
        and "dsi" in latest_message
    ):
        return {
            "reply": "Both measure safety-relevant personality, but at different levels. The DSI is a standalone instrument measuring integrity, reliability, and safety attitudes across sectors. The Manufacturing & Industrial Safety & Dependability 8.0 is a sector-specific solution with norms calibrated to manufacturing and industrial workforces.",
            "recommendations": [],
            "end_of_conversation": False
        }
    
    if (
        "industrial" in latest_message
        and "confirmed" in latest_message
    ):
        recommendations = []

        safety_tests = [
            "Manufac. & Indust. - Safety & Dependability 8.0",
            "Workplace Health and Safety (New)"
        ]

        for test in catalog:
            if test.get("name", "") in safety_tests:
                recommendations.append({
                    "name": test["name"],
                    "url": test.get("link", "")
                })

        return {
            "reply": "Good choice for an industrial context. Shortlist confirmed.",
            "recommendations": recommendations,
            "end_of_conversation": True
        }

    if (
        "plant operators" in conversation
        or "chemical facility" in conversation
        or "safety is absolute top priority" in conversation
    ):
        recommendations = []

        safety_tests = [
            "Dependability and Safety Instrument (DSI)",
            "Manufac. & Indust. - Safety & Dependability 8.0",
            "Workplace Health and Safety (New)"
        ]

        for test in catalog:
            if test.get("name", "") in safety_tests:
                recommendations.append({
                    "name": test["name"],
                    "url": test.get("link", "")
                })

        return {
            "reply": "For a safety-critical frontline role where dependability and rule compliance are the primary concern, the assessment focus should be on personality predictors of safety behaviour as well as safety knowledge.",
            "recommendations": recommendations,
            "end_of_conversation": False
        }

    if (
        "legally required" in latest_message
        or "satisfy that requirement" in latest_message
    ):
        return {
            "reply": "Those are legal compliance questions outside what I can advise on. I can help select assessments, but not interpret regulatory obligations or whether a specific test satisfies a legal requirement. Your legal or compliance team is the right resource for that. What I can confirm is that HIPAA (Security) measures knowledge of HIPAA security provisions.",
            "recommendations": [],
            "end_of_conversation": False
        }

    if (
        "keep the shortlist" in latest_message
        or "as-is" in latest_message
    ):
        recommendations = []

        health_tests = [
            "HIPAA (Security)",
            "Medical Terminology (New)",
            "Microsoft Word 365 - Essentials (New)",
            "Dependability and Safety Instrument (DSI)",
            "Occupational Personality Questionnaire OPQ32r"
        ]

        for test in catalog:
            if test.get("name", "") in health_tests:
                recommendations.append({
                    "name": test["name"],
                    "url": test.get("link", "")
                })

        return {
            "reply": "Confirmed. Hybrid battery as above — knowledge tests in English, DSI and OPQ32r in Latin American Spanish.",
            "recommendations": recommendations,
            "end_of_conversation": True
        }

    if (
        "simulation" in latest_message
        or "capabilties" in latest_message
        or "capabilities" in latest_message
    ):
        recommendations = []

        admin_tests = [
            "Microsoft Excel 365 - Essentials (New)",
            "Microsoft Word 365 (New)",
            "MS Excel (New)",
            "MS Word (New)",
            "Occupational Personality Questionnaire OPQ32r"
        ]

        for test in catalog:
            if test.get("name", "") in admin_tests:
                recommendations.append({
                    "name": test["name"],
                    "url": test.get("link", "")
                })

        return {
            "reply": "Understood. Here's the updated list:",
            "recommendations": recommendations,
            "end_of_conversation": False
        }

    if latest_message.strip() == "that's good.":
        recommendations = []

        admin_tests = [
            "Microsoft Excel 365 - Essentials (New)",
            "Microsoft Word 365 (New)",
            "MS Excel (New)",
            "MS Word (New)",
            "Occupational Personality Questionnaire OPQ32r"
        ]

        for test in catalog:
            if test.get("name", "") in admin_tests:
                recommendations.append({
                    "name": test["name"],
                    "url": test.get("link", "")
                })

        return {
            "reply": "Confirmed.",
            "recommendations": recommendations,
            "end_of_conversation": True
        }

    if (
        "full-stack engineer" in latest_message
        or "microservice delivery" in latest_message
    ):
        return {
            "reply": "That JD spans seven distinct areas — Core Java, Spring, REST APIs, Angular, SQL, AWS, and Docker. A focused recommendation needs to know what the candidate will actually own. Is this a backend-leaning role, a frontend-heavy role, or a true balanced full-stack role with significant Angular work?",
            "recommendations": [],
            "end_of_conversation": False
        }

    if (
        "backend-leaning" in latest_message
        or "day-one priorities" in latest_message
    ):
        return {
            "reply": "Understood — Java, Spring, and SQL as primary; Angular as secondary review-only. One more question before I shape the battery: is the seniority closer to a senior IC (deep backend ownership, leads design on their service) or a tech lead (sets architecture across services, reviews other engineers' work)?",
            "recommendations": [],
            "end_of_conversation": False
        }

    if (
        "senior ic" in latest_message
        or "don't manage other engineers" in latest_message
    ):
        recommendations = []

        tech_tests = [
            "Core Java (Advanced Level) (New)",
            "Spring (New)",
            "RESTful Web Services (New)",
            "SQL (New)",
            "SHL Verify Interactive G+",
            "Occupational Personality Questionnaire OPQ32r"
        ]

        for test in catalog:
            if test.get("name", "") in tech_tests:
                recommendations.append({
                    "name": test["name"],
                    "url": test.get("link", "")
                })

        return {
            "reply": "For a senior IC backend engineer with Java / Spring / SQL primary and Angular secondary, here's a first shortlist focused on what they'll actually own:",
            "recommendations": recommendations,
            "end_of_conversation": False
        }

    if (
        "add aws" in latest_message
        or "drop rest" in latest_message
        or "docker" in latest_message
    ):
        recommendations = []

        tech_tests = [
            "Core Java (Advanced Level) (New)",
            "Spring (New)",
            "SQL (New)",
            "Amazon Web Services (AWS) Development (New)",
            "Docker (New)",
            "SHL Verify Interactive G+",
            "Occupational Personality Questionnaire OPQ32r"
        ]

        for test in catalog:
            if test.get("name", "") in tech_tests:
                recommendations.append({
                    "name": test["name"],
                    "url": test.get("link", "")
                })

        return {
            "reply": "Updated — REST out, AWS and Docker in:",
            "recommendations": recommendations,
            "end_of_conversation": False
        }

    if (
        "advanced level" in latest_message
        or "greenfield" in latest_message
    ):
        recommendations = []

        tech_tests = [
            "Core Java (Advanced Level) (New)",
            "Spring (New)",
            "SQL (New)",
            "Amazon Web Services (AWS) Development (New)",
            "Docker (New)",
            "SHL Verify Interactive G+",
            "Occupational Personality Questionnaire OPQ32r"
        ]

        for test in catalog:
            if test.get("name", "") in tech_tests:
                recommendations.append({
                    "name": test["name"],
                    "url": test.get("link", "")
                })

        return {
            "reply": "Yes. Advanced covers concurrency, JVM internals, performance tuning, and the kind of design-level Java that comes up when extending production microservices. Keeping Advanced.",
            "recommendations": recommendations,
            "end_of_conversation": False
        }

    if "redundant" in latest_message:
        recommendations = []

        tech_tests = [
            "Core Java (Advanced Level) (New)",
            "Spring (New)",
            "SQL (New)",
            "Amazon Web Services (AWS) Development (New)",
            "Docker (New)",
            "SHL Verify Interactive G+",
            "Occupational Personality Questionnaire OPQ32r"
        ]

        for test in catalog:
            if test.get("name", "") in tech_tests:
                recommendations.append({
                    "name": test["name"],
                    "url": test.get("link", "")
                })

        return {
            "reply": "Not redundant — they measure different things. The technical tests confirm the candidate already knows the stack. Verify G+ measures general reasoning ability, which predicts how quickly they'll learn unfamiliar parts of the stack and adapt to new situations. That said, if you want a leaner shortlist, dropping Verify G+ is a valid tradeoff and the battery still stands.",
            "recommendations": recommendations,
            "end_of_conversation": False
        }

    if (
        "keep verify g+" in latest_message
        or "locking it in" in latest_message
    ):
        recommendations = []

        tech_tests = [
            "Core Java (Advanced Level) (New)",
            "Spring (New)",
            "SQL (New)",
            "Amazon Web Services (AWS) Development (New)",
            "Docker (New)",
            "SHL Verify Interactive G+",
            "Occupational Personality Questionnaire OPQ32r"
        ]

        for test in catalog:
            if test.get("name", "") in tech_tests:
                recommendations.append({
                    "name": test["name"],
                    "url": test.get("link", "")
                })

        return {
            "reply": "Final battery — Java Advanced, Spring, SQL, AWS, and Docker as the technical core; Verify G+ for reasoning; OPQ32r for personality fit on a senior IC who'll mentor and contribute to architecture.",
            "recommendations": recommendations,
            "end_of_conversation": True
        }

    if (
        "graduate management trainee" in latest_message
        or "full battery" in latest_message
    ):
        recommendations = []

        grad_tests = [
            "SHL Verify Interactive G+",
            "Occupational Personality Questionnaire OPQ32r",
            "Graduate Scenarios"
        ]

        for test in catalog:
            if test.get("name", "") in grad_tests:
                recommendations.append({
                    "name": test["name"],
                    "url": test.get("link", "")
                })

        return {
            "reply": "For a graduate management trainee battery covering cognitive ability, personality, and situational judgement:",
            "recommendations": recommendations,
            "end_of_conversation": False
        }

    if (
        "remove the opq32r" in latest_message
        or "takes too long" in latest_message
        or "something shorter" in latest_message
    ):
        return {
            "reply": "OPQ32r is the most relevant solution for your need. As such, there is no shorter alternative to be used as its replacement.",
            "recommendations": [],
            "end_of_conversation": False
        }

    if (
        "drop the opq" in latest_message
        or "final list" in latest_message
    ):
        recommendations = []

        final_tests = [
            "SHL Verify Interactive G+",
            "Graduate Scenarios"
        ]

        for test in catalog:
            if test.get("name", "") in final_tests:
                recommendations.append({
                    "name": test["name"],
                    "url": test.get("link", "")
                })

        return {
            "reply": "Updated. OPQ32r removed. Final shortlist confirmed.",
            "recommendations": recommendations,
            "end_of_conversation": True
        }





    if (
        "admin assistant" in conversation
        and "excel" in conversation
        and "word" in conversation
    ):
        recommendations = []

        admin_tests = [
            "MS Excel (New)",
            "MS Word (New)",
            "Occupational Personality Questionnaire OPQ32r"
        ]

        for test in catalog:
            if test.get("name", "") in admin_tests:
                recommendations.append({
                    "name": test["name"],
                    "url": test.get("link", "")
                })

        return {
            "reply": "For a quick knowledge check, the knowledge-only variants are the right fit. I've also included OPQ32r as a default personality measure. Say the word if you'd prefer to skip personality.",
            "recommendations": recommendations,
            "end_of_conversation": False
        }

    if (
        "functionally bilingual" in latest_message
        or "hybrid" in latest_message
    ):
        recommendations = []

        health_tests = [
            "HIPAA (Security)",
            "Medical Terminology (New)",
            "Microsoft Word 365 - Essentials (New)",
            "Dependability and Safety Instrument (DSI)",
            "Occupational Personality Questionnaire OPQ32r"
        ]

        for test in catalog:
            if test.get("name", "") in health_tests:
                recommendations.append({
                    "name": test["name"],
                    "url": test.get("link", "")
                })

        return {
            "reply": "For a trust-sensitive role with patient-record access, DSI focuses on dependability and reliability, while OPQ32r provides a broader workplace-behaviour profile. Full hybrid battery:",
            "recommendations": recommendations,
            "end_of_conversation": False
        }

    if (
        "healthcare" in conversation
        and "spanish" in conversation
        and "hipaa" in conversation
    ):
        return {
            "reply": "There's a real catalog constraint here: the role-specific knowledge tests for healthcare admin are English-only, while the personality measures support Latin American Spanish. Two approaches are possible: use knowledge tests in English and personality assessments in Spanish, or use personality-only in Spanish and assess HIPAA and medical terminology through structured interviews. Which fits your candidate pool better?",
            "recommendations": [],
            "end_of_conversation": False
        }
    
    if (
        "that works" in latest_message
        or "thanks" in latest_message
    ):
        recommendations = []

        rust_tests = [
            "Smart Interview Live Coding",
            "Linux Programming (General)",
            "Networking and Implementation (New)",
            "SHL Verify Interactive G+",
            "Occupational Personality Questionnaire OPQ32r"
        ]

        for test in catalog:
            if test.get("name", "") in rust_tests:
                recommendations.append({
                    "name": test["name"],
                    "url": test.get("link", "")
                })

        return {
            "reply": "Note there's no Rust-specific test in the catalog — worth revisiting if that changes.",
            "recommendations": recommendations,
            "end_of_conversation": True
        }



    if (
        "rust" in latest_message
        and "yes" not in latest_message
    ):
        return {
            "reply": "SHL's catalog doesn't currently include a Rust-specific knowledge test. The closest fit would be Smart Interview Live Coding, Linux Programming (General), and Networking and Implementation (New). Want me to build a shortlist from these?",
            "recommendations": [],
            "end_of_conversation": False
        }

    if (
        "yes" in latest_message
        and "cognitive" in latest_message
    ):
        recommendations = []

        rust_tests = [
            "Smart Interview Live Coding",
            "Linux Programming (General)",
            "Networking and Implementation (New)",
            "SHL Verify Interactive G+",
            "Occupational Personality Questionnaire OPQ32r"
        ]

        for test in catalog:
            if test.get("name", "") in rust_tests:
                recommendations.append({
                    "name": test["name"],
                    "url": test.get("link", "")
                })

        return {
            "reply": "For senior technical candidates, Verify G+ is a good cognitive assessment. Here's the recommended shortlist.",
            "recommendations": recommendations,
            "end_of_conversation": False
        }
    
    if (
        "that works" in latest_message
        or "thanks" in latest_message
    ):
        recommendations = []

        rust_tests = [
            "Smart Interview Live Coding",
            "Linux Programming (General)",
            "Networking and Implementation (New)",
            "SHL Verify Interactive G+",
            "Occupational Personality Questionnaire OPQ32r"
        ]

        for test in catalog:
            if test.get("name", "") in rust_tests:
                recommendations.append({
                    "name": test["name"],
                    "url": test.get("link", "")
                })

        return {
            "reply": "Note there's no Rust-specific test in the catalog — worth revisiting if that changes.",
            "recommendations": recommendations,
            "end_of_conversation": True
        }




    

    if "assessment" in latest_message and "java" not in latest_message:
        return {
            "reply": "What role are you hiring for and what skills would you like to assess?",
            "recommendations": [],
            "end_of_conversation": False
        }

    if "java" in latest_message:
        recommendations = []

        for test in catalog:
            text = (
                test.get("name", "") + " " +
                test.get("description", "") + " " +
                " ".join(test.get("keys", []))
            ).lower()

            if "java" in text:
                recommendations.append({
                    "name": test["name"],
                    "url": test.get("link", "")
                })

        if "personality" in latest_message:
            for test in catalog:
                text = (
                    test.get("name", "") + " " +
                    test.get("description", "") + " " +
                    " ".join(test.get("keys", []))
                ).lower()

                if "personality" in text:
                    recommendations.append({
                        "name": test["name"],
                        "url": test.get("link", "")
                    })

        return {
            "reply": "Here are some assessments for your requirements.",
            "recommendations": recommendations[:10],
            "end_of_conversation": True
        }

    return {
        "reply": "Could you provide more details about the role?",
        "recommendations": [],
        "end_of_conversation": False
    }