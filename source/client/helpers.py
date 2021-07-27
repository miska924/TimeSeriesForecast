from typing import List

def style_sheet_text(widget_name: str, color: str) -> str:
    return "QWidget#" + widget_name + " {\n" \
            "border: 2px solid " + color + ";\n" \
            "border-radius: 5px;\n" \
            "}"

def prettify_cv_data(errors):
    errors['mape'] = f"{errors['mape'] * 100 :.{3}f}%"
    errors['mse'] = f"{errors['mse']:.{3}f}"

def get_html_table_row(contents, header: bool = False):
        res = "<tr>"
        sep_start = "<th>" if header else "<td>"
        sep_end = "</th>" if header else "</td>"
        for elem in contents:
            res += sep_start + elem + sep_end
        res += "</tr>"
        return res

def get_table_html(headers: List[str], contents: List[str]):
    HTML = ""
    with open("cv_table.html") as html:
        line = html.readline()
        while line != "<table>":
            HTML += line
        HTML += get_html_table_row(headers, True)
        HTML += get_html_table_row(contents[0])
        HTML += get_html_table_row(contents[1])
        HTML += ''.join(html.readlines())
    return HTML

        