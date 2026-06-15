def extract_title(soup):
    if soup.title:
        return soup.title.string.strip()
    return ""


def extract_text(soup):
    texts = [p.get_text() for p in soup.find_all("p")]
    return " ".join(texts)


def extract_links(soup):
    return [a.get("href") for a in soup.find_all("a") if a.get("href")]