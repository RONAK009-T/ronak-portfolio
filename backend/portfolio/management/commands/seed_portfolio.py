from django.core.management.base import BaseCommand
from portfolio.models import Project, Skill, Experience, Education, Service, SocialLink, Resume
from datetime import date

class Command(BaseCommand):
    help = 'Seeds database with Ronak\'s portfolio data (Pure Django Edition)'

    def handle(self, *args, **options):
        self.stdout.write('Clearing existing data...')
        Project.objects.all().delete()
        Skill.objects.all().delete()
        Experience.objects.all().delete()
        Education.objects.all().delete()
        Service.objects.all().delete()
        SocialLink.objects.all().delete()
        Resume.objects.all().delete()

        self.stdout.write('Seeding services...')
        services_data = [
            {"title": "Full Stack Development", "description": "Building modern, responsive, end-to-end web applications with optimal scalability and robust performance.", "icon_name": "Layers", "order": 1},
            {"title": "Python Development", "description": "Writing clean, modular, and efficient Python code for automation, backend logic, and system integration.", "icon_name": "Terminal", "order": 2},
            {"title": "Django Development", "description": "Designing secure backend architectures, database schemas, and RESTful APIs using Django and Django REST Framework.", "icon_name": "Shield", "order": 3},
            {"title": "React Development", "description": "Crafting premium, interactive frontend user interfaces using modern state management and dynamic 3D elements.", "icon_name": "Cpu", "order": 4},
            {"title": "AI / GenAI Integration", "description": "Implementing intelligent features like custom LLM integrations, text-to-speech, computer vision, and speech processing.", "icon_name": "BrainCircuit", "order": 5},
            {"title": "Data Science", "description": "Analyzing complex datasets, extracting meaningful insights, and developing predictive machine learning models.", "icon_name": "BarChart", "order": 6},
        ]
        for s in services_data:
            Service.objects.create(**s)

        self.stdout.write('Seeding skills...')
        skills_data = [
            # Frontend
            {"name": "React.js", "category": "Frontend", "proficiency": 90, "icon_name": "Cpu"},
            {"name": "HTML5 / CSS3", "category": "Frontend", "proficiency": 95, "icon_name": "FileCode"},
            {"name": "JavaScript", "category": "Frontend", "proficiency": 88, "icon_name": "Code"},
            {"name": "Three.js / Canvas 2D", "category": "Frontend", "proficiency": 80, "icon_name": "Box"},
            
            # Backend
            {"name": "Python / Django", "category": "Backend", "proficiency": 95, "icon_name": "Terminal"},
            {"name": "MySQL / SQLite", "category": "Backend", "proficiency": 85, "icon_name": "Database"},
            
            # AI / Data Science
            {"name": "Gemini API", "category": "AI/Data Science", "proficiency": 88, "icon_name": "Sparkles"},
            {"name": "OpenCV / YOLO", "category": "AI/Data Science", "proficiency": 80, "icon_name": "Eye"},
            {"name": "Speech Recognition", "category": "AI/Data Science", "proficiency": 82, "icon_name": "Mic"},
            
            # Business & Commerce (B.Com)
            {"name": "Microsoft Excel (Pivots/Macros)", "category": "Tools", "proficiency": 95, "icon_name": "FileSpreadsheet"},
            {"name": "Microsoft PowerPoint (PPT/Slides)", "category": "Tools", "proficiency": 92, "icon_name": "Presentation"},
            {"name": "Financial Analysis", "category": "Tools", "proficiency": 85, "icon_name": "TrendingUp"},
            {"name": "Business Analytics", "category": "Tools", "proficiency": 82, "icon_name": "Briefcase"},
        ]
        for sk in skills_data:
            Skill.objects.create(**sk)

        self.stdout.write('Seeding experience...')
        experience_data = [
            {
                "role": "AI & Full Stack Developer",
                "company": "Freelance / Projects Development",
                "description": "Designing and building advanced AI-infused web platforms and responsive client portfolios.",
                "technologies": "Python, Django, React, MySQL, Gemini API, Three.js",
                "responsibilities": "Integrated state-of-the-art Generative AI features including speech interfaces and code reviews.\nBuilt modern responsive frontend apps utilizing Tailwind CSS and Framer Motion.\nConfigured secure relational database architectures with MySQL and Django ORM.",
                "start_date": "Jun 2024",
                "end_date": "Present",
                "current": True,
                "order": 1
            },
            {
                "role": "Software Engineering & Commerce Student",
                "company": "Academic Projects",
                "description": "Developed several enterprise and automation projects, centering on Python backend work, commercial calculations, and interactive systems.",
                "technologies": "Python, OpenCV, MediaPipe, Django, HTML/CSS/JS",
                "responsibilities": "Developed gesture tracking visualizers with MediaPipe and Canvas.\nImplemented custom network management services and image compression engines using OpenCV/YOLO.\nBuilt custom Excel spreadsheet analyzers and financial generators using Python.",
                "start_date": "Jul 2021",
                "end_date": "Jun 2024",
                "current": False,
                "order": 2
            }
        ]
        for exp in experience_data:
            Experience.objects.create(**exp)

        self.stdout.write('Seeding education...')
        education_data = [
            {
                "course": "B.Com (Bachelor of Commerce) — Final Year Student",
                "institute": "Technical & Commerce University",
                "year": "2023 - 2026",
                "grade_or_skills": "Specialized in Financial Analysis & IT Applications",
                "description": "Integrating core commercial concepts like accounting and analytics with python programming, database management, and AI models.",
                "order": 1
            }
        ]
        for edu in education_data:
            Education.objects.create(**edu)

        self.stdout.write('Seeding projects...')
        projects_data = [
            {
                "title": "AI Interview Assistant",
                "description": "An AI-powered technical mock interview platform that conducts voice-based interviews, translates and evaluates answers, and generates scores with detailed feedback.",
                "category": "AI & Django",
                "technologies": "Python, Django, React, Gemini API, Speech Recognition, Text-to-Speech",
                "features": "AI interview questions generation\nReal-time voice-to-text response parsing\nAccurate score generation based on response metrics\nPersonalized dashboard with performance analytical graphs",
                "github_url": "https://github.com/ronak/ai-interview-assistant",
                "live_url": "http://127.0.0.1:8001",
                "image_url": "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?q=80&w=600&auto=format&fit=crop",
                "featured": True,
                "created_date": date(2026, 8, 1),
                "local_path": r"C:\Users\RONAK\OneDrive\Desktop\django\ai_interview_assistant",
                "local_port": 8001
            },
            {
                "title": "AI Code Reviewer",
                "description": "AI-powered code analysis system that detects logical programming errors, explains code complexity, and generates optimized bug-free code blocks.",
                "category": "AI & Django",
                "technologies": "Python, Django, React, Gemini API, REST API",
                "features": "Logical bug and syntax error detection\nOptimized solution generation with runtime comparison\nSupports Python, Java, C++, and JavaScript code formats\nInteractive diff viewer showing the original and optimized code",
                "github_url": "https://github.com/ronak/ai-code-reviewer",
                "live_url": "http://127.0.0.1:8501",
                "image_url": "https://images.unsplash.com/photo-1607799279861-4dd421887fb3?q=80&w=600&auto=format&fit=crop",
                "featured": True,
                "created_date": date(2026, 7, 20),
                "local_path": r"C:\Users\RONAK\OneDrive\Desktop\django\AI_Code_Reviewer_Pro",
                "local_port": 8501
            },
            {
                "title": "Image Analyzer & Editor",
                "description": "A smart image editor and computer vision utility focusing on compression, resize, RGB color distribution and YOLO object detection.",
                "category": "Computer Vision",
                "technologies": "Python, Pillow, OpenCV, YOLO, Tkinter",
                "features": "Lossless image compression and file size (MB) reduction\nRGB distribution analyzer and dominant color extractor\nYOLO object detection and background removal\nAI Generated Image detector helper",
                "github_url": "https://github.com/ronak/image-analyzer-editor",
                "live_url": "",
                "image_url": "https://images.unsplash.com/photo-1541701494587-cb58502866ab?q=80&w=600&auto=format&fit=crop",
                "featured": False,
                "created_date": date(2026, 6, 15),
                "local_path": "",
                "local_port": None
            },
            {
                "title": "ChatConnect",
                "description": "A secure modern communication web app featuring channels, media exchange, and real-time JWT authentication.",
                "category": "React & Node.js",
                "technologies": "React, Node.js, Express, MySQL, JWT, Multer, Axios",
                "features": "WhatsApp-style clean messaging layout\nSecure token authentication and contact management\nDynamic multi-file sharing support (Images, Videos)\nInteractive audio player and message search features",
                "github_url": "https://github.com/ronak/chatconnect",
                "live_url": "http://127.0.0.1:3002",
                "image_url": "https://images.unsplash.com/photo-1611746872915-64382b5c76da?q=80&w=600&auto=format&fit=crop",
                "featured": True,
                "created_date": date(2026, 5, 10),
                "local_path": r"C:\Users\RONAK\Downloads\beautiful-react-tailwind-portfolio-main\beautiful-react-tailwind-portfolio-main",
                "local_port": 3002
            },
            {
                "title": "LuxTimepieces",
                "description": "Luxury watch e-commerce application equipped with a gorgeous visual product showcase, wishlist, cart logic, and checkout integrations.",
                "category": "React & MySQL",
                "technologies": "React, Node.js, Express, MySQL, Tailwind CSS",
                "features": "Futuristic interactive luxury product dashboard\nDynamic persistent cart and wishlist functionality\nSecure administrative dashboard for inventory edits\nInstant searching, filtering, and checkout simulations",
                "github_url": "https://github.com/ronak/luxtimepieces",
                "live_url": "http://127.0.0.1:3001",
                "image_url": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?q=80&w=600&auto=format&fit=crop",
                "featured": False,
                "created_date": date(2026, 4, 5),
                "local_path": r"C:\Users\RONAK\Downloads\shopMe_Ecommerce\shopMe_Ecommerce",
                "local_port": 3001
            },
            {
                "title": "My Hand Craft",
                "description": "An interactive e-commerce catalog featuring customized local handcrafted products with a modular inventory administrator console.",
                "category": "HTML/CSS & Node",
                "technologies": "HTML, CSS, JavaScript, Tailwind CSS, Node.js, MySQL",
                "features": "Fully responsive modular layout showcasing artisan pieces\nSecure SQL database connecting carts to order states\nResponsive admin dashboard highlighting orders and products",
                "github_url": "https://github.com/ronak/my-hand-craft",
                "live_url": "http://127.0.0.1:8004",
                "image_url": "https://images.unsplash.com/photo-1513519245088-0e12902e5a38?q=80&w=600&auto=format&fit=crop",
                "featured": False,
                "created_date": date(2026, 3, 10),
                "local_path": r"C:\Users\RONAK\OneDrive\Desktop\django\Furniture-Bazar-master",
                "local_port": 8004
            },
            {
                "title": "Anime World",
                "description": "An interactive anime encyclopedia detailing character records, strength comparison stats, wins/losses ratio, and official cinematic trailers.",
                "category": "React UI",
                "technologies": "React, JavaScript, CSS, REST API",
                "features": "Immersive character search with Jikan API integration\nInteractive visual charts mapping power levels and stats\nInteractive carousel showcasing cinematic trailers\nMobile responsive anime tracking lists",
                "github_url": "https://github.com/ronak/anime-world",
                "live_url": "http://127.0.0.1:8012",
                "image_url": "https://images.unsplash.com/photo-1578632767115-351597cf2477?q=80&w=600&auto=format&fit=crop",
                "featured": False,
                "created_date": date(2026, 2, 2),
                "local_path": r"C:\Users\RONAK\Downloads\NASA-Space-Apps-main\NASA-Space-Apps-main",
                "local_port": 8012
            },
            {
                "title": "Gesture Particle System",
                "description": "A computer vision visual canvas interface allowing real-time particle movement control through intuitive hand gesture commands.",
                "category": "HTML5 & CV",
                "technologies": "HTML, CSS, JavaScript, MediaPipe, Canvas, Computer Vision",
                "features": "Real-time AI hand-tracking using Google MediaPipe\nInteractive high-density HTML5 Canvas particle renderer\nSmooth, GPU-accelerated gesture movement response\nDynamic visual settings controls (velocity, count, colors)",
                "github_url": "https://github.com/ronak/gesture-particle-system",
                "live_url": "http://127.0.0.1:8011",
                "image_url": "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=600&auto=format&fit=crop",
                "featured": True,
                "created_date": date(2026, 1, 15),
                "local_path": r"C:\Users\RONAK\rfc\Gesture-Particle-System",
                "local_port": 8011
            },
            {
                "title": "LAN Device Management",
                "description": "A network scanning interface for scanning, discovering, and monitoring devices connected to the local area network with secure admin prompts.",
                "category": "Network & Django",
                "technologies": "Python, Django, Networking, HTML, CSS, JavaScript",
                "features": "Local area network IP pinging and ARP scans\nReal-time connection telemetry and authorized logs\nAdministrative approval triggers for system registrations\nOptimized performance using Python concurrent threads",
                "github_url": "https://github.com/ronak/lan-device-management",
                "live_url": "http://127.0.0.1:8002",
                "image_url": "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?q=80&w=600&auto=format&fit=crop",
                "featured": False,
                "created_date": date(2025, 12, 10),
                "local_path": r"C:\Users\RONAK\OneDrive\Desktop\django\College-ERP-main\College-ERP-main",
                "local_port": 8002
            }
        ]
        for p in projects_data:
            Project.objects.create(**p)

        self.stdout.write('Seeding social links...')
        socials_data = [
            {"platform": "GitHub", "url": "https://github.com/ronak", "icon_name": "Github", "order": 1},
            {"platform": "LinkedIn", "url": "https://linkedin.com/in/ronak", "icon_name": "Linkedin", "order": 2},
            {"platform": "Email", "url": "mailto:ronak@example.com", "icon_name": "Mail", "order": 3},
        ]
        for soc in socials_data:
            SocialLink.objects.create(**soc)

        self.stdout.write(self.style.SUCCESS('Successfully seeded all portfolio data!'))
