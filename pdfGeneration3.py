import pandas
from fpdf import FPDF

# A4 Page Size - 210 x 297 mm
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

# Page No
pgNo = 1

df = pandas.read_csv("topics.csv")

for index, dict in df.iterrows():

    # Add a Page
    pdf.add_page()

    # Style
    pdf.set_font(family="Times", size=24, style="B")
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=12, txt=dict["Topic"], align="L", ln=1)

    # Lines
    for line in range(20, 297, 20):
        pdf.line(10, line, 200, line)

    # Set footer on same page on Line
    pdf.ln(265)

    # Page No in Center
    pdf.set_font(family="Times", size=15, style="B")
    pdf.set_text_color(180, 180, 260)
    pdf.cell(w=0, h=8, txt=str(pgNo), ln=0, align="C")
    pgNo += 1

    # Set footer topic on Right
    pdf.set_font(family="Times", size=12, style="I")
    pdf.set_text_color(0, 0, 260)
    pdf.cell(w=0, h=8, txt=dict["Topic"], ln=1, align="R")

    # Set footer
    for i in range(dict["Pages"] - 1):
        # Add a Page for no of Pages in "topics.csv"
        pdf.add_page()

        # Lines
        for line in range(20, 297, 20):
            pdf.line(10, line, 200, line)

        # Set footer on Line No
        pdf.ln(275)

        # Page No in Center
        pdf.set_font(family="Times", size=15, style="B")
        pdf.set_text_color(180, 180, 260)
        pdf.cell(w=0, h=8, txt=str(pgNo), ln=0, align="C")
        pgNo += 1

        # Set footer
        pdf.set_font(family="Times", size=12, style="I")
        pdf.set_text_color(0, 0, 260)
        pdf.cell(w=0, h=8, txt=dict["Topic"], ln=1, align="R")

pdf.output("Page3.pdf")
