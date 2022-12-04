from fpdf import FPDF
import pandas

# A4 Page Size - 210 x 297 mm
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pandas.read_csv("topics.csv")

# Page No
pgNo = 1

for index, dict in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=dict["Topic"], align="L", ln=1)
    pdf.line(10, 21, 200, 21)

    # Set footer
    pdf.ln(265)
    pdf.set_font(family="Times", size=12, style="I")
    pdf.set_text_color(0, 0, 260)
    pdf.cell(w=0, h=10, txt=dict["Topic"], align="R", ln=1)

    for page in range(dict["Pages"] - 1):
        # Set footer for next pages
        pdf.add_page()
        pdf.ln(275)
        pdf.set_font(family="Times", size=12, style="I")
        pdf.set_text_color(0, 0, 260)
        pdf.cell(w=0, h=10, txt=dict["Topic"], align="R", ln=1)

pdf.output("Page2.pdf")
