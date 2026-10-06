"""All portfolio content in one place. Edit this file to update the site."""

PROFILE = {
    "name": "Vandana Kumari",
    "role": "Software developer",
    "location": "Bengaluru, Karnataka",
    "email": "k.vandana2468@gmail.com",
    "phone": "+91-8218171976",
    "github": "https://github.com/Vandana-2029",
    "linkedin": "https://www.linkedin.com/in/vandana-kumari1",
    "tagline": (
        "I build backends in Python and Flask, and I like problems where "
        "images carry more than they show: biometrics, steganography and "
        "computer vision."
    ),
    "about": [
        "I'm a Computer Science graduate from MIET Meerut (B.Tech, 2026) "
        "looking for my first full-time role in software development.",
        "Most of my projects start with a Flask API and end with something "
        "a person can actually use: an ear-based login system, a parking lot "
        "that tells you where the free slot is, a tool that hides encrypted "
        "messages inside ordinary photos.",
        "I work comfortably across C++, Python, Java, SQL and JavaScript, and "
        "I care about the fundamentals underneath: data structures, DBMS, "
        "operating systems and networks.",
    ],
    "open_to": "Open to fresher roles in backend, full-stack and QA engineering.",
}

SKILLS = [
    ("Languages", ["C++", "Python", "Java", "SQL", "JavaScript", "HTML5", "CSS3"]),
    ("Backend", ["Flask", "RESTful APIs", "API design", "Authentication", "JWT", "CRUD"]),
    ("Frontend", ["React.js", "React Hooks", "State management", "Responsive design"]),
    ("Data", ["MySQL", "MongoDB", "SQLite", "Data modeling", "Query optimization"]),
    ("Tools", ["Git & GitHub", "Docker", "Linux", "OpenCV", "AWS"]),
    ("Core CS", ["DSA", "OOP", "DBMS", "Operating systems", "Computer networks"]),
]

PROJECTS = [
    {
        "slug": "ear-biometric",
        "title": "Ear Biometric",
        "date": "Feb 2024",
        "featured": True,
        "summary": "A login system that identifies people by the shape of their ear.",
        "stack": ["Python", "OpenCV", "Flask"],
        "repo": "https://github.com/Vandana-2029/ear-biometric",
        "points": [
            "Extracts features from ear images to identify and authenticate users.",
            "Flask REST APIs handle registration, authentication and image upload.",
            "OpenCV preprocessing and feature extraction improve matching accuracy.",
            "Images are stored by ear category, so feature lookup searches a smaller set.",
        ],
    },
    {
        "slug": "securesteg",
        "title": "SecureSteg",
        "date": "Jun 2025",
        "featured": True,
        "summary": "Hides an encrypted message inside an image, readable only with the right key.",
        "stack": ["Python", "Flask", "Pillow"],
        "repo": "https://github.com/Vandana-2029/SecureSteg",
        "points": [
            "Two layers of protection: the message is encrypted, then written into the image's least significant bits.",
            "Even if someone extracts the hidden bits, they can't read them without the key.",
            "Key-based workflow for embedding and retrieving messages through a web UI.",
        ],
    },
    {
        "slug": "automated-parking",
        "title": "Automated Vehicle Parking",
        "date": "Nov 2024",
        "featured": True,
        "summary": "Watches a parking lot through a camera and points drivers to the nearest free slot.",
        "stack": ["Python", "OpenCV"],
        "repo": "https://github.com/Vandana-2029/Automated_Parking",
        "points": [
            "OpenCV vehicle detection marks each slot as occupied or free in real time.",
            "A recommendation step finds the nearest available space.",
            "An interface shows live occupancy across the lot.",
        ],
    },
    {
        "slug": "taskflow",
        "title": "TaskFlow",
        "date": "2025",
        "featured": False,
        "summary": "A team task manager with projects, assignments and secure sign-in.",
        "stack": ["React", "Flask", "SQLite", "JWT"],
        "repo": "https://github.com/Vandana-2029/TaskFlow-Team-Task-Manager",
        "points": [
            "Flask backend with SQLAlchemy models for users, projects and tasks.",
            "JWT authentication with protected routes on the React side.",
            "Dashboard, project and task views built from reusable components.",
        ],
    },
    {
        "slug": "meeting-notes",
        "title": "AI Meeting Notes Summarizer",
        "date": "2025",
        "featured": False,
        "summary": "Turns a meeting transcript into a structured summary and emails it.",
        "stack": ["Node.js", "Express", "Groq Llama 3.1", "Resend"],
        "repo": "https://github.com/Vandana-2029/AI-Summarized-Meeting-Notes",
        "demo": "https://ai-summarized-meeting-notes.onrender.com",
        "points": [
            "Upload or paste a transcript and add a custom instruction.",
            "Produces decisions, action items and next steps; editable before sending.",
            "Sends the summary to one or more recipients by email.",
        ],
    },
    {
        "slug": "file-encryptor",
        "title": "File Encryptor",
        "date": "2024",
        "featured": False,
        "summary": "Password-based file encryption, available as CLI, desktop and web app.",
        "stack": ["Python", "Tkinter", "Flask", "JavaScript"],
        "repo": "https://github.com/Vandana-2029/File-Encryptor",
        "points": [
            "The same encryption core wrapped in three interfaces: command line, Tkinter and Flask.",
            "A pure HTML/JS version runs entirely in the browser.",
        ],
    },
]

EDUCATION = [
    {
        "period": "2022 – 2026",
        "title": "B.Tech, Computer Science",
        "place": "Meerut Institute of Engineering & Technology",
        "detail": "CGPA 7.6",
    },
    {
        "period": "2020 – 2021",
        "title": "Senior Secondary",
        "place": "Army Public School, Meerut",
        "detail": "83.2%",
    },
]

CERTIFICATES = [
    ("AWS Certified Cloud Practitioner", "Amazon Web Services", "2026"),
    ("Web Developer Bootcamp with Flask & Python", "Udemy", "2025"),
    ("Data Structures", "LinkedIn Learning", "2025"),
    ("Level Up: C++", "LinkedIn Learning", "2025"),
]

BEYOND = [
    "Captained the college volleyball team to first place in the zonals and a spot in the state-level tournament.",
    "Won first place in the inter-college zonal basketball championship.",
]


def get_project(slug):
    return next((p for p in PROJECTS if p["slug"] == slug), None)
