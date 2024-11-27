import pathlib
from django.http import HttpResponse

this_dir = pathlib.Path(__file__).resolve().parent

def home_page_view(request, *args, **kwargs):
    my_title = "My page"
    my_context = {
        "page_title": my_title
    } # dictionary
    html_file_path = this_dir / "home.html"
    html_ = html_file_path.read_text()
    return HttpResponse(html_)


def old_home_page_view(request, *args, **kwargs):
    my_title = "My page"
    my_context = {
        "page_title": my_title
    } # dictionary

    inline_html = """
    <!DOCTYPE html>
    <html>
        <body>
            <h1>{page_title}</h1>
        </body>
    </html>
""".format(**my_context)

    html_file_path = this_dir / "home.html"
    html_ = html_file_path.read_text()
    return HttpResponse(inline_html)