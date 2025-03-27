from flask import Flask, render_template, request, jsonify
import datetime
import json
import os
import random

# Initialize Flask application
app = Flask(__name__)

# Ensure the 'static/data' directory exists
os.makedirs('static/data', exist_ok=True)

# Define the path to resume data
resume_data_path = 'static/data/resume_data.json'

# Load resume data from JSON file if it exists
if os.path.exists(resume_data_path):
    try:
        with open(resume_data_path, 'r') as f:
            resume_data = json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        print(f"Error loading resume data: {e}")
        # Fall back to the default data if file can't be loaded
        # Define default resume data (your existing resume_data dictionary)
        resume_data = {
            "personal_info": {
                "name": "Samuel Adegbenjo O.",
                "title": "Information Security & Data Analytics Professional",
                "social_links": {
                    "linkedin": "https://www.linkedin.com/in/samuel-adegbenjo-1b5277118/",
                    "github": "#"
                }
            },
            "experience": [
                {
                    "role": "Graduate Assistant",
                    "company": "University of Arkansas",
                    "period": "August 2022 – Present",
                    "achievements": [
                        "Assisted instructors with classroom management, grading, and technology setup",
                        "Created first destination surveys and conducted data analysis with Qualtrics systems for undergraduate students to gather data about post-graduation plans",
                        "Developed a Python script to automate the process of populating missing data across multiple Excel files, improving data completeness and consistency",
                        "Conducted in-depth analysis on events and student data sourced from Handshake and Career Connections portal leveraging Power BI and Tableau to create insightful dashboards and reports",
                        "Developed strong communication and interpersonal skills through interactions with students and faculty members"
                    ]
                },
                {
                    "role": "Information Security Risk Analyst",
                    "company": "Total E & P Nigeria Limited",
                    "period": "January 2020 – July 2022",
                    "achievements": [
                        "Designed risk assessment protocols and conducted regular evaluations to enhance Total Energy and Petroleum's operational integrity",
                        "Developed internal compliance and risk mitigation strategies with emphasis on continuous improvement and customer satisfaction",
                        "Identified and monitored key risk indicators (KRIs)",
                        "Advised on IT risk posture for engineering teams to optimize internal controls",
                        "Conducted regular internal audits to assess compliance with ISO 9001 standards and identify areas for improvement",
                        "Performed cloud security risk assessments, and developed ISMS policies, standards and controls in a regulated environment aligning with business functions and requirements"
                    ]
                },
                {
                    "role": "Research Assistant",
                    "company": "University of Ibadan",
                    "period": "March 2016 – June 2019",
                    "achievements": [
                        "Conducted literature reviews and gathered data on ICT and Social Order",
                        "Analyzed and Interpreted data, creating visual representations like graphs and charts",
                        "Assisted in drafting, reviewing, and editing research papers, articles, and reports",
                        "Managed research projects, coordinated timelines, and prepared presentations for conferences and seminars"
                    ]
                }
            ],
            "education": [
                {
                    "degree": "M.I.S, Management of Information Systems (Cybersecurity/Adaptive Cloud Infrastructure)",
                    "institution": "University of Arkansas",
                    "year": "Expected May 2025"
                },
                {
                    "degree": "M.A., History",
                    "institution": "University of Arkansas, USA",
                    "year": "2024"
                },
                {
                    "degree": "B.A., History",
                    "institution": "University of Ibadan (U.I.), Oyo State, Nigeria",
                    "year": "2019"
                }
            ],
            "certifications": [
                {"name": "Security+", "issuer": "CompTIA", "status": "Completed"},
                {"name": "Artificial Intelligence Fundamentals", "issuer": "IBM", "status": "Completed"},
                {"name": "CISA", "issuer": "ISACA", "status": "In Progress"}
            ],
            "skills": {
                "programming": ["Python"],
                "ml_frameworks": ["TensorFlow", "ONNX", "PyTorch", "Scikit-Learn", "Pandas", "NumPy"],
                "cloud_computing": ["Microsoft Azure (Machine Learning Studio, Virtual Machines, Blob Storage)"],
                "data_analysis": ["SQL", "Excel", "Tableau", "PowerBI"],
                "other_technical": ["Artificial Neural Networks", "Data Preprocessing", "Deep Learning", "Natural Language Processing (NLP)"],
                "business": ["Communication (Oral & Written)", "Problem-Solving", "Cross-functional Collaboration"]
            },
            "key_courses": [
                {
                    "name": "ERP FUNDAMENTALS",
                    "description": "Comprehensive introduction to Enterprise Resource Planning (ERP) systems, focusing on their role in integrating business processes across sales, finance, HR, and supply chain management. Gained practical skills in executing, analyzing, and modeling business processes with SAP ERP software, enhancing ability to make data-driven operational and strategic decisions."
                },
                {
                    "name": "IT SKILLS SEMINAR",
                    "description": "Equipped with foundational skills in business, information systems, and analytics, including proficiency in Microsoft Excel, descriptive statistics, and programming fundamentals. Developed expertise in project management, technology ethics, and business communication."
                },
                {
                    "name": "DATA AND CYBERSECURITY",
                    "description": "Comprehensive understanding of cybersecurity principles, including risk management, threat assessment, and incident response planning. Gained practical experience in data protection strategies such as encryption and access controls and explored regulatory compliance with standards like GDPR and HIPAA."
                },
                {
                    "name": "DATA AND SYSTEM SECURITY",
                    "description": "Understanding of the intersection between security frameworks and practical cybersecurity applications, emphasizing the CIA Triad: Confidentiality, Integrity, and Availability. Explored key principles such as Defense in Depth, Least Privilege, Identity and Access Management, and Security by Design."
                }
            ],
            "projects": [
                {
                    "title": "Automated Data Population Script",
                    "description": "Developed a Python script to automate the process of populating missing data across multiple Excel files, improving data completeness and consistency.",
                    "technologies": ["Python", "Pandas", "Excel"]
                },

                {
                    "title": "Development of a college event management website using Agile methodology",
                    "description": "Led the development of a college event management website using Agile methodology and SDLC best practices within a cross-functional team. Implemented a robust CI/CD pipeline in GitHub, emphasizing secure workflows and automated testing to ensure application security. This project enhanced my skills in web development, agile practices, and cloud technologies while fostering effective teamwork and communication.",
                    "technologies": ["HTML", "CSS", "JavaScript", "Agile", "GitHub"]
                },

                {
                    "title": "Development of a comprehensive roadmap to enhance student career readiness services at the Career Services ",
                    "description": "Led the development of a comprehensive roadmap to enhance student career readiness services at the Career Services department. This involved identifying critical skills gaps, defining key capabilities, and creating a multi-year plan for implementing new programs and services. I collaborated with stakeholders to prioritize initiatives and successfully implemented key roadmap elements, such as mentorship program and career coaching.  I continuously monitored progress and adjusted the roadmap to ensure its alignment with evolving student needs and market demands.",
                    "technologies": ["Roadmap", "Career Services", "Student Career Readiness"]
                },

                {
                    "title": "ERPsim business simulation utilizing SAP S/4HANA",
                    "description": "Participated in an ERPsim business simulation utilizing SAP S/4HANA, where I analyzed real-time OData feeds with PowerBI to make strategic decisions in a competitive market. Collaborated with my team to optimize production, procurement, and sales, while monitoring KPIs to achieve company objectives within the simulation. This experience enhanced my understanding of ERP systems, data-driven decision-making, and teamwork in a dynamic business environment.",
                    "technologies": ["SAP S/4HANA", "PowerBI", "OData"]
                },

                {
                    "title": "Machine learning-based phishing email detection program",
                    "description": "Developed a machine learning-based phishing email detection program that analyzes incoming emails and flags potential threats using a trained binary classifier(with phishing datasets). This browser extension effectively identifies and filters malicious emails, reducing the risk of phishing attacks with high accuracy.",
                    "technologies": ["Python", "Machine Learning", "Browser Extension", "ONNX", "TensorFlow", "Random Forest"]
                },

                {
                    "title": "Python-based Speech to Text Transcription Tool",
                    "description": "Developed a Python-based Speech to Text Transcription Tool using the Google Speech Recognition API. This tool offers both a user-friendly GUI (tkinter) and CLI, enabling real-time speech recognition and transcription. Transcriptions are automatically saved to a text file, providing a convenient solution for capturing spoken information. This project highlights my Python programming, GUI development, and API integration skills.",
                    "technologies": ["Python", "Google Speech Recognition API", "tkinter"]
                },

                {
                    "title": "Python-based web vulnerability scanner",
                    "description": "Developed a Python-based web vulnerability scanner that identifies potential security risks in web applications. The tool checks for basic reflected Cross-Site Scripting (XSS) and SQL injection vulnerabilities by sending crafted payloads to the target URL and analyzing the responses. Additionally, it scrapes web pages to find and extract information about HTML forms, providing insights into potential attack vectors. Utilized libraries such as requests for HTTP requests and BeautifulSoup for web scraping.",
                    "technologies": ["Python", "Requests", "BeautifulSoup"]
                },

                {
                    "title": "Student Data Analysis Dashboard",
                    "description": "Conducted in-depth analysis on events and student data sourced from Handshake and Career Connections portal leveraging Power BI and Tableau to create insightful dashboards and reports.",
                    "technologies": ["Power BI", "Tableau", "Data Analysis"]
                },

                {
                    "title": "vulnerability scans",
                    "description": "Conducted vulnerability scans on a TryHackMe target machine using Gobuster, uncovering hidden directories and potential security weaknesses. Employed various wordlists and settings to maximize scan coverage and identify vulnerabilities like exposed admin panels. This project enhanced my practical understanding of web server security, vulnerability scanning techniques, and the effective use of Gobuster.",
                    "technologies": ["Gobuster", "TryHackMe"]
                }
            ]
        }
