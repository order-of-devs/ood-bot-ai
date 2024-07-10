from src.url.parser import parse_url


def tests_should_parse_youtube_url():
    url = "https://www.youtube.com/watch?v=6v2L2UGZJAM"
    parsed_url = parse_url(url)
    assert parsed_url.base_url == "www.youtube.com"
    assert parsed_url.path == "/watch"
    assert parsed_url.query == "v=6v2L2UGZJAM"


def tests_should_parse_youtube_short_url():
    url = "https://youtu.be/JRrxtwnvOek"
    parsed_url = parse_url(url)
    assert parsed_url.base_url == "www.youtube.com"
    assert parsed_url.path == "/watch"


