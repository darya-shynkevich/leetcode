# TinyURL is a URL shortening service where you enter a URL
# such as https://leetcode.com/problems/design-tinyurl and it returns a short URL
# such as http://tinyurl.com/4e9iAk. Design a class to encode a URL and decode a tiny URL.
#
# There is no restriction on how your encode/decode algorithm should work.
# You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.
#
# Implement the Solution class:
#
# Solution() Initializes the object of the system.
# String encode(String longUrl) Returns a tiny URL for the given longUrl.
# String decode(String shortUrl) Returns the original long URL for the given shortUrl.
# It is guaranteed that the given shortUrl was encoded by the same object.

# Constraints:
#
# 1 <= url.length <= 10^4
# url is guranteed to be a valid URL.


class Codec:

    def __init__(self):
        self.short_to_long_url_map = {}

    def regenerate_short_url(self, current_long_url, longUrl):
        short_url = None
        while current_long_url:
            short_url = str(hash(longUrl))
            current_long_url = self.short_to_long_url_map.get(short_url)
        return short_url

    def encode(self, longUrl: str) -> str:
        short_url = str(hash(longUrl))

        current_long_url = self.short_to_long_url_map.get(short_url)
        if current_long_url != longUrl:
            short_url = self.regenerate_short_url(current_long_url, longUrl)

        self.short_to_long_url_map.update({short_url: longUrl})
        return short_url

    def decode(self, shortUrl: str) -> str:
        return self.short_to_long_url_map.get(shortUrl)


if __name__ == "__main__":
    codec = Codec()

    url = "https://leetcode.com/problems/design-tinyurl"
    assert codec.decode(codec.encode(url)) == url
