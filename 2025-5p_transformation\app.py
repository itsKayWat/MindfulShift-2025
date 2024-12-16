import customtkinter as ctk
from PIL import Image, ImageTk

class DetoxApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Configure window
        self.title("5P Transformation - Your Journey to Thriving in 2025")
        self.geometry("1400x900")
        
        # Set theme colors
        self.colors = {
            "primary": "#004d40",    # Dark emerald
            "secondary": "#ffd700",   # Yellow
            "text_light": "#ffffff", 
            "text_dark": "#333333",
            "background": "#001f1a",  # Darker emerald
            "accent": "#00796b"       # Medium emerald
        }
        
        # Set theme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        
        # Initialize pages dictionary
        self.pages = {}
        self.current_page = None
        
        # Create UI
        self.setup_ui()

    def setup_ui(self):
        # Configure grid
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Create sidebar
        self.create_sidebar()
        
        # Create main content
        self.create_main_content()
        
        # Create pages
        self.create_pages()
        
        # Show welcome page by default
        self.show_page("🏠 Welcome")

    def create_pages(self):
        """Create all application pages"""
        self.pages = {
            "🏠 Welcome": self.create_welcome_page,
            "👥 People Detox": self.create_people_page,
            "🏠 Places Detox": self.create_places_page,
            "👤 Personal Growth": self.create_personal_page,
            "💼 Professional Growth": self.create_professional_page,
            "🎯 Purpose Discovery": self.create_purpose_page,
            "📝 Journal": self.create_journal_page,
            "📊 Progress": self.create_progress_page
        }

    def create_sidebar(self):
        # Sidebar frame
        self.sidebar = ctk.CTkFrame(
            self,
            fg_color=self.colors["primary"],
            width=250
        )
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.sidebar.grid_propagate(False)

        # App title
        title = ctk.CTkLabel(
            self.sidebar,
            text="5P Transformation",
            font=("Helvetica", 24, "bold"),
            text_color=self.colors["secondary"]
        )
        title.pack(pady=30)

        # Navigation buttons
        nav_items = [
            "🏠 Welcome",
            "👥 People Detox",
            "🏠 Places Detox",
            "👤 Personal Growth",
            "💼 Professional Growth",
            "🎯 Purpose Discovery",
            "📝 Journal",
            "📊 Progress"
        ]

        for item in nav_items:
            btn = ctk.CTkButton(
                self.sidebar,
                text=item,
                fg_color="transparent",
                text_color=self.colors["text_light"],
                hover_color=self.colors["accent"],
                anchor="w",
                command=lambda x=item: self.show_page(x)
            )
            btn.pack(pady=5, padx=20, fill="x")

    def create_main_content(self):
        # Main content frame
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(0, weight=1)

    def show_page(self, page_name):
        """Switch to the selected page"""
        # Clear current page
        if self.current_page:
            self.current_page.destroy()
        
        # Create new page
        if page_name in self.pages:
            self.current_page = self.pages[page_name]()
            self.current_page.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
        
        print(f"Showing page: {page_name}")

    def create_welcome_page(self):
        """Create welcome page"""
        page = ctk.CTkFrame(self.main_frame)
        
        # Welcome message
        welcome = ctk.CTkLabel(
            page,
            text="Welcome to Your 2025 Transformation Journey",
            font=("Helvetica", 32, "bold"),
            text_color=self.colors["secondary"]
        )
        welcome.pack(pady=50)

        # Motivation quote
        quote = ctk.CTkLabel(
            page,
            text="'We're not just surviving, we're thriving in 2025'",
            font=("Helvetica", 18, "italic"),
            text_color=self.colors["text_light"]
        )
        quote.pack(pady=20)

        # Get Started button
        start_btn = ctk.CTkButton(
            page,
            text="Begin Your Journey",
            font=("Helvetica", 16, "bold"),
            fg_color=self.colors["accent"],
            hover_color=self.colors["primary"],
            command=self.start_journey
        )
        start_btn.pack(pady=30)
        
        return page

    def create_people_page(self):
        """Create people detox page"""
        page = ctk.CTkFrame(self.main_frame)
        
        title = ctk.CTkLabel(
            page,
            text="People Detox",
            font=("Helvetica", 32, "bold"),
            text_color=self.colors["secondary"]
        )
        title.pack(pady=30)
        
        description = ctk.CTkLabel(
            page,
            text="Transform your relationships and social connections",
            font=("Helvetica", 16),
            text_color=self.colors["text_light"]
        )
        description.pack(pady=20)
        
        return page

    def create_places_page(self):
        """Create places detox page"""
        page = ctk.CTkFrame(self.main_frame)
        
        title = ctk.CTkLabel(
            page,
            text="Places Detox",
            font=("Helvetica", 32, "bold"),
            text_color=self.colors["secondary"]
        )
        title.pack(pady=30)
        
        description = ctk.CTkLabel(
            page,
            text="Optimize your environment for success",
            font=("Helvetica", 16),
            text_color=self.colors["text_light"]
        )
        description.pack(pady=20)
        
        return page

    def create_personal_page(self):
        """Create personal growth page"""
        page = ctk.CTkFrame(self.main_frame)
        
        title = ctk.CTkLabel(
            page,
            text="Personal Growth",
            font=("Helvetica", 32, "bold"),
            text_color=self.colors["secondary"]
        )
        title.pack(pady=30)
        
        return page

    def create_professional_page(self):
        """Create professional growth page"""
        page = ctk.CTkFrame(self.main_frame)
        
        title = ctk.CTkLabel(
            page,
            text="Professional Growth",
            font=("Helvetica", 32, "bold"),
            text_color=self.colors["secondary"]
        )
        title.pack(pady=30)
        
        return page

    def create_purpose_page(self):
        """Create purpose discovery page"""
        page = ctk.CTkFrame(self.main_frame)
        
        title = ctk.CTkLabel(
            page,
            text="Purpose Discovery",
            font=("Helvetica", 32, "bold"),
            text_color=self.colors["secondary"]
        )
        title.pack(pady=30)
        
        return page

    def create_journal_page(self):
        """Create journal page"""
        page = ctk.CTkFrame(self.main_frame)
        
        title = ctk.CTkLabel(
            page,
            text="Journal",
            font=("Helvetica", 32, "bold"),
            text_color=self.colors["secondary"]
        )
        title.pack(pady=30)
        
        # Add journal entry field
        journal_entry = ctk.CTkTextbox(
            page,
            width=800,
            height=400,
            font=("Helvetica", 14)
        )
        journal_entry.pack(pady=20)
        
        # Save button
        save_btn = ctk.CTkButton(
            page,
            text="Save Entry",
            font=("Helvetica", 16),
            fg_color=self.colors["accent"],
            hover_color=self.colors["primary"]
        )
        save_btn.pack(pady=20)
        
        return page

    def create_progress_page(self):
        """Create progress page"""
        page = ctk.CTkFrame(self.main_frame)
        
        title = ctk.CTkLabel(
            page,
            text="Progress Tracking",
            font=("Helvetica", 32, "bold"),
            text_color=self.colors["secondary"]
        )
        title.pack(pady=30)
        
        return page

    def start_journey(self):
        """Start the transformation journey"""
        self.show_page("👥 People Detox")

if __name__ == "__main__":
    app = DetoxApp()
    app.mainloop()