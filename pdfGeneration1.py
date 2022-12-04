from fpdf import FPDF

# A4 Page Size - 210 x 297 mm
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()

pdf.set_font(family="Times", style="B", size=12)
pdf.set_text_color(100, 100, 100)
pdf.cell(w=0, h=12, txt="Hi! There", align="L", ln=1)

pdf.set_font(family="Times", size=12, style="B")
pdf.set_text_color(100, 100, 100)
pdf.cell(w=0, h=12, txt="Hello! There.", align="L", ln=1)


pdf.add_page()

pdf.set_font(family="Times", style="I", size=15)
pdf.set_text_color(100, 100, 100)
pdf.cell(w=1, h=12, txt="Hi! There", align="L", ln=1)

pdf.set_font(family="Times", size=15, style="I")
pdf.set_text_color(100, 100, 100)
pdf.cell(w=1, h=15, txt="Hello! There.", align="L", ln=1)

pdf.output("Page1.pdf")
