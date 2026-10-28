# Listing 4.8: Cleaning a social media post
import html
import re
import emoji

def clean_web_text(text):
    text = html.unescape(text)                           # &amp; -> &
    text = re.sub(r"<[^>]+>", " ", text)                 # strip HTML tags
    text = re.sub(r"https?://\S+|www\.\S+", " <URL> ", text)
    text = re.sub(r"@\w+", " <USER> ", text)             # anonymize mentions
    text = re.sub(
        r"#(\w+)",
        lambda m: " " + re.sub(r"(?<=[a-z])(?=[A-Z])", " ", m.group(1)),
        text,
    )
    # 😍 -> :smiling_face_with_heart-eyes:
    text = emoji.demojize(text, delimiters=(" :", ": "))
    text = re.sub(r"(\w)\1{2,}", r"\1\1", text)          # soooo -> soo
    return re.sub(r"\s+", " ", text).strip()

post = ("@lena_k Sooooo happy with my order 😍 &amp; fast shipping!! "
        "#CustomerService https://t.co/xyz")
print(clean_web_text(post))