else:
    # If file doesn't exist, use default data
    resume_data = {
        "personal_info": {
            "name": "Samuel Adegbenjo O.",
            "title": "Information Security & Data Analytics Professional",
            "social_links": {
                "linkedin": "https://www.linkedin.com/in/samuel-adegbenjo-1b5277118/",
                "github": "#"
            }
        },
        "experience": [
            {
                "role": "Graduate Assistant",
                "company": "University of Arkansas",
                "period": "August 2022 – Present",
                "achievements": [
                    "Assisted instructors with classroom management, grading, and technology setup",
                    "Created first destination surveys and conducted data analysis with Qualtrics systems for undergraduate students to gather data about post-graduation plans",
                    "Developed a Python script to automate the process of populating missing data across multiple Excel files, improving data completeness and consistency",
                    "Conducted in-depth analysis on events and student data sourced from Handshake and Career Connections portal leveraging Power BI and Tableau to create insightful dashboards and reports",
                    "Developed strong communication and interpersonal skills through interactions with students and faculty members"
                ]
            },
            {
                "role": "Information Security Risk Analyst",
                "company": "Total E & P Nigeria Limited",
                "period": "January 2020 – July 2022",
                "achievements": [
                    "Designed risk assessment protocols and conducted regular evaluations to enhance Total Energy and Petroleum's operational integrity",
                    "Developed internal compliance and risk mitigation strategies with emphasis on continuous improvement and customer satisfaction",
                    "Identified and monitored key risk indicators (KRIs)",
                    "Advised on IT risk posture for engineering teams to optimize internal controls",
                    "Conducted regular internal audits to assess compliance with ISO 9001 standards and identify areas for improvement",
                    "Performed cloud security risk assessments, and developed ISMS policies, standards and controls in a regulated environment aligning with business functions and requirements"
                ]
            },
            {
                "role": "Research Assistant",
                "company": "University of Ibadan",
                "period": "March 2016 – June 2019",
                "achievements": [
                    "Conducted literature reviews and gathered data on ICT and Social Order",
                    "Analyzed and Interpreted data, creating visual representations like graphs and charts",
                    "Assisted in drafting, reviewing, and editing research papers, articles, and reports",
                    "Managed research projects, coordinated timelines, and prepared presentations for conferences and seminars"
                ]
            }
        ],
        "education": [
            {
                "degree": "M.I.S, Management of Information Systems (Cybersecurity/Adaptive Cloud Infrastructure)",
                "institution": "University of Arkansas",
                "year": "Expected May 2025"
            },
            {
                "degree": "M.A., History",
                "institution": "University of Arkansas, USA",
                "year": "2024"
            },
            {
                "degree": "B.A., History",
                "institution": "University of Ibadan (U.I.), Oyo State, Nigeria",
                "year": "2019"
            }
        ],
        "certifications": [
            {"name": "Security+", "issuer": "CompTIA", "status": "Completed"},
            {"name": "Artificial Intelligence Fundamentals", "issuer": "IBM", "status": "Completed"},
            {"name": "CISA", "issuer": "ISACA", "status": "In Progress"}
        ],
        "skills": {
            "programming": ["Python"],
            "ml_frameworks": ["TensorFlow", "ONNX", "PyTorch", "Scikit-Learn", "Pandas", "NumPy"],
            "cloud_computing": ["Microsoft Azure (Machine Learning Studio, Virtual Machines, Blob Storage)"],
            "data_analysis": ["SQL", "Excel", "Tableau", "PowerBI"],
            "other_technical": ["Artificial Neural Networks", "Data Preprocessing", "Deep Learning", "Natural Language Processing (NLP)"],
            "business": ["Communication (Oral & Written)", "Problem-Solving", "Cross-functional Collaboration"]
        },
        "key_courses": [
            {
                "name": "ERP FUNDAMENTALS",
                "description": "Comprehensive introduction to Enterprise Resource Planning (ERP) systems, focusing on their role in integrating business processes across sales, finance, HR, and supply chain management. Gained practical skills in executing, analyzing, and modeling business processes with SAP ERP software, enhancing ability to make data-driven operational and strategic decisions."
            },
            {
                "name": "IT SKILLS SEMINAR",
                "description": "Equipped with foundational skills in business, information systems, and analytics, including proficiency in Microsoft Excel, descriptive statistics, and programming fundamentals. Developed expertise in project management, technology ethics, and business communication."
            },
            {
                "name": "DATA AND CYBERSECURITY",
                "description": "Comprehensive understanding of cybersecurity principles, including risk management, threat assessment, and incident response planning. Gained practical experience in data protection strategies such as encryption and access controls and explored regulatory compliance with standards like GDPR and HIPAA."
            },
            {
                "name": "DATA AND SYSTEM SECURITY",
                "description": "Understanding of the intersection between security frameworks and practical cybersecurity applications, emphasizing the CIA Triad: Confidentiality, Integrity, and Availability. Explored key principles such as Defense in Depth, Least Privilege, Identity and Access Management, and Security by Design."
            }
        ],
        "projects": [
            {
                "title": "Automated Data Population Script",
                "description": "Developed a Python script to automate the process of populating missing data across multiple Excel files, improving data completeness and consistency.",
                "technologies": ["Python", "Pandas", "Excel"]
            },

            {
                "title": "Development of a college event management website using Agile methodology",
                "description": "Led the development of a college event management website using Agile methodology and SDLC best practices within a cross-functional team. Implemented a robust CI/CD pipeline in GitHub, emphasizing secure workflows and automated testing to ensure application security. This project enhanced my skills in web development, agile practices, and cloud technologies while fostering effective teamwork and communication.",
                "technologies": ["HTML", "CSS", "JavaScript", "Agile", "GitHub"]
            },

            {
                "title": "Development of a comprehensive roadmap to enhance student career readiness services at the Career Services ",
                "description": "Led the development of a comprehensive roadmap to enhance student career readiness services at the Career Services department. This involved identifying critical skills gaps, defining key capabilities, and creating a multi-year plan for implementing new programs and services. I collaborated with stakeholders to prioritize initiatives and successfully implemented key roadmap elements, such as mentorship program and career coaching.  I continuously monitored progress and adjusted the roadmap to ensure its alignment with evolving student needs and market demands.",
                "technologies": ["Roadmap", "Career Services", "Student Career Readiness"]
            },

            {
                "title": "ERPsim business simulation utilizing SAP S/4HANA",
                "description": "Participated in an ERPsim business simulation utilizing SAP S/4HANA, where I analyzed real-time OData feeds with PowerBI to make strategic decisions in a competitive market. Collaborated with my team to optimize production, procurement, and sales, while monitoring KPIs to achieve company objectives within the simulation. This experience enhanced my understanding of ERP systems, data-driven decision-making, and teamwork in a dynamic business environment.",
                "technologies": ["SAP S/4HANA", "PowerBI", "OData"]
            },

            {
                "title": "Machine learning-based phishing email detection program",
                "description": "Developed a machine learning-based phishing email detection program that analyzes incoming emails and flags potential threats using a trained binary classifier(with phishing datasets). This browser extension effectively identifies and filters malicious emails, reducing the risk of phishing attacks with high accuracy.",
                "technologies": ["Python", "Machine Learning", "Browser Extension", "ONNX", "TensorFlow", "Random Forest"]
            },

            {
                "title": "Python-based Speech to Text Transcription Tool",
                "description": "Developed a Python-based Speech to Text Transcription Tool using the Google Speech Recognition API. This tool offers both a user-friendly GUI (tkinter) and CLI, enabling real-time speech recognition and transcription. Transcriptions are automatically saved to a text file, providing a convenient solution for capturing spoken information. This project highlights my Python programming, GUI development, and API integration skills.",
                "technologies": ["Python", "Google Speech Recognition API", "tkinter"]
            },

            {
                "title": "Python-based web vulnerability scanner",
                "description": "Developed a Python-based web vulnerability scanner that identifies potential security risks in web applications. The tool checks for basic reflected Cross-Site Scripting (XSS) and SQL injection vulnerabilities by sending crafted payloads to the target URL and analyzing the responses. Additionally, it scrapes web pages to find and extract information about HTML forms, providing insights into potential attack vectors. Utilized libraries such as requests for HTTP requests and BeautifulSoup for web scraping.",
                "technologies": ["Python", "Requests", "BeautifulSoup"]
            },

            {
                "title": "Student Data Analysis Dashboard",
                "description": "Conducted in-depth analysis on events and student data sourced from Handshake and Career Connections portal leveraging Power BI and Tableau to create insightful dashboards and reports.",
                "technologies": ["Power BI", "Tableau", "Data Analysis"]
            },

            {
                "title": "vulnerability scans",
                "description": "Conducted vulnerability scans on a TryHackMe target machine using Gobuster, uncovering hidden directories and potential security weaknesses. Employed various wordlists and settings to maximize scan coverage and identify vulnerabilities like exposed admin panels. This project enhanced my practical understanding of web server security, vulnerability scanning techniques, and the effective use of Gobuster.",
                "technologies": ["Gobuster", "TryHackMe"]
            }
        ]
    }
    
    # Save the default data to the JSON file
    with open(resume_data_path, 'w') as f:
        json.dump(resume_data, f, indent=4)

