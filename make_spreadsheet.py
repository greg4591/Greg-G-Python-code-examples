"""Empty spreadsheet template.

Edit ROW_HEADERS (column A labels) and COLUMN_HEADERS (row 1 labels) below,
or pass them on the command line:

    python make_spreadsheet.py --rows Apples Oranges Pears --cols Jan Feb Mar -o fruit.xlsx
"""
import argparse
from importlib import import_module

_openpyxl = import_module("openpyxl")
_styles = import_module("openpyxl.styles")
_utils = import_module("openpyxl.utils")
Workbook = _openpyxl.Workbook
Alignment, Border, Font, PatternFill, Side = (
    _styles.Alignment,
    _styles.Border,
    _styles.Font,
    _styles.PatternFill,
    _styles.Side,
)
get_column_letter = _utils.get_column_letter

# ---- Change these as required ----
CORNER_LABEL = ""  # cell A1
COLUMN_HEADERS = ["Column 1", "Column 2", "Column 3", "Column 4", "Column 5"]  # B1, C1, ...
ROW_HEADERS = ["Row 1", "Row 2", "Row 3", "Row 4", "Row 5"]  # A2, A3, ...
SHEET_NAME = "Sheet1"
OUTPUT_FILE = "Python-Excel-01.xlsx"
# ----------------------------------


def build(row_headers, column_headers, corner="", sheet_name="Sheet1", output="Python-Excel-01.xlsx"):
    wb = Workbook()
    ws = wb.active
    ws.title = sheet_name

    header_font = Font(bold=True, color="FFFFFF")
    header_fill = PatternFill("solid", fgColor="4F81BD")
    thin = Side(style="thin", color="999999")
    border = Border(left=thin, right=thin, top=thin, bottom=thin)
    center = Alignment(horizontal="center", vertical="center")

    ws.cell(row=1, column=1, value=corner)
    for c, name in enumerate(column_headers, start=2):
        ws.cell(row=1, column=c, value=name)
    for r, name in enumerate(row_headers, start=2):
        ws.cell(row=r, column=1, value=name)

    for r in range(1, len(row_headers) + 2):
        for c in range(1, len(column_headers) + 2):
            cell = ws.cell(row=r, column=c)
            cell.border = border
            if r == 1 or c == 1:
                cell.font = header_font
                cell.fill = header_fill
                cell.alignment = center

    for c in range(1, len(column_headers) + 2):
        longest = max(len(str(ws.cell(row=r, column=c).value or "")) for r in range(1, len(row_headers) + 2))
        ws.column_dimensions[get_column_letter(c)].width = max(12, longest + 4)

    ws.freeze_panes = "B2"
    wb.save(output)
    return output


if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Generate an empty spreadsheet with custom headers.")
    p.add_argument("--rows", nargs="+", default=ROW_HEADERS, help="Labels for column A")
    p.add_argument("--cols", nargs="+", default=COLUMN_HEADERS, help="Labels for row 1")
    p.add_argument("--corner", default=CORNER_LABEL, help="Label for cell A1")
    p.add_argument("--sheet", default=SHEET_NAME, help="Sheet name")
    p.add_argument("-o", "--output", default=OUTPUT_FILE, help="Output .xlsx file")
    a = p.parse_args()
    print("Created", build(a.rows, a.cols, a.corner, a.sheet, a.output))
