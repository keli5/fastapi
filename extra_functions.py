header = open("pages/templates/header.html").read()
footer = open("pages/templates/footer.html").read()


def fillin_hf(page_content):
    page_content = page_content.replace("%HEADER%", header)
    page_content = page_content.replace("%FOOTER", footer)
    return page_content