# Real-time analytics data (simulated)
analytics_data = {
    "page_views": {
        "home": random.randint(500, 1000),
        "experience": random.randint(300, 800),
        "education": random.randint(200, 600),
        "skills": random.randint(400, 900),
        "projects": random.randint(350, 850)
    },
    "visitor_locations": {
        "United States": random.randint(40, 60),
        "Nigeria": random.randint(10, 30),
        "United Kingdom": random.randint(5, 15),
        "Canada": random.randint(5, 15),
        "Other": random.randint(5, 20)
    },
    "device_types": {
        "Desktop": random.randint(50, 70),
        "Mobile": random.randint(20, 40),
        "Tablet": random.randint(5, 15)
    }
}

# Add a "featured" flag to your projects
for project in resume_data["projects"]:
    project["featured"] = False
    
# Set specific projects as featured (adjust indices as needed)
resume_data["projects"][1]["featured"] = True  # Second project
resume_data["projects"][4]["featured"] = True  # Fifth project (the ML phishing detection project)

# Routes
@app.route('/')
def home():
    now = datetime.datetime.now()
    # Filter for featured projects only
    featured_projects = [p for p in resume_data['projects'] if p.get('featured', False)]
    # Limit to 2 if somehow more are marked as featured
    featured_projects = featured_projects[:2]
    
    return render_template('index.html', personal_info=resume_data['personal_info'], 
                           experience=resume_data['experience'][:2],
                           skills=resume_data['skills'],
                           projects=featured_projects,
                           now=now)

@app.route('/experience')
def experience():
    now = datetime.datetime.now()
    return render_template('experience.html', personal_info=resume_data['personal_info'], 
                           experience=resume_data['experience'],
                           now=now)

@app.route('/education')
def education():
    now = datetime.datetime.now()
    return render_template('education.html', personal_info=resume_data['personal_info'], 
                           education=resume_data['education'],
                           certifications=resume_data['certifications'],
                           key_courses=resume_data['key_courses'],
                           now=now)

@app.route('/skills')
def skills():
    now = datetime.datetime.now()
    return render_template('skills.html', personal_info=resume_data['personal_info'], 
                           skills=resume_data['skills'],
                           other_technical=resume_data['skills']['other_technical'],  # Include other_technical skills
                           now=now)

@app.route('/projects')
def projects():
    now = datetime.datetime.now()
    return render_template('projects.html', personal_info=resume_data['personal_info'], 
                           projects=resume_data['projects'],
                           now=now)

@app.route('/contact')
def contact():
    now = datetime.datetime.now()
    return render_template('contact.html', personal_info=resume_data['personal_info'],
                           now=now)

# Real-time features
@app.route('/api/visitor-count')
def visitor_count():
    """Simulate real-time visitor count with random fluctuations"""
    base_count = 15
    fluctuation = random.randint(-5, 10)
    return jsonify({"count": base_count + fluctuation})

