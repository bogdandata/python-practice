from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "CS50 Shirtificate", align="C", ln=1)

def main():
    name = input("Name: ")
    pdf = PDF()
    pdf.add_page()
    pdf.image("shirtificate.png", x=10, y=30, w=pdf.w - 20)
    pdf.set_font("Arial", "", 16)
    pdf.set_y(140)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(0, 10, f"This certifies that {name} has completed CS50", align="C", ln=1)
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()

