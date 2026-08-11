from django.core.management.base import BaseCommand
from students.models import Subject


class Command(BaseCommand):
    help = 'Seeds core engineering subjects for all major departments across 8 semesters.'

    def handle(self, *args, **kwargs):
        subjects_data = [
            # ==========================================
            # SEMESTER 1 (Common across Engineering)
            # ==========================================
            {"subject_code": "HS3151", "subject_name": "Professional English - I", "description": "Technical communication and vocabulary building."},
            {"subject_code": "MA3151", "subject_name": "Matrices and Calculus", "description": "Linear algebra, differential calculus, and partial derivatives."},
            {"subject_code": "PH3151", "subject_name": "Engineering Physics", "description": "Optics, laser, fiber optics, and quantum physics."},
            {"subject_code": "CY3151", "subject_name": "Engineering Chemistry", "description": "Electrochemistry, water technology, and nano-materials."},
            {"subject_code": "GE3151", "subject_name": "Problem Solving and Python Programming", "description": "Algorithmic thinking and basic programming using Python."},
            {"subject_code": "GE3152", "subject_name": "Heritage of Tamils", "description": "Cultural history, arts, and technology of ancient Tamils."},

            # ==========================================
            # SEMESTER 2 (General & Departmental Intro)
            # ==========================================
            {"subject_code": "HS3251", "subject_name": "Professional English - II", "description": "Advanced report writing and technical presentations."},
            {"subject_code": "MA3251", "subject_name": "Statistics and Numerical Methods", "description": "Probability distributions, linear equations, and numerical integration."},
            {"subject_code": "PH3256", "subject_name": "Physics for Information Science", "description": "Semiconductor theory and magnetic storage materials."},
            {"subject_code": "BE3251", "subject_name": "Basic Electrical and Electronics Engineering", "description": "AC/DC circuits, transformers, and semiconductor devices."},
            {"subject_code": "GE3251", "subject_name": "Engineering Graphics", "description": "Orthographic projections, isometric drawings, and CAD software."},
            {"subject_code": "GE3252", "subject_name": "Tamils and Technology", "description": "Engineering contributions of Tamils in agriculture and architecture."},

            # ==========================================
            # SEMESTER 3 (Core Fundamentals)
            # ==========================================
            # CSE / IT
            {"subject_code": "CS3351", "subject_name": "Digital Principles and Computer Organization", "description": "Logic gates, instruction pipeline, memory hierarchies."},
            {"subject_code": "CS3352", "subject_name": "Foundations of Data Science", "description": "Data wrangling, EDA, and statistical visualization."},
            {"subject_code": "CS3301", "subject_name": "Data Structures", "description": "Stacks, queues, linked lists, trees, and graphs."},
            {"subject_code": "CS3391", "subject_name": "Object Oriented Programming", "description": "OOP paradigms, classes, inheritance, polymorphism in Java."},
            {"subject_code": "MA3354", "subject_name": "Discrete Mathematics", "description": "Set theory, logic, combinatorics, and graph theory."},
            # ECE / EEE
            {"subject_code": "EC3351", "subject_name": "Signals and Systems", "description": "Continuous and discrete time signals, Fourier transform."},
            {"subject_code": "EE3301", "subject_name": "Electromagnetic Theory", "description": "Electrostatics, magnetostatics, and Maxwell's equations."},
            # MECH / CIVIL
            {"subject_code": "ME3381", "subject_name": "Kinematics of Machinery", "description": "Velocity, acceleration analysis, gears, and cams."},
            {"subject_code": "CE3301", "subject_name": "Fluid Mechanics", "description": "Fluid statics, dynamics, Bernoullis equation, and pipe flow."},

            # ==========================================
            # SEMESTER 4 (Intermediate Core)
            # ==========================================
            # CSE / IT
            {"subject_code": "CS3451", "subject_name": "Introduction to Operating Systems", "description": "Process scheduling, deadlocks, and virtual memory."},
            {"subject_code": "CS3491", "subject_name": "Artificial Intelligence and Machine Learning", "description": "Supervised/unsupervised models, neural nets, search algorithms."},
            {"subject_code": "CS3492", "subject_name": "Database Management Systems", "description": "Relational algebra, SQL, normalization, and ACID properties."},
            {"subject_code": "CS3401", "subject_name": "Algorithms", "description": "Divide and conquer, greedy, dynamic programming, NP-hardness."},
            # ECE / EEE
            {"subject_code": "EC3452", "subject_name": "Electromagnetic Fields", "description": "Wave propagation, guided waves, and transmission lines."},
            {"subject_code": "EE3402", "subject_name": "Linear Integrated Circuits", "description": "Op-amps, timers, Phase Locked Loops (PLL), and converters."},
            # MECH / CIVIL
            {"subject_code": "ME3491", "subject_name": "Thermal Engineering", "description": "Applied thermodynamics, steam cycles, and compressors."},
            {"subject_code": "CE3402", "subject_name": "Strength of Materials", "description": "Stresses, strains, bending moments, and deflection in beams."},

            # ==========================================
            # SEMESTER 5 (Advanced Technical)
            # ==========================================
            # CSE / IT
            {"subject_code": "CS3591", "subject_name": "Computer Networks", "description": "TCP/IP, routing, switching, MAC protocols, and network layer."},
            {"subject_code": "CS3501", "subject_name": "Compiler Design", "description": "Parsing, syntax-directed translation, code optimization."},
            {"subject_code": "CB3491", "subject_name": "Cryptography and Cyber Security", "description": "AES, RSA, public key infrastructure, and network defense."},
            # ECE / EEE
            {"subject_code": "EC3501", "subject_name": "Wireless Communication", "description": "Cellular concepts, fading channels, and modulation schemes."},
            {"subject_code": "EE3501", "subject_name": "Power System Analysis", "description": "Bus admittance matrix, load flow, and fault analysis."},
            # MECH / CIVIL
            {"subject_code": "ME3591", "subject_name": "Design of Machine Elements", "description": "Design against static/dynamic loads, shafts, and fasteners."},
            {"subject_code": "CE3501", "subject_name": "Structural Analysis - I", "description": "Indeterminate structures, energy methods, and slope deflection."},

            # ==========================================
            # SEMESTER 6 (Domain Specialization)
            # ==========================================
            # CSE / IT
            {"subject_code": "CS3691", "subject_name": "Embedded Systems and IoT", "description": "Microcontrollers, RTOS, sensor nodes, and cloud integration."},
            {"subject_code": "CS3601", "subject_name": "Software Engineering", "description": "Agile methodologies, UML, requirements, and testing."},
            {"subject_code": "CCS334", "subject_name": "Big Data Analytics", "description": "Hadoop, MapReduce, PySpark, and distributed processing."},
            {"subject_code": "CCS370", "subject_name": "UI/UX Design", "description": "Heuristic evaluation, wireframing, and Figma prototyping."},
            # ECE / EEE
            {"subject_code": "EC3601", "subject_name": "VLSI Design", "description": "CMOS logic circuitry, ASIC layout, and Verilog HDL."},
            {"subject_code": "EE3602", "subject_name": "Power Electronics", "description": "Inverters, converters, choppers, and motor drives."},
            # MECH / CIVIL
            {"subject_code": "ME3691", "subject_name": "Computer Aided Design and Manufacturing", "description": "CNC programming, FEA analysis, and additive manufacturing."},
            {"subject_code": "CE3601", "subject_name": "Design of Reinforced Concrete Elements", "description": "Limit state design of beams, columns, and slabs."},

            # ==========================================
            # SEMESTER 7 (Advanced Electives & Phase-1)
            # ==========================================
            {"subject_code": "CS3701", "subject_name": "Cloud Computing", "description": "Virtualization, AWS/Azure services, serverless deployment."},
            {"subject_code": "GE3791", "subject_name": "Human Values and Ethics", "description": "Engineering ethics, corporate responsibility, and integrity."},
            {"subject_code": "CCS335", "subject_name": "Deep Learning", "description": "CNN, RNN, Transformers, PyTorch/TensorFlow frameworks."},
            {"subject_code": "EC3701", "subject_name": "Optical Communication", "description": "Fiber attenuation, optical sources, and detectors."},
            {"subject_code": "ME3701", "subject_name": "Power Plant Engineering", "description": "Thermal, hydro, nuclear, and renewable power plants."},
            {"subject_code": "CE3701", "subject_name": "Estimation and Quantity Surveying", "description": "Cost estimation, valuation, and specification writing."},
            {"subject_code": "CS3711", "subject_name": "Project Work Phase - I", "description": "Domain selection, literature review, and architecture design."},

            # ==========================================
            # SEMESTER 8 (Management & Final Capstone)
            # ==========================================
            {"subject_code": "GE3792", "subject_name": "Industrial Management", "description": "Supply chain, operations research, and quality control (TQM)."},
            {"subject_code": "GE3793", "subject_name": "Total Quality Management", "description": "Six Sigma, ISO 9000, Benchmarking, and Quality Function Deployment."},
            {"subject_code": "CS3811", "subject_name": "Project Work Phase - II", "description": "Complete implementation, testing, deployment, and thesis defense."},
        ]

        created_count = 0
        updated_count = 0

        for data in subjects_data:
            subject, created = Subject.objects.get_or_create(
                subject_code=data["subject_code"],
                defaults={
                    "subject_name": data["subject_name"],
                    "description": data["description"]
                }
            )
            if created:
                created_count += 1
            else:
                # Update description or name if it already existed
                subject.subject_name = data["subject_name"]
                subject.description = data["description"]
                subject.save()
                updated_count += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully processed {len(subjects_data)} subjects! "
                f"(Created: {created_count}, Updated: {updated_count})"
            )
        )