@app.route('/api/analytics')
def analytics():
    """Return simulated analytics data"""
    # Add a timestamp to give the impression of real-time data
    analytics_data["timestamp"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return jsonify(analytics_data)

# Helper function to check if visitor is new (simulated)
@app.route('/api/check-new-visitor')
def check_new_visitor():
    """Simulated check if the visitor is new to the site"""
    is_new = random.choice([True, False])
    return jsonify({"is_new": is_new})

if __name__ == '__main__':
    # Create necessary directories if they don't exist
    os.makedirs('static/data', exist_ok=True)
    os.makedirs('static/css', exist_ok=True)
    os.makedirs('static/js', exist_ok=True)
    os.makedirs('static/img', exist_ok=True)
    os.makedirs('templates', exist_ok=True)
    
    # Move HTML files to templates directory if they aren't there already
    template_files = ['base.html', 'index.html', 'experience.html', 'contact.html', 'dashboard.html']
    for file in template_files:
        source = os.path.join(os.path.dirname(__file__), file)
        destination = os.path.join(os.path.dirname(__file__), 'templates', file)
        if os.path.exists(source) and not os.path.exists(destination):
            with open(source, 'r', encoding='utf-8') as f:
                content = f.read()
            with open(destination, 'w', encoding='utf-8') as f:
                f.write(content)
            os.remove(source)  # Remove the source file after moving

    # Create styles.css in static/css if it doesn't exist
    css_source = os.path.join(os.path.dirname(__file__), 'style.css')
    css_dest = os.path.join(os.path.dirname(__file__), 'static', 'css', 'styles.css')
    if os.path.exists(css_source) and not os.path.exists(css_dest):
        with open(css_source, 'r', encoding='utf-8') as f:
            content = f.read()
        with open(css_dest, 'w', encoding='utf-8') as f:
            f.write(content)
        os.remove(css_source)  # Remove the source file after moving
            
    # Create main.js in static/js if it doesn't exist
    js_source = os.path.join(os.path.dirname(__file__), 'main.js')
    js_dest = os.path.join(os.path.dirname(__file__), 'static', 'js', 'main.js')
    if os.path.exists(js_source) and not os.path.exists(js_dest):
        with open(js_source, 'r', encoding='utf-8') as f:
            content = f.read()
        with open(js_dest, 'w', encoding='utf-8') as f:
            f.write(content)
        os.remove(js_source)  # Remove the source file after moving
    
    # Run the app in debug mode
    app.run(debug=True)