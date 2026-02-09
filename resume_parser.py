import fitz
import re


class ResumeParser:
    """
    A class to parse resume PDFs using PyMuPDF
    """

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.text = ""

    def load_pdf(self):
        """Open PDF and extract all text"""
        doc = fitz.open(self.file_path)
        pages_text = []

        for page in doc:
            pages_text.append(page.get_text())

        self.text = "\n".join(pages_text)

    def extract_email(self):
        match = re.search(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", self.text)
        return match.group(0) if match else None

    def extract_phone(self):
        match = re.search(r"\+?\d[\d\s\-]{8,15}", self.text)
        return match.group(0) if match else None

    def extract_skills(self):
        keywords = ["python", "java", "sql", "machine learning",
                    "data science", "html", "css", "javascript"]

        found = []
        lower_text = self.text.lower()

        for skill in keywords:
            if skill in lower_text:
                found.append(skill)

        return found

    def parse(self):
        """Main controller method"""
        self.load_pdf()

        return {
            "email": self.extract_email(),
            "phone": self.extract_phone(),
            "skills": self.extract_skills(),
            "raw_text": self.text[:1000]  # preview
        }


class ResumeApp:
    """
    Application layer
    """

    def run(self):
        path = input("Enter resume PDF path: ")

        parser = ResumeParser(path)
        data = parser.parse()

        print("\n--- Resume Data ---")
        for key, value in data.items():
            print(f"{key}: {value}")


if __name__ == "__main__":
    app = ResumeApp()
    app.run()
