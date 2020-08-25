def fillin_hf(page_content):
    header = open("pages/templates/header.html").read()
    headerc = open("pages/templates/headercode.html").read()
    footer = open("pages/templates/footer.html").read()

    page_content = page_content.replace("%HEADER%", header)
    page_content = page_content.replace("%HCODE%", headerc)
    page_content = page_content.replace("%FOOTER%", footer)
    return page_content